"""
Gideon Utility Functions Module
================================
Helper functions for speech recognition, text-to-speech, file operations,
and system interactions.

Author: Muhammad Ali (CodeCelix Internship)
"""

# Vosk Audio Handler - Offline speech recognition (replaces speech_recognition)
from audio_handler import get_audio_handler, VoskAudioHandler
import pyttsx3
import logging
import subprocess
import webbrowser
import pywhatkit
from pathlib import Path
from datetime import datetime
from typing import Tuple, Optional, List
import sys
import config

# Initialize logger
logger = logging.getLogger(__name__)

# ==================== TEXT-TO-SPEECH ENGINE ====================
# Global TTS engine instance
_tts_engine: Optional[pyttsx3.Engine] = None


def initialize_tts() -> pyttsx3.Engine:
    """
    Initialize and configure the text-to-speech engine.

    Returns:
        Configured pyttsx3 engine instance

    Raises:
        RuntimeError: If TTS engine initialization fails
    """
    global _tts_engine

    if _tts_engine is None:
        try:
            _tts_engine = pyttsx3.init()

            # Configure voice settings
            _tts_engine.setProperty('rate', config.TTS_RATE)
            _tts_engine.setProperty('volume', config.TTS_VOLUME)

            # Try to set preferred voice
            voices = _tts_engine.getProperty('voices')
            if voices and len(voices) > config.TTS_VOICE_INDEX:
                _tts_engine.setProperty('voice', voices[config.TTS_VOICE_INDEX].id)

            logger.info("TTS engine initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize TTS engine: {e}")
            raise RuntimeError(f"TTS initialization failed: {e}")

    return _tts_engine


def speak(text: str, log: bool = True) -> bool:
    """
    Convert text to speech using pyttsx3.
    Gideon speaks the provided text.

    Args:
        text: The text to speak
        log: Whether to log the spoken text

    Returns:
        True if speech was successful, False otherwise
    """
    try:
        if log:
            logger.info(f"Gideon speaking: {text}")

        engine = initialize_tts()
        engine.say(text)
        engine.runAndWait()
        return True

    except Exception as e:
        logger.error(f"Speech error: {e}")
        print(f"[Gideon Error] Could not speak: {text}")
        return False


# ==================== SPEECH RECOGNITION (VOSK - OFFLINE) ====================
def listen_for_command(timeout: int = config.RECOGNITION_TIMEOUT) -> Optional[str]:
    """
    Listen for voice input and convert to text using Vosk offline recognition.
    Replaces Google Speech Recognition API with 100% offline solution.

    Args:
        timeout: Maximum seconds to wait for speech

    Returns:
        Recognized text in lowercase, or None if recognition failed
    """
    try:
        logger.info("Listening for command (Vosk offline mode)...")

        # Get global audio handler (singleton pattern)
        handler = get_audio_handler()

        # Listen for command using Vosk
        command = handler.listen_once(
            duration=timeout,
            phrase_time_limit=config.RECOGNITION_PHRASE_LIMIT,
            silence_threshold=config.SILENCE_THRESHOLD
        )

        if command is None:
            logger.debug("No speech detected or timeout")
            return None

        if not command or command.strip() == "":
            logger.warning("Empty command received")
            return "unknown"

        logger.info(f"Recognized command: {command}")
        return command  # Already lowercase from Vosk

    except FileNotFoundError as e:
        logger.error(f"Vosk model not found: {e}")
        speak("Audio model not found. Please run vosk setup.")
        return None

    except Exception as e:
        logger.error(f"Unexpected error in speech recognition: {e}")
        speak(config.RESPONSES["microphone_error"])
        return None


def listen_with_retry(max_attempts: int = config.MAX_RETRY_ATTEMPTS) -> Optional[str]:
    """
    Listen for command with automatic retry on failure.

    Args:
        max_attempts: Maximum number of retry attempts

    Returns:
        Recognized command or None if all attempts failed
    """
    for attempt in range(max_attempts):
        command = listen_for_command()

        if command is not None and command != "unknown":
            return command

        if command == "unknown" and attempt < max_attempts - 1:
            speak(config.RESPONSES["repeat_request"])

    logger.warning(f"Failed to recognize command after {max_attempts} attempts")
    return None


