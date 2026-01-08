"""
Gideon Multi-Language Support
==============================
Comprehensive multi-language support for Gideon voice assistant.
Currently supports English and Roman Urdu (Urdu written in Latin script).

Features:
- Command translation from Roman Urdu to English
- Bilingual responses
- Natural language matching with fuzzy logic
- Extensible architecture for adding more languages

Author: Muhammad Ali (CodeCelix Internship)
"""

import logging
import re
from typing import Optional, Dict, Tuple, List

logger = logging.getLogger("Gideon.Multilingual")


# ==================== ROMAN URDU COMMAND MAPPINGS ====================

# Greetings and Social
GREETINGS_URDU = {
    "salam": "hello",
    "salam alaikum": "hello",
    "adaab": "hello",
    "assalam o alaikum": "hello",
    "kya haal hai": "how are you",
    "kaise ho": "how are you",
    "kya chal raha hai": "how are you",
    "theek ho": "how are you",
    "shukriya": "thank you",
    "meherbani": "thank you",
    "bohot shukriya": "thank you very much",
    "khuda hafiz": "goodbye",
    "allah hafiz": "goodbye",
}

# Applications
APPLICATIONS_URDU = {
    "chrome kholo": "open chrome",
    "chrome chalao": "open chrome",
    "notepad kholo": "open notepad",
    "notepad chalao": "open notepad",
    "calculator kholo": "open calculator",
    "calculator chalao": "open calculator",
    "excel kholo": "open excel",
    "excel chalao": "open excel",
    "word kholo": "open word",
    "word chalao": "open word",
    "vs code kholo": "open vs code",
    "vs code chalao": "open vs code",
    "file explorer kholo": "open file explorer",
    "explorer kholo": "open file explorer",
}

# YouTube and Media
YOUTUBE_URDU = {
    "gaana chalao": "play music",
    "gaana bajao": "play music",
    "music chalao": "play music",
    "music bajao": "play music",
    "youtube kholo": "open youtube",
    "youtube par": "on youtube",  # Used in combinations
    "video chalao": "play video",
    "video dikhaao": "play video",
}

# Websites
WEBSITES_URDU = {
    "google kholo": "open google",
    "gmail kholo": "open gmail",
    "github kholo": "open github",
    "facebook kholo": "open facebook",
    "youtube website kholo": "open youtube",
}

# Files and Folders
FILES_URDU = {
    "folder banao": "create folder",
    "folder banaao": "create folder",
    "naya folder": "new folder",
    "naya folder banao": "create folder",
    "downloads saaf karo": "clean downloads",
    "downloads organize karo": "organize downloads",
    "file organize karo": "organize files",
    "files organize karo": "organize files",
}

# System Information
SYSTEM_URDU = {
    "time batao": "what time is it",
    "time kya hai": "what time is it",
    "waqt batao": "what time is it",
    "date batao": "what is the date",
    "date kya hai": "what is the date",
    "aaj ki date": "today's date",
    "tarikh batao": "what is the date",
}

# Workflows
WORKFLOWS_URDU = {
    "kaam shuru karo": "start workday",
    "kaam ka time": "start workday",
    "din shuru karo": "start workday",
    "coding shuru karo": "start coding",
    "code likhna hai": "start coding",
    "kaam khatam": "end workday",
    "kaam khatam karo": "end workday",
    "din khatam": "end workday",
    "focus mode": "start focus mode",
    "dhyaan lagana hai": "start focus mode",
    "break chahiye": "take a break",
    "aaram chahiye": "take a break",
    "thak gaya": "take a break",
}

# Control Commands
CONTROL_URDU = {
    "band karo": "quit gideon",
    "band ho jao": "quit gideon",
    "gideon band karo": "quit gideon",
    "exit karo": "exit gideon",
    "madad": "help",
    "madad chahiye": "help",
    "madad karo": "help",
    "kya kar sakte ho": "what can you do",
    "theek hai": "okay",
    "haan": "yes",
    "nahi": "no",
    "nahin": "no",
}

# Combine all dictionaries
ALL_URDU_COMMANDS = {
    **GREETINGS_URDU,
    **APPLICATIONS_URDU,
    **YOUTUBE_URDU,
    **WEBSITES_URDU,
    **FILES_URDU,
    **SYSTEM_URDU,
    **WORKFLOWS_URDU,
    **CONTROL_URDU,
}


