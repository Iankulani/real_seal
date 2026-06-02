@echo off
:: install.bat
:: REAL SEAL HT - Windows Batch Installation Script

title REAL SEAL HT Installer
color 0A
echo ================================================
echo    REAL SEAL HT - Windows Installation
echo ================================================
echo.

:: Check Administrator
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Please run as Administrator
    pause
    exit /b 1
)

:: Check Python
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.7+
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Create virtual environment
echo [2/6] Creating virtual environment...
python -m venv venv
if %errorLevel% neq 0 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)

:: Activate and install
echo [3/6] Installing dependencies...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt

:: Create directories
echo [4/6] Creating directories...
mkdir .real_seal 2>nul
mkdir .real_seal\reports 2>nul
mkdir .real_seal\phishing_pages 2>nul
mkdir .real_seal\keylogs 2>nul
mkdir .real_seal\ssh_keys 2>nul
mkdir .real_seal\wordlists 2>nul
mkdir .real_seal\traffic_logs 2>nul
mkdir .real_seal\spoof_logs 2>nul
mkdir .real_seal\captured_credentials 2>nul

:: Create start script
echo [5/6] Creating start script...
(
echo @echo off
echo call venv\Scripts\activate.bat
echo python real_seal.py
echo pause
) > start.bat

:: Create desktop shortcut
echo [6/6] Creating desktop shortcut...
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%USERPROFILE%\Desktop\REAL_SEAL.lnk'); $SC.TargetPath = '%CD%\start.bat'; $SC.WorkingDirectory = '%CD%'; $SC.Save()"

echo.
echo ================================================
echo    Installation Complete!
echo ================================================
echo.
echo To start REAL SEAL:
echo   - Run start.bat
echo   - Or click the desktop shortcut
echo.
echo Web Interface: http://localhost:5000
echo.
pause