# ==================== APPLICATION MANAGEMENT ====================
def open_application(app_name: str) -> Tuple[bool, str]:
    """
    Launch a Windows application.

    Args:
        app_name: Name of the application to open

    Returns:
        (success: bool, message: str) tuple
    """
    try:
        # Get application executable from config
        app_key = app_name.lower()
        app_executable = config.APPLICATIONS.get(app_key)

        if not app_executable:
            message = f"Application '{app_name}' not found in configuration"
            logger.warning(message)
            return False, message

        # Special handling for Chrome - use detected path
        if app_key in ["chrome", "google chrome"]:
            if config.CHROME_PATH:
                subprocess.Popen([config.CHROME_PATH])
                message = f"Opened {app_name}"
                logger.info(message)
                return True, message
            else:
                # Fallback to default browser
                webbrowser.open("https://www.google.com")
                message = "Chrome not found, opened default browser"
                logger.warning(message)
                return True, message

        # Special handling for Windows settings
        elif app_executable.startswith("ms-"):
            subprocess.Popen(["start", app_executable], shell=True)
        else:
            subprocess.Popen([app_executable], shell=True)

        message = f"Opened {app_name}"
        logger.info(message)
        return True, message

    except FileNotFoundError:
        message = config.RESPONSES["app_not_found"].format(app=app_name)
        logger.error(message)
        return False, message

    except Exception as e:
        message = f"Error opening {app_name}: {str(e)}"
        logger.error(message)
        return False, message


# ==================== WEB OPERATIONS ====================
def open_website(website_name: str) -> Tuple[bool, str]:
    """
    Open a website in the default browser.

    Args:
        website_name: Name or URL of the website

    Returns:
        (success: bool, message: str) tuple
    """
    try:
        # Check if it's a known website
        website_key = website_name.lower()
        url = config.WEBSITES.get(website_key, website_name)

        # Add https:// if not present
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"

        webbrowser.open(url)

        message = f"Opened {website_name}"
        logger.info(message)
        return True, message

    except Exception as e:
        message = f"Error opening website: {str(e)}"
        logger.error(message)
        return False, message


def open_chrome_with_url(url: str) -> Tuple[bool, str]:
    """
    Open Chrome browser with a specific URL.

    Args:
        url: URL to open in Chrome

    Returns:
        (success: bool, message: str) tuple
    """
    try:
        # Add https:// if not present
        if not url.startswith(('http://', 'https://')):
            url = f"https://{url}"

        # Try to open in Chrome
        if config.CHROME_PATH:
            subprocess.Popen([config.CHROME_PATH, url])
            message = f"Opened {url} in Chrome"
            logger.info(message)
            return True, message
        else:
            # Fallback to default browser
            webbrowser.open(url)
            message = f"Opened {url} in default browser (Chrome not found)"
            logger.warning(message)
            return True, message

    except Exception as e:
        message = f"Error opening URL: {str(e)}"
        logger.error(message)
        return False, message


def play_on_youtube(query: str) -> Tuple[bool, str]:
    """
    Play a video on YouTube using pywhatkit (auto-plays first matching video).
    This is a KEY feature of Gideon.

    Args:
        query: Search query for the video/song

    Returns:
        (success: bool, message: str) tuple
    """
    try:
        if not config.ENABLE_YOUTUBE:
            return False, "YouTube feature is disabled"

        logger.info(f"Playing on YouTube: {query}")
        speak(f"Playing {query} on YouTube")

        # Use pywhatkit to search and play the video
        # This automatically opens the first matching video and starts playback
        pywhatkit.playonyt(query)

        # Give browser time to open
        import time
        time.sleep(1)

        message = f"Playing '{query}' on YouTube"
        logger.info(message)
        return True, message

    except Exception as e:
        message = f"Could not play YouTube video: {str(e)}"
        logger.error(message)
        speak("Sorry, I couldn't open YouTube. Please check your internet connection.")
        return False, message