# ==================== URDU RESPONSE TEMPLATES ====================

RESPONSES_URDU = {
    # Confirmations
    "okay": "theek hai",
    "done": "ho gaya",
    "yes": "haan",
    "no": "nahi",
    "understood": "samajh gaya",
    "i understand": "main samajh gaya",

    # Actions
    "opening": "khol raha hoon",
    "playing": "chala raha hoon",
    "creating": "bana raha hoon",
    "cleaning": "saaf kar raha hoon",
    "organizing": "organize kar raha hoon",
    "starting": "shuru kar raha hoon",
    "stopping": "band kar raha hoon",

    # Greetings
    "hello": "salam",
    "good morning": "subah bakhair",
    "good afternoon": "dopehr bakhair",
    "good evening": "shaam bakhair",
    "good night": "shab bakhair",
    "goodbye": "khuda hafiz",
    "thank you": "shukriya",
    "you're welcome": "koi baat nahi",

    # Questions
    "how may i help you": "main aap ki kya madad kar sakta hoon",
    "what can i do": "main kya kar sakta hoon",
    "ready": "tayyar hoon",

    # Status
    "shutting down": "band ho raha hoon",
    "starting up": "shuru ho raha hoon",
    "listening": "sun raha hoon",
    "processing": "process kar raha hoon",
    "working": "kaam kar raha hoon",

    # Errors
    "error": "kharaabi",
    "sorry": "maaf kijiye",
    "i didn't understand": "main samjha nahi",
    "please repeat": "dobara kahiye",
    "not found": "nahi mila",
}


# ==================== TRANSLATION FUNCTIONS ====================

def translate_urdu_to_english(command: str) -> Tuple[str, bool]:
    """
    Translate Roman Urdu command to English.

    Args:
        command: Voice command in Roman Urdu or English

    Returns:
        (translated_command, was_translated) tuple
    """
    command_lower = command.lower().strip()
    was_translated = False

    # Check for exact matches first
    if command_lower in ALL_URDU_COMMANDS:
        translated = ALL_URDU_COMMANDS[command_lower]
        logger.info(f"Exact translation: '{command}' -> '{translated}'")
        return translated, True

    # Check for partial matches and compound commands
    translated_command = command_lower

    # Handle YouTube commands with song names
    # Example: "youtube par coldplay chalao" -> "play coldplay on youtube"
    if "youtube par" in command_lower and ("chalao" in command_lower or "bajao" in command_lower):
        # Extract song name
        song_part = command_lower.replace("youtube par", "").replace("chalao", "").replace("bajao", "").strip()
        translated_command = f"play {song_part} on youtube"
        was_translated = True
        logger.info(f"YouTube translation: '{command}' -> '{translated_command}'")
        return translated_command, was_translated

    # Handle "play X on youtube" variations
    if ("chalao" in command_lower or "bajao" in command_lower) and "youtube" in command_lower:
        song_part = command_lower.replace("youtube", "").replace("chalao", "").replace("bajao", "").replace("par", "").strip()
        translated_command = f"play {song_part} on youtube"
        was_translated = True
        logger.info(f"YouTube play translation: '{command}' -> '{translated_command}'")
        return translated_command, was_translated

    # Handle application opening with app names
    # Example: "chrome kholo" -> "open chrome"
    if "kholo" in command_lower or "chalao" in command_lower:
        app_name = command_lower.replace("kholo", "").replace("chalao", "").strip()
        translated_command = f"open {app_name}"
        was_translated = True
        logger.info(f"Open app translation: '{command}' -> '{translated_command}'")
        return translated_command, was_translated

    # Check for phrase-level matches (longer phrases first)
    sorted_phrases = sorted(ALL_URDU_COMMANDS.items(), key=lambda x: len(x[0]), reverse=True)

    for urdu_phrase, english_phrase in sorted_phrases:
        if urdu_phrase in translated_command:
            translated_command = translated_command.replace(urdu_phrase, english_phrase)
            was_translated = True

    if was_translated:
        logger.info(f"Partial translation: '{command}' -> '{translated_command}'")

    return translated_command, was_translated


def translate_response_to_urdu(english_text: str) -> str:
    """
    Translate English response to Roman Urdu.

    Args:
        english_text: Response text in English

    Returns:
        Translated text in Roman Urdu
    """
    text_lower = english_text.lower()

    # Check for exact matches
    for eng, urdu in RESPONSES_URDU.items():
        if eng == text_lower:
            return urdu

    # Check for partial matches
    translated = english_text
    for eng, urdu in RESPONSES_URDU.items():
        if eng in text_lower:
            translated = translated.replace(eng, urdu)

    return translated


