#!/bin/bash
# install.sh
# REAL SEAL HT - Linux/macOS Installation Script

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}"
echo "================================================"
echo "   REAL SEAL HT - Installation Script"
echo "================================================"
echo -e "${NC}"

# Check root
if [[ $EUID -eq 0 ]]; then
   echo -e "${YELLOW}[WARNING] Running as root is not recommended${NC}"
fi

# Check Python
echo -e "${GREEN}[1/8] Checking Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[ERROR] Python 3 not found. Please install Python 3.7+${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if (( $(echo "$PYTHON_VERSION < 3.7" | bc -l) )); then
    echo -e "${RED}[ERROR] Python 3.7+ required (found $PYTHON_VERSION)${NC}"
    exit 1
fi

# Install system dependencies (Linux only)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo -e "${GREEN}[2/8] Installing system dependencies...${NC}"
    if command -v apt-get &> /dev/null; then
        sudo apt-get update
        sudo apt-get install -y python3-pip python3-dev libffi-dev libssl-dev \
            libpcap-dev nmap whois dnsutils hping3 arping net-tools \
            iproute2 iptables openssh-client chromium-browser chromium-chromedriver
    elif command -v yum &> /dev/null; then
        sudo yum install -y python3-pip python3-devel libffi-devel openssl-devel \
            libpcap-devel nmap whois bind-utils hping3 arping net-tools \
            iproute iptables openssh-clients chromium
    elif command -v pacman &> /dev/null; then
        sudo pacman -S python-pip python-virtualenv libffi openssl \
            libpcap nmap whois dnsutils hping3 arping net-tools \
            iptables openssh chromium
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "${GREEN}[2/8] Installing Homebrew dependencies...${NC}"
    if ! command -v brew &> /dev/null; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install python@3.11 libffi openssl nmap whois hping3 net-tools
fi

# Create virtual environment
echo -e "${GREEN}[3/8] Creating virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo -e "${GREEN}[4/8] Upgrading pip...${NC}"
pip install --upgrade pip

# Install requirements
echo -e "${GREEN}[5/8] Installing Python packages...${NC}"
pip install -r requirements.txt

# Create directories
echo -e "${GREEN}[6/8] Creating directories...${NC}"
mkdir -p .real_seal/{reports,phishing_pages,keylogs,ssh_keys,wordlists,traffic_logs,spoof_logs,captured_credentials}
mkdir -p logs

# Create environment file
echo -e "${GREEN}[7/8] Creating configuration...${NC}"
if [ ! -f .env ]; then
    cat > .env << EOF
# REAL SEAL Configuration
REAL_SEAL_API_KEY=$(openssl rand -hex 32 2>/dev/null || python3 -c "import secrets; print(secrets.token_hex(32))")
REAL_SEAL_ADMIN_USER=admin
REAL_SEAL_ADMIN_PASS=$(openssl rand -base64 16 2>/dev/null || python3 -c "import secrets; print(secrets.token_urlsafe(16))")
REAL_SEAL_LOG_LEVEL=INFO
REAL_SEAL_MODE=production

# Bot Tokens (optional)
# DISCORD_BOT_TOKEN=
# TELEGRAM_API_ID=
# TELEGRAM_API_HASH=
# TELEGRAM_BOT_TOKEN=
# SLACK_BOT_TOKEN=
EOF
    chmod 600 .env
fi

# Create start script
echo -e "${GREEN}[8/8] Creating start script...${NC}"
cat > start.sh << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
python3 real_seal.py "$@"
EOF
chmod +x start.sh

# Create systemd service (Linux only)
if [[ "$OSTYPE" == "linux-gnu"* ]] && command -v systemctl &> /dev/null; then
    SERVICE_FILE="/etc/systemd/system/real-seal.service"
    if [ ! -f "$SERVICE_FILE" ]; then
        echo -e "${YELLOW}Create systemd service? (y/n)${NC}"
        read -r create_service
        if [[ "$create_service" == "y" ]]; then
            CURRENT_DIR=$(pwd)
            CURRENT_USER=$(whoami)
            sudo bash -c "cat > $SERVICE_FILE" << EOF
[Unit]
Description=REAL SEAL HT Cybersecurity Framework
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
WorkingDirectory=$CURRENT_DIR
ExecStart=$CURRENT_DIR/start.sh
Restart=on-failure
RestartSec=10
StandardOutput=append:$CURRENT_DIR/logs/stdout.log
StandardError=append:$CURRENT_DIR/logs/stderr.log

[Install]
WantedBy=multi-user.target
EOF
            sudo systemctl daemon-reload
            echo -e "${GREEN}Service created. Use:${NC}"
            echo "  sudo systemctl start real-seal"
            echo "  sudo systemctl enable real-seal"
        fi
    fi
fi

# Completion
echo -e "${GREEN}"
echo "================================================"
echo "   Installation Complete!"
echo "================================================"
echo -e "${NC}"
echo -e "To start REAL SEAL:"
echo -e "  ${BLUE}./start.sh${NC}"
echo ""
echo -e "Or run directly:"
echo -e "  ${BLUE}source venv/bin/activate && python3 real_seal.py${NC}"
echo ""
echo -e "Web Interface: ${GREEN}http://localhost:5000${NC}"
echo -e "Admin Credentials saved in: ${BLUE}.env${NC}"
echo ""
echo -e "Default password can be found in .env file"
echo -e "${YELLOW}IMPORTANT: Change the default password immediately!${NC}"