def extract_youtube_query(command: str) -> str:
    """
    Extract video/song name from various YouTube command formats.

    Handles variations like:
    - "play coldplay on youtube" -> "coldplay"
    - "search for python tutorial on youtube" -> "python tutorial"
    - "youtube despacito" -> "despacito"
    - "play some coldplay music" -> "coldplay music"

    Args:
        command: The voice command string

    Returns:
        Extracted query string
    """
    command = command.lower().strip()

    # Remove common trigger phrases
    patterns_to_remove = [
        "play ",
        "search ",
        "search for ",
        "on youtube",
        "in youtube",
        "youtube ",
        "on yt",
        "play on youtube ",
        "some ",
        "music",
    ]

    for pattern in patterns_to_remove:
        command = command.replace(pattern, "")

    return command.strip()


# ==================== SYSTEM INFORMATION ====================
def get_current_time() -> str:
    """
    Get the current time in 12-hour format.

    Returns:
        Formatted time string
    """
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    return time_str


def get_current_date() -> str:
    """
    Get the current date in a readable format.

    Returns:
        Formatted date string
    """
    now = datetime.now()
    date_str = now.strftime("%B %d, %Y")  # e.g., "January 07, 2026"
    return date_str


def get_time_based_greeting() -> str:
    """
    Return a greeting based on current time of day.

    Returns:
        Appropriate greeting message
    """
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 17:
        return "Good afternoon"
    elif 17 <= current_hour < 21:
        return "Good evening"
    else:
        return "Good night"


# ==================== FILE OPERATIONS ====================
def create_folder(folder_name: str, parent_dir: Optional[Path] = None) -> Tuple[bool, str]:
    """
    Create a new folder.

    Args:
        folder_name: Name of the folder to create
        parent_dir: Parent directory (defaults to Desktop)

    Returns:
        (success: bool, message: str) tuple
    """
    try:
        if parent_dir is None:
            parent_dir = config.DESKTOP_DIR

        folder_path = parent_dir / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)

        message = f"Created folder: {folder_path}"
        logger.info(message)
        return True, message

    except Exception as e:
        message = f"Error creating folder: {str(e)}"
        logger.error(message)
        return False, message


def list_files(directory: Path, extension: Optional[str] = None) -> List[Path]:
    """
    List files in a directory, optionally filtered by extension.

    Args:
        directory: Directory to search
        extension: File extension filter (e.g., ".mp3")

    Returns:
        List of file paths
    """
    try:
        if not directory.exists():
            logger.warning(f"Directory does not exist: {directory}")
            return []

        if extension:
            files = list(directory.glob(f"*{extension}"))
        else:
            files = [f for f in directory.iterdir() if f.is_file()]

        return files

    except Exception as e:
        logger.error(f"Error listing files: {e}")
        return []


def play_music_file(file_path: Path) -> Tuple[bool, str]:
    """
    Play a music file using the default media player.

    Args:
        file_path: Path to the music file

    Returns:
        (success: bool, message: str) tuple
    """
    try:
        if not file_path.exists():
            return False, f"File not found: {file_path}"

        # Open with default application
        subprocess.Popen(["start", str(file_path)], shell=True)

        message = f"Playing: {file_path.name}"
        logger.info(message)
        return True, message

    except Exception as e:
        message = f"Error playing music: {str(e)}"
        logger.error(message)
        return False, message