def detect_language(command: str) -> str:
    """
    Detect if command is in English, Roman Urdu, or mixed.

    Args:
        command: Voice command string

    Returns:
        "english", "urdu", or "mixed"
    """
    command_lower = command.lower()

    # Common Urdu indicators
    urdu_indicators = ["kholo", "chalao", "bajao", "banao", "karo", "batao", "hai", "chahiye"]

    urdu_word_count = sum(1 for indicator in urdu_indicators if indicator in command_lower)

    if urdu_word_count >= 2:
        return "urdu"
    elif urdu_word_count == 1:
        return "mixed"
    else:
        return "english"


def get_bilingual_response(english_response: str, urdu_response: Optional[str] = None) -> str:
    """
    Get bilingual response (English + Urdu).

    Args:
        english_response: Response in English
        urdu_response: Optional pre-translated Urdu response

    Returns:
        Bilingual response string
    """
    if urdu_response is None:
        urdu_response = translate_response_to_urdu(english_response)

    if english_response.lower() == urdu_response.lower():
        # No translation available, return English only
        return english_response
    else:
        # Return both
        return f"{english_response} ({urdu_response})"


# ==================== COMMAND PROCESSING ====================

def process_multilingual_command(command: str) -> Tuple[str, Dict[str, str]]:
    """
    Process command in any supported language.

    Args:
        command: Voice command in English, Roman Urdu, or mixed

    Returns:
        (english_command, metadata) tuple
        metadata includes: original_command, language, was_translated
    """
    # Detect language
    language = detect_language(command)

    # Translate if needed
    english_command, was_translated = translate_urdu_to_english(command)

    # Prepare metadata
    metadata = {
        "original_command": command,
        "language": language,
        "was_translated": str(was_translated),
        "english_command": english_command
    }

    logger.info(f"Multilingual processing: {command} -> {english_command} (lang: {language})")

    return english_command, metadata


# ==================== UTILITY FUNCTIONS ====================

def get_supported_languages() -> List[str]:
    """Get list of supported languages"""
    return ["English", "Roman Urdu"]


def get_command_count_by_language() -> Dict[str, int]:
    """Get count of commands by language"""
    return {
        "English": len(ALL_URDU_COMMANDS),  # Can be mapped back
        "Roman Urdu": len(ALL_URDU_COMMANDS),
        "Total Translations": len(ALL_URDU_COMMANDS)
    }


def list_urdu_commands() -> Dict[str, List[str]]:
    """
    Get categorized list of Urdu commands.

    Returns:
        Dictionary of categories with Urdu commands
    """
    return {
        "Greetings": list(GREETINGS_URDU.keys()),
        "Applications": list(APPLICATIONS_URDU.keys()),
        "YouTube & Media": list(YOUTUBE_URDU.keys()),
        "Websites": list(WEBSITES_URDU.keys()),
        "Files & Folders": list(FILES_URDU.keys()),
        "System Info": list(SYSTEM_URDU.keys()),
        "Workflows": list(WORKFLOWS_URDU.keys()),
        "Control": list(CONTROL_URDU.keys()),
    }


def print_urdu_command_reference() -> None:
    """Print comprehensive Urdu command reference"""
    print("\n" + "=" * 70)
    print("GIDEON - ROMAN URDU COMMANDS REFERENCE")
    print("=" * 70)

    categories = list_urdu_commands()

    for category, commands in categories.items():
        print(f"\n{category}:")
        print("-" * 50)
        for cmd in commands:
            english = ALL_URDU_COMMANDS[cmd]
            print(f"  {cmd:30} -> {english}")

    print("\n" + "=" * 70)


# Example usage
if __name__ == "__main__":
    # Test translations
    test_commands = [
        "chrome kholo",
        "youtube par coldplay chalao",
        "time batao",
        "kaam shuru karo",
        "band karo"
    ]

    print("Testing Multi-Language Support:\n")
    for cmd in test_commands:
        english_cmd, metadata = process_multilingual_command(cmd)
        print(f"Input: {cmd}")
        print(f"  -> {english_cmd}")
        print(f"  Language: {metadata['language']}")
        print()

    # Print full command reference
    print_urdu_command_reference()
