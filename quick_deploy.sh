#!/bin/bash
# quick_deploy.sh
# One-command deployment for REAL SEAL HT

set -e

echo "🚀 REAL SEAL HT - Quick Deploy"
echo "================================"

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "🐳 Installing Docker..."
    curl -fsSL https://get.docker.com | sh
    sudo usermod -aG docker $USER
fi

# Check Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "📦 Installing Docker Compose..."
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

# Clone or update
if [ ! -d "real-seal" ]; then
    git clone https://gitlab.com/ian-kulani/real-seal.git real-seal
fi

cd real-seal

# Generate secrets
echo "🔐 Generating secrets..."
echo "REAL_SEAL_API_KEY=$(openssl rand -hex 32)" > .env
echo "REAL_SEAL_ADMIN_USER=admin" >> .env
echo "REAL_SEAL_ADMIN_PASS=$(openssl rand -base64 16)" >> .env
echo "REAL_SEAL_LOG_LEVEL=INFO" >> .env
echo "REAL_SEAL_MODE=production" >> .env

# Build and start
echo "🏗️ Building and starting containers..."
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build

# Wait for health
echo "⏳ Waiting for services to be ready..."
sleep 30

# Show status
echo ""
echo "✅ Deployment Complete!"
echo "========================"
echo "🌐 Web Interface: http://localhost:5000"
echo "👤 Username: admin"
echo "🔑 Password: $(grep REAL_SEAL_ADMIN_PASS .env | cut -d= -f2)"
echo ""
echo "📋 Commands:"
echo "  docker-compose logs -f    # View logs"
echo "  docker-compose down       # Stop services"
echo "  docker-compose up -d      # Start services"