def clean_downloads_folder() -> Tuple[bool, str]:
    """
    Clean downloads folder by organizing files.
    With confirmation prompt for safety.

    Returns:
        (success: bool, message: str) tuple
    """
    try:
        # Ask for confirmation
        if not ask_confirmation("organize your downloads folder"):
            return False, "Action cancelled by user"

        downloads_dir = config.DOWNLOADS_DIR

        if not downloads_dir.exists():
            return False, "Downloads folder not found"

        # Count files to organize
        files = [f for f in downloads_dir.iterdir() if f.is_file()]
        file_count = len(files)

        if file_count == 0:
            speak("Downloads folder is already clean")
            return True, "No files to organize"

        speak(f"Organizing {file_count} files")

        # Create organized folders
        folders_to_create = {
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
            "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
            "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
            "Installers": [".exe", ".msi", ".dmg"],
            "Others": []
        }

        # Create folders
        for folder_name in folders_to_create.keys():
            folder_path = downloads_dir / folder_name
            folder_path.mkdir(exist_ok=True)

        # Move files
        moved_count = 0
        for file_path in files:
            extension = file_path.suffix.lower()
            moved = False

            for folder_name, extensions in folders_to_create.items():
                if extension in extensions:
                    dest = downloads_dir / folder_name / file_path.name
                    try:
                        file_path.rename(dest)
                        moved_count += 1
                        moved = True
                    except Exception as e:
                        logger.warning(f"Could not move {file_path.name}: {e}")
                    break

            # Move to Others if not categorized
            if not moved and folder_name != "Others":
                dest = downloads_dir / "Others" / file_path.name
                try:
                    file_path.rename(dest)
                    moved_count += 1
                except Exception as e:
                    logger.warning(f"Could not move {file_path.name}: {e}")

        message = f"Organized {moved_count} files in downloads folder"
        speak(f"Done! Organized {moved_count} files.")
        logger.info(message)
        return True, message

    except Exception as e:
        message = f"Error cleaning downloads: {str(e)}"
        logger.error(message)
        return False, message


def delete_file_safe(file_path: Path) -> Tuple[bool, str]:
    """
    Delete a file with confirmation.

    Args:
        file_path: Path to file to delete

    Returns:
        (success: bool, message: str) tuple
    """
    try:
        if not file_path.exists():
            return False, f"File not found: {file_path}"

        # Ask for confirmation
        if not ask_confirmation(f"delete {file_path.name}"):
            return False, "Deletion cancelled by user"

        file_path.unlink()
        message = f"Deleted: {file_path.name}"
        speak(message)
        logger.info(message)
        return True, message

    except Exception as e:
        message = f"Error deleting file: {str(e)}"
        logger.error(message)
        return False, message


# ==================== LOGGING SETUP ====================
def setup_logging() -> logging.Logger:
    """
    Configure logging for Gideon.
    Creates timestamped log files in the logs directory.

    Returns:
        Configured logger instance
    """
    # Create logs directory if it doesn't exist
    config.LOGS_DIR.mkdir(exist_ok=True)

    # Generate log filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = config.LOGS_DIR / f"{config.LOG_FILE_PREFIX}_{timestamp}.log"

    # Configure logging
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format=config.LOG_FORMAT,
        datefmt=config.LOG_DATE_FORMAT,
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger("Gideon")
    logger.info("=" * 60)
    logger.info(f"Gideon v{config.VERSION} - Logging initialized")
    logger.info(f"Log file: {log_file}")
    logger.info("=" * 60)

    return logger


# ==================== COMMAND PARSING ====================
def extract_youtube_query(command: str) -> Optional[str]:
    """
    Extract the search query from a YouTube command.
    Handles variations like "play X on youtube", "search X youtube", etc.

    Args:
        command: Raw voice command

    Returns:
        Extracted search query or None
    """
    command_lower = command.lower()

    # Try different patterns
    patterns = [
        ("play ", " on youtube"),
        ("play ", " youtube"),
        ("search ", " on youtube"),
        ("search ", " youtube"),
        ("play ", ""),
    ]

    for start, end in patterns:
        if start in command_lower:
            query = command_lower.split(start, 1)[1]
            if end and end in query:
                query = query.split(end)[0]
            return query.strip()

    return None


def ask_confirmation(action: str, timeout: int = 10) -> bool:
    """
    Ask user for confirmation before critical action.

    Args:
        action: Description of action (e.g., "delete files")
        timeout: Seconds to wait for response (default: 10)

    Returns:
        True if user confirms, False otherwise
    """
    try:
        speak(f"Are you sure you want to {action}? Say yes or no.")
        logger.info(f"Asking confirmation for: {action}")

        # Listen for response
        response = listen_for_command(timeout=timeout)

        if not response:
            speak("I didn't hear a response. Cancelling for safety.")
            logger.warning("No confirmation response received")
            return False

        response_lower = response.lower().strip()

        # Check for confirmation
        yes_phrases = ["yes", "yeah", "sure", "confirm", "do it", "go ahead", "proceed", "ok", "okay", "affirmative"]
        no_phrases = ["no", "nope", "cancel", "don't", "stop", "nevermind", "never mind", "negative"]

        for phrase in yes_phrases:
            if phrase in response_lower:
                speak("Confirmed. Proceeding.")
                logger.info(f"Action confirmed: {action}")
                return True

        for phrase in no_phrases:
            if phrase in response_lower:
                speak("Cancelled.")
                logger.info(f"Action cancelled: {action}")
                return False

        # Unclear response
        speak("I didn't understand. Cancelling for safety.")
        logger.warning(f"Unclear confirmation response: {response}")
        return False

    except Exception as e:
        logger.error(f"Error in confirmation prompt: {str(e)}")
        speak("Error getting confirmation. Cancelling for safety.")
        return False


