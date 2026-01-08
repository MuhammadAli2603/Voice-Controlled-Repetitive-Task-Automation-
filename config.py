"""
Gideon Configuration Module
===========================
Central configuration for the Gideon voice assistant system.
Contains all settings, constants, and configurable parameters.

Author: Muhammad Ali (CodeCelix Internship)
"""

from pathlib import Path
from typing import Dict, List

# ==================== GIDEON IDENTITY ====================
ASSISTANT_NAME = "Gideon"
VERSION = "1.0.0"
GREETING_MESSAGE = "Gideon online. All systems operational. How may I assist you?"
SHUTDOWN_MESSAGE = "Shutting down. Goodbye!"

# ==================== ASCII ART LOGO ====================
GIDEON_LOGO = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     ██████╗ ██╗██████╗ ███████╗ ██████╗ ███╗   ██╗      ║
║    ██╔════╝ ██║██╔══██╗██╔════╝██╔═══██╗████╗  ██║      ║
║    ██║  ███╗██║██║  ██║█████╗  ██║   ██║██╔██╗ ██║      ║
║    ██║   ██║██║██║  ██║██╔══╝  ██║   ██║██║╚██╗██║      ║
║    ╚██████╔╝██║██████╔╝███████╗╚██████╔╝██║ ╚████║      ║
║     ╚═════╝ ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝      ║
║                                                           ║
║           Voice-Controlled Task Automation System         ║
║                      Version 1.0.0                        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
"""

# ==================== VOSK AUDIO CONFIGURATION ====================
# Vosk Offline Speech Recognition (Replaces PyAudio/Google Speech API)

# Path to Vosk model directory
# Download models using: python vosk_setup.py
# Recommended: vosk-model-small-en-us-0.15 (40MB)
VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"

# Audio Settings for Vosk
SAMPLE_RATE = 16000  # 16kHz optimal for speech recognition
AUDIO_CHANNELS = 1   # Mono audio (required for Vosk)
AUDIO_DEVICE_INDEX = None  # None = default microphone, or specify device index

# Recognition Settings
RECOGNITION_TIMEOUT = 5  # Seconds to wait for speech to start
RECOGNITION_PHRASE_LIMIT = 8  # Maximum seconds for complete phrase (reduced for faster response)
SILENCE_THRESHOLD = 100.0  # Volume threshold to detect speech (LOWERED for better sensitivity)
MAX_RETRY_ATTEMPTS = 3  # Number of times to ask user to repeat on failure

# Multi-Language Support
ENABLE_URDU_RECOGNITION = False  # Set to True to enable Urdu speech recognition
URDU_MODEL_PATH = "vosk-model-small-ur-0.3"  # Path to Urdu model (download separately)

# ==================== SPEECH SETTINGS (Legacy - Kept for TTS) ====================
# Text-to-Speech Configuration
TTS_RATE = 175  # Words per minute (default: 200, slower: 150)
TTS_VOLUME = 0.9  # Volume level (0.0 to 1.0)
TTS_VOICE_INDEX = 1  # Voice index (0: male, 1: female - if available)

# Legacy Settings (Deprecated - Using Vosk now)
# These are kept for backward compatibility but not used
RECOGNITION_ENERGY_THRESHOLD = 4000  # No longer used with Vosk
RECOGNITION_PAUSE_THRESHOLD = 0.8  # No longer used with Vosk

# ==================== DIRECTORY PATHS ====================
# Project directories
BASE_DIR = Path(__file__).parent.resolve()
LOGS_DIR = BASE_DIR / "logs"
MUSIC_DIR = Path.home() / "Music"
DOWNLOADS_DIR = Path.home() / "Downloads"
DOCUMENTS_DIR = Path.home() / "Documents"
DESKTOP_DIR = Path.home() / "Desktop"

# Create directories if they don't exist
LOGS_DIR.mkdir(exist_ok=True)

# ==================== APPLICATION PATHS ====================
# Common Windows applications
APPLICATIONS: Dict[str, str] = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "excel": "excel.exe",
    "word": "winword.exe",
    "powerpoint": "powerpnt.exe",
    "vs code": "code",
    "visual studio code": "code",
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
    "firefox": "firefox.exe",
    "explorer": "explorer.exe",
    "file explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "settings": "ms-settings:",
    "command prompt": "cmd.exe",
    "powershell": "powershell.exe",
}

# ==================== BROWSER CONFIGURATION ====================
import os

# Chrome installation paths (checked in order)
CHROME_PATHS: List[str] = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
]

def find_chrome_path() -> str:
    """Find Chrome executable path on Windows"""
    for path in CHROME_PATHS:
        if os.path.exists(path):
            return path
    return None

# Detected Chrome path (None if not found)
CHROME_PATH = find_chrome_path()

# YouTube Configuration
YOUTUBE_BASE_URL = "https://www.youtube.com/results?search_query="
USE_CHROME_FOR_YOUTUBE = True  # Force Chrome for YouTube when available

# ==================== WEBSITE URLS ====================
# Frequently accessed websites
WEBSITES: Dict[str, str] = {
    "google": "https://www.google.com",
    "gmail": "https://mail.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "stack overflow": "https://stackoverflow.com",
    "linkedin": "https://www.linkedin.com",
    "twitter": "https://twitter.com",
    "facebook": "https://www.facebook.com",
    "reddit": "https://www.reddit.com",
    "chatgpt": "https://chat.openai.com",
    "claude": "https://claude.ai",
    "weather": "https://weather.com",
    "news": "https://news.google.com",
    "maps": "https://maps.google.com",
}

# ==================== SHUTDOWN COMMANDS ====================
# Commands that will terminate Gideon (expanded for better recognition)
SHUTDOWN_TRIGGERS: List[str] = [
    # Primary commands (most reliable)
    "quit gideon",
    "gideon quit",
    "exit gideon",
    "gideon exit",
    "goodbye gideon",
    "gideon goodbye",
    "stop gideon",
    "gideon stop",
    # Variations
    "shutdown gideon",
    "gideon shutdown",
    "shut down gideon",
    "gideon shut down",
    "close gideon",
    "gideon close",
    # Simple fallbacks (use with caution)
    "quit",
    "exit",
    "goodbye",
]

# ==================== WAKE WORDS ====================
# Words that activate Gideon (optional - can be always listening)
WAKE_WORDS: List[str] = [
    "gideon",
    "hey gideon",
    "ok gideon",
]

# ==================== COMMAND ALIASES ====================
# Alternative ways to invoke the same command
COMMAND_ALIASES: Dict[str, List[str]] = {
    "time": ["what time is it", "tell me the time", "current time", "what's the time"],
    "date": ["what date is it", "tell me the date", "current date", "what's the date", "today's date"],
    "help": ["what can you do", "list commands", "show commands", "available commands", "your capabilities"],
}

# ==================== GREETINGS ====================
# Time-based greetings
MORNING_GREETINGS = ["Good morning", "Good morning sir", "Morning"]
AFTERNOON_GREETINGS = ["Good afternoon", "Good afternoon sir", "Afternoon"]
EVENING_GREETINGS = ["Good evening", "Good evening sir", "Evening"]
NIGHT_GREETINGS = ["Good night", "Working late?", "Good night sir"]

# ==================== RESPONSE TEMPLATES ====================
# Standard response messages
RESPONSES = {
    "listening": "Listening...",
    "processing": "Processing...",
    "done": "Done.",
    "opening_app": "Opening {app} for you.",
    "opening_website": "Opening {website}.",
    "playing_youtube": "Playing {query} on YouTube.",
    "unknown_command": "I'm not sure how to do that. Try saying 'help' for available commands.",
    "error_occurred": "I encountered an error: {error}",
    "repeat_request": "I didn't catch that. Could you please repeat?",
    "microphone_error": "I'm having trouble accessing the microphone. Please check your audio settings.",
    "network_error": "I need an internet connection for that command.",
    "app_not_found": "I couldn't find {app}. Is it installed?",
    "success": "Task completed successfully.",
    "cancelled": "Operation cancelled.",
    "confirm_request": "Are you sure? Say yes to confirm or no to cancel.",
    "you_are_welcome": "You're welcome!",
    "acknowledged": "Acknowledged.",
}

# ==================== MUSIC FILE EXTENSIONS ====================
AUDIO_EXTENSIONS = [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".wma"]

# ==================== LOGGING CONFIGURATION ====================
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_FILE_PREFIX = "gideon_log"
LOG_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

# ==================== FEATURE FLAGS ====================
# Enable/disable features
ENABLE_YOUTUBE = True
ENABLE_EMAIL = False  # Requires email configuration
ENABLE_WEATHER = False  # Requires weather API key
ENABLE_COMMAND_HISTORY = True
ENABLE_VOICE_CONFIRMATION = True  # Gideon confirms actions verbally

# ==================== SAFETY SETTINGS ====================
# Commands that require confirmation
DANGEROUS_OPERATIONS = [
    "delete",
    "remove",
    "clean",
    "format",
    "shutdown system",
    "restart system",
]

REQUIRE_CONFIRMATION = True  # Ask before executing dangerous operations

# ==================== YOUTUBE SETTINGS ====================
YOUTUBE_TRIGGERS = [
    "play",
    "search",
    "show me",
    "find",
    "look up",
]

YOUTUBE_KEYWORDS = [
    "on youtube",
    "youtube",
    "video",
    "song",
    "music",
]

# ==================== SYSTEM INFO ====================
SUPPORTED_PLATFORMS = ["Windows"]
PYTHON_VERSION_REQUIRED = "3.8+"

# ==================== DEVELOPER INFO ====================
DEVELOPER = "Muhammad Ali"
ORGANIZATION = "CodeCelix"
PROJECT_TYPE = "AI Engineer Internship Project"
INSPIRATION = "Named after the AI from The Flash"