def check_for_shutdown(command: str) -> bool:
    """
    Check if the command is a shutdown trigger.
    Enhanced with better recognition for exit commands.

    Supports multiple variations:
    - "quit gideon" / "gideon quit"
    - "exit gideon" / "gideon exit"
    - "goodbye gideon" / "gideon goodbye"
    - "stop gideon" / "gideon stop"
    - Simple: "quit", "exit", "goodbye" (as fallbacks)

    Args:
        command: Voice command to check

    Returns:
        True if command should shutdown Gideon, False otherwise
    """
    if not command:
        return False

    command_lower = command.lower().strip()

    # Remove common filler words for better matching
    filler_words = ["please", "can you", "could you", "would you", "now", "the", "application"]
    for filler in filler_words:
        command_lower = command_lower.replace(filler, "").strip()

    # Priority exit phrases (most reliable)
    priority_exits = [
        "quit gideon",
        "gideon quit",
        "exit gideon",
        "gideon exit",
        "goodbye gideon",
        "gideon goodbye",
        "stop gideon",
        "gideon stop",
        "close gideon",
        "gideon close"
    ]

    # Check priority exits first
    for trigger in priority_exits:
        if trigger in command_lower:
            logger.info(f"Shutdown triggered by priority command: {command}")
            return True

    # Check for standalone exit words (only if they're the complete command)
    # This prevents false positives like "exit vim" or "quit chrome"
    standalone_exits = ["quit", "exit", "goodbye", "bye"]
    if command_lower in standalone_exits:
        logger.info(f"Shutdown triggered by standalone command: {command}")
        return True

    # Check all other triggers from config
    for trigger in config.SHUTDOWN_TRIGGERS:
        if trigger in command_lower:
            logger.info(f"Shutdown triggered by config trigger: {command}")
            return True

    return False


def normalize_command(command: str) -> str:
    """
    Normalize a command by applying aliases and cleaning.

    Args:
        command: Raw command string

    Returns:
        Normalized command string
    """
    command_lower = command.lower().strip()

    # Check aliases
    for base_command, aliases in config.COMMAND_ALIASES.items():
        if command_lower in aliases:
            return base_command

    return command_lower


# ==================== VALIDATION ====================
def validate_microphone() -> bool:
    """
    Check if microphone is accessible using Vosk audio handler.

    Returns:
        True if microphone is available, False otherwise
    """
    try:
        handler = get_audio_handler()
        # Test microphone for 2 seconds
        result = handler.test_microphone(duration=2)
        return result
    except Exception as e:
        logger.error(f"Microphone validation failed: {e}")
        return False


def display_startup_banner() -> None:
    """
    Display Gideon's ASCII art logo and startup information.
    """
    print(config.GIDEON_LOGO)
    print(f"\nDeveloper: {config.DEVELOPER}")
    print(f"Organization: {config.ORGANIZATION}")
    print(f"Version: {config.VERSION}")
    print(f"\nInitializing {config.ASSISTANT_NAME}...")
    print("-" * 60)


# ==================== ERROR HANDLING ====================
def handle_error(error: Exception, context: str = "") -> str:
    """
    Handle errors gracefully and return user-friendly message.

    Args:
        error: The exception that occurred
        context: Additional context about where the error occurred

    Returns:
        User-friendly error message
    """
    error_msg = f"{context}: {str(error)}" if context else str(error)
    logger.error(f"Error handled: {error_msg}")

    # Return appropriate message
    return config.RESPONSES["error_occurred"].format(error=str(error))
