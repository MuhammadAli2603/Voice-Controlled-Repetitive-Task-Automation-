"""
Gideon Command Registry and Handlers
====================================
All voice command definitions, handlers, and execution logic.
Modular design allows easy addition of new commands.

Author: Muhammad Ali (CodeCelix Internship)
"""

import logging
from typing import Tuple, Optional, Dict, Any, Callable
from datetime import datetime
from pathlib import Path
import random

import config
import utils
import workflows
import scheduler
import multilingual

logger = logging.getLogger("Gideon.Commands")


# ==================== COMMAND HANDLER FUNCTIONS ====================

def cmd_time() -> Tuple[bool, str]:
    """Tell the current time."""
    time_str = utils.get_current_time()
    response = f"The time is {time_str}"
    utils.speak(response)
    return True, response


def cmd_date() -> Tuple[bool, str]:
    """Tell the current date."""
    date_str = utils.get_current_date()
    response = f"Today is {date_str}"
    utils.speak(response)
    return True, response


def cmd_greeting() -> Tuple[bool, str]:
    """Respond to user greetings."""
    greeting = utils.get_time_based_greeting()
    response = f"{greeting}! How may I assist you?"
    utils.speak(response)
    return True, response


def cmd_thank_you() -> Tuple[bool, str]:
    """Respond to thank you messages."""
    responses = [
        "You're welcome!",
        "Happy to help!",
        "Anytime!",
        "My pleasure!",
    ]
    response = random.choice(responses)
    utils.speak(response)
    return True, response


def cmd_help() -> Tuple[bool, str]:
    """
    Display comprehensive help and available commands.
    Speaks key capabilities and displays full help in console.
    """
    # Spoken summary (concise for voice)
    spoken_help = (
        "Here are my main capabilities. "
        "I can open applications like Chrome, Notepad, Excel, and VS Code. "
        "I can play videos on YouTube. "
        "I can open websites like Gmail and Google. "
        "I can create folders and manage files. "
        "I can tell you the time and date. "
        "I can also run workflows like 'start my workday'. "
        "Say 'quit gideon' when you want to exit. "
        "Check the console for a full list of commands."
    )

    # Detailed help (displayed in console)
    detailed_help = """
╔═══════════════════════════════════════════════════════════╗
║                   GIDEON COMMAND REFERENCE                ║
╚═══════════════════════════════════════════════════════════╝

📋 BASIC CONTROLS
  • help / what can you do    - Show this help menu
  • quit gideon / exit gideon  - Exit Gideon (MOST RELIABLE)
  • gideon quit / gideon exit  - Alternative exit commands
  • goodbye gideon            - Polite exit

💻 APPLICATIONS
  • open chrome               - Open Google Chrome
  • open notepad              - Open Notepad
  • open calculator           - Open Calculator
  • open excel                - Open Microsoft Excel
  • open word                 - Open Microsoft Word
  • open vs code              - Open Visual Studio Code
  • open task manager         - Open Task Manager
  • open file explorer        - Open File Explorer

🎬 YOUTUBE & MEDIA (KEY FEATURE!)
  • play [song/video] on youtube  - Play video on YouTube
  • search [topic] on youtube     - Search YouTube
  • play [artist name]            - Play music on YouTube

  Examples:
    "play coldplay on youtube"
    "play despacito"
    "youtube python tutorial"
    "play lofi music"

🌐 WEBSITES
  • open google               - Open Google
  • open gmail                - Open Gmail
  • open github               - Open GitHub
  • open youtube              - Open YouTube
  • open stack overflow       - Open Stack Overflow
  • open linkedin             - Open LinkedIn
  • open chatgpt              - Open ChatGPT

📁 FILES & FOLDERS
  • create folder [name]      - Create new folder on Desktop
  • create dated folder       - Create folder with today's date
  • create project folder     - Create dated project folder
  • clean downloads           - Clean and organize downloads (with confirmation)

⏰ SYSTEM INFORMATION
  • what time is it           - Tell current time
  • what's the date           - Tell current date
  • today's date              - Tell current date

🔄 WORKFLOWS (Multi-Task Automation)
  • start my workday          - Opens Gmail, GitHub, VS Code, Notepad, creates folder
  • start coding session      - Opens VS Code, GitHub, Stack Overflow, plays focus music
  • end workday               - Cleans downloads, organizes files, farewell message
  • start focus mode          - Plays focus music, minimizes distractions
  • prepare for meeting       - Opens Notepad, Gmail, ready message
  • take a break              - Plays relaxing music, health reminders

💬 SOCIAL
  • hello / hi                - Greet Gideon
  • thank you                 - Respond to thanks
  • who are you               - Gideon introduces itself
  • tell me a joke            - Hear a programming joke

🔧 TIPS FOR BEST RESULTS
  • Speak clearly and at normal volume
  • Use "Gideon" in your command for better recognition
  • Say "quit gideon" to exit (most reliable)
  • Reduce background noise for better accuracy
  • Wait for Gideon's response before next command

For more commands and detailed documentation, check:
  - COMMANDS.md - Complete command reference
  - COMMANDS_COMPLETE.md - Extended command list
  - README.md - Full documentation

"""

    # Speak the summary
    utils.speak(spoken_help)

    # Print detailed help to console
    print(detailed_help)

    # Log the help request
    logger.info("Help command executed")

    return True, "Help displayed"


def cmd_open_app(app_name: str) -> Tuple[bool, str]:
    """
    Open an application.

    Args:
        app_name: Name of the application to open
    """
    success, message = utils.open_application(app_name)
    if success:
        utils.speak(config.RESPONSES["opening_app"].format(app=app_name))
    else:
        utils.speak(message)
    return success, message


def cmd_open_website(website_name: str) -> Tuple[bool, str]:
    """
    Open a website.

    Args:
        website_name: Name or URL of the website
    """
    success, message = utils.open_website(website_name)
    if success:
        utils.speak(config.RESPONSES["opening_website"].format(website=website_name))
    else:
        utils.speak(message)
    return success, message


def cmd_youtube(query: str) -> Tuple[bool, str]:
    """
    Play a video on YouTube.

    Args:
        query: Search query for the video
    """
    success, message = utils.play_on_youtube(query)
    if not success:
        utils.speak(message)
    return success, message


def cmd_create_folder(folder_name: str) -> Tuple[bool, str]:
    """
    Create a folder on Desktop.

    Args:
        folder_name: Name of the folder to create
    """
    success, message = utils.create_folder(folder_name)
    if success:
        utils.speak(f"Folder {folder_name} created on your desktop")
    else:
        utils.speak(message)
    return success, message


def cmd_create_dated_folder() -> Tuple[bool, str]:
    """Create a folder with today's date."""
    today = datetime.now().strftime("%Y-%m-%d")
    folder_name = f"Folder_{today}"
    return cmd_create_folder(folder_name)


def cmd_empty_recycle_bin() -> Tuple[bool, str]:
    """Empty the recycle bin (with confirmation)."""
    try:
        # Ask for confirmation
        utils.speak("Are you sure you want to empty the recycle bin? Say yes or no.")

        # Listen for response
        response = utils.listen_for_command(timeout=10)

        if not response:
            utils.speak("No response received. Cancelling for safety.")
            return False, "Operation cancelled - no response"

        response_lower = response.lower().strip()

        # Check for confirmation
        yes_phrases = ["yes", "yeah", "sure", "confirm", "do it", "go ahead", "proceed", "ok", "okay"]

        confirmed = any(phrase in response_lower for phrase in yes_phrases)

        if not confirmed:
            utils.speak("Cancelled.")
            return False, "Operation cancelled by user"

        # Empty recycle bin
        utils.speak("Emptying recycle bin...")
        logger.info("Emptying recycle bin")

        import subprocess
        import os

        # Use PowerShell to empty recycle bin
        result = subprocess.run(
            ["powershell", "-Command", "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0 or result.returncode == 1:  # 1 is also ok (no items)
            message = "Recycle bin emptied successfully"
            utils.speak(message)
            logger.info(message)
            return True, message
        else:
            message = "Failed to empty recycle bin"
            utils.speak(message)
            logger.error(f"Recycle bin error: {result.stderr}")
            return False, message

    except subprocess.TimeoutExpired:
        message = "Recycle bin operation timed out"
        utils.speak(message)
        logger.error(message)
        return False, message
    except Exception as e:
        message = f"Error emptying recycle bin: {str(e)}"
        utils.speak(message)
        logger.error(message, exc_info=True)
        return False, message


def cmd_play_music() -> Tuple[bool, str]:
    """Play a random music file from Music folder."""
    music_files = []
    for ext in config.AUDIO_EXTENSIONS:
        music_files.extend(utils.list_files(config.MUSIC_DIR, ext))

    if not music_files:
        message = "No music files found in your Music folder"
        utils.speak(message)
        return False, message

    # Play random song
    song = random.choice(music_files)
    success, message = utils.play_music_file(song)
    if success:
        utils.speak(f"Playing {song.stem}")
    return success, message


def cmd_open_music_folder() -> Tuple[bool, str]:
    """Open the Music folder."""
    return cmd_open_app("file explorer")


def cmd_who_are_you() -> Tuple[bool, str]:
    """Introduce Gideon."""
    response = (
        f"I am {config.ASSISTANT_NAME}, your voice-controlled task automation assistant. "
        f"I'm here to help you with daily tasks, "
        "opening applications, browsing the web, playing music, and much more. "
        f"I was inspired by the AI from The Flash."
    )
    utils.speak(response)
    return True, response


def cmd_joke() -> Tuple[bool, str]:
    """Tell a programming joke."""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the programmer quit his job? Because he didn't get arrays!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        "What's a programmer's favorite place to hang out? The Foo Bar!",
        "Why do Java developers wear glasses? Because they don't C sharp!",
    ]
    joke = random.choice(jokes)
    utils.speak(joke)
    return True, joke


def cmd_shutdown() -> Tuple[bool, str]:
    """Shutdown Gideon."""
    utils.speak(config.SHUTDOWN_MESSAGE)
    return True, "Shutdown initiated"


# ==================== WORKFLOW COMMANDS ====================
def cmd_workflow(workflow_name: str) -> Tuple[bool, str]:
    """
    Execute a workflow by name.

    Args:
        workflow_name: Name of the workflow to execute
    """
    return workflows.execute_workflow(workflow_name)


def cmd_start_workday() -> Tuple[bool, str]:
    """Start workday workflow."""
    return workflows.start_workday_workflow()


def cmd_start_coding() -> Tuple[bool, str]:
    """Start coding session workflow."""
    return workflows.start_coding_session()


def cmd_end_workday() -> Tuple[bool, str]:
    """End workday workflow."""
    return workflows.end_workday_workflow()


def cmd_focus_mode() -> Tuple[bool, str]:
    """Start focus mode workflow."""
    return workflows.start_focus_mode()


def cmd_meeting_prep() -> Tuple[bool, str]:
    """Prepare for meeting workflow."""
    return workflows.prepare_for_meeting()


def cmd_break() -> Tuple[bool, str]:
    """Start break workflow."""
    return workflows.start_break()


def cmd_clean_downloads() -> Tuple[bool, str]:
    """Clean and organize downloads folder (with confirmation)."""
    return utils.clean_downloads_folder()


# ==================== SCHEDULING COMMANDS ====================
def cmd_list_scheduled_tasks() -> Tuple[bool, str]:
    """List all scheduled tasks."""
    task_scheduler = scheduler.get_scheduler()
    tasks = task_scheduler.list_tasks()

    if not tasks:
        message = "No scheduled tasks"
        utils.speak(message)
        return True, message

    # Speak summary
    count = len(tasks)
    utils.speak(f"You have {count} scheduled task" + ("s" if count > 1 else ""))

    # Display detailed list
    formatted_list = scheduler.format_task_list(tasks)
    print(formatted_list)

    # Speak each task briefly
    for task in tasks[:3]:  # Speak first 3 tasks only
        utils.speak(f"{task['name']} at {task['time']}")

    if count > 3:
        utils.speak(f"And {count - 3} more. Check the console for full list.")

    return True, formatted_list


def cmd_clear_scheduled_tasks() -> Tuple[bool, str]:
    """Clear all scheduled tasks with confirmation."""
    task_scheduler = scheduler.get_scheduler()
    tasks = task_scheduler.list_tasks()

    if not tasks:
        message = "No scheduled tasks to clear"
        utils.speak(message)
        return True, message

    # Ask for confirmation
    count = len(tasks)
    if utils.ask_confirmation(f"clear {count} scheduled task" + ("s" if count > 1 else "")):
        return task_scheduler.clear_all_tasks()
    else:
        message = "Cancelled"
        utils.speak(message)
        return False, message


# ==================== MULTILINGUAL COMMANDS ====================
def cmd_show_urdu_commands() -> Tuple[bool, str]:
    """Show Roman Urdu command reference."""
    utils.speak("Showing Roman Urdu commands in the console")

    # Print to console
    multilingual.print_urdu_command_reference()

    # Speak some examples
    utils.speak("You can say: chrome kholo, gaana chalao, time batao, kaam shuru karo")

    return True, "Urdu commands displayed"


def cmd_language_info() -> Tuple[bool, str]:
    """Show supported languages information."""
    languages = multilingual.get_supported_languages()
    command_counts = multilingual.get_command_count_by_language()

    message = f"I support {len(languages)} languages: {', '.join(languages)}"
    utils.speak(message)

    # Print detailed stats
    print("\n" + "=" * 60)
    print("LANGUAGE SUPPORT:")
    print("-" * 60)
    for lang, count in command_counts.items():
        print(f"{lang}: {count} commands")
    print("=" * 60)

    return True, message


# ==================== COMMAND PATTERNS ====================

class CommandPattern:
    """
    Represents a command pattern with matching logic.
    """

    def __init__(
        self,
        keywords: list[str],
        handler: Callable,
        description: str,
        requires_param: bool = False,
        param_extractor: Optional[Callable[[str], Optional[str]]] = None,
        priority: int = 0
    ):
        """
        Initialize a command pattern.

        Args:
            keywords: List of keywords/phrases that trigger this command
            handler: Function to execute when command matches
            description: Human-readable description of the command
            requires_param: Whether this command needs a parameter
            param_extractor: Function to extract parameter from command
            priority: Higher priority commands are checked first (default: 0)
        """
        self.keywords = [k.lower() for k in keywords]
        self.handler = handler
        self.description = description
        self.requires_param = requires_param
        self.param_extractor = param_extractor
        self.priority = priority

    def matches(self, command: str) -> bool:
        """
        Check if command matches this pattern using fuzzy matching.
        Handles common speech recognition errors.
        """
        command_lower = command.lower().strip()

        # Exact substring match (original behavior)
        for keyword in self.keywords:
            if keyword in command_lower:
                return True

        # Fuzzy matching for single-word commands (e.g., "chrome" vs "cron")
        command_words = command_lower.split()
        for keyword in self.keywords:
            keyword_words = keyword.split()

            # For single-word keywords, use fuzzy matching
            if len(keyword_words) == 1 and len(command_words) > 0:
                keyword_word = keyword_words[0]
                for cmd_word in command_words:
                    # Check if words are similar (allow 1-2 character difference)
                    if self._is_similar(keyword_word, cmd_word):
                        return True

            # For multi-word keywords, check if most words match
            elif len(keyword_words) > 1:
                matches = sum(1 for kw in keyword_words if any(self._is_similar(kw, cw) for cw in command_words))
                # If at least 70% of words match, consider it a match
                if matches >= len(keyword_words) * 0.7:
                    return True

        return False

    def _is_similar(self, word1: str, word2: str) -> bool:
        """Check if two words are similar using simple edit distance."""
        # Exact match
        if word1 == word2:
            return True

        # Length difference check (avoid comparing very different lengths)
        if abs(len(word1) - len(word2)) > 2:
            return False

        # Calculate simple Levenshtein distance
        distance = self._levenshtein_distance(word1, word2)
        max_distance = max(2, len(word1) // 3)  # Allow up to 2 edits or 33% of word length

        return distance <= max_distance

    def _levenshtein_distance(self, s1: str, s2: str) -> int:
        """Calculate Levenshtein distance between two strings."""
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                # Cost of insertions, deletions, or substitutions
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def extract_param(self, command: str) -> Optional[str]:
        """Extract parameter from command if needed."""
        if not self.requires_param:
            return None

        if self.param_extractor:
            return self.param_extractor(command)

        return None


# ==================== PARAMETER EXTRACTORS ====================

def extract_app_name(command: str) -> Optional[str]:
    """Extract application name from 'open X' command."""
    command_lower = command.lower()

    # Try "open X"
    if "open" in command_lower:
        parts = command_lower.split("open", 1)
        if len(parts) > 1:
            app_name = parts[1].strip()
            # Remove common filler words
            app_name = app_name.replace("the", "").strip()
            return app_name

    return None


def extract_website_name(command: str) -> Optional[str]:
    """Extract website name from command."""
    command_lower = command.lower()

    # Patterns: "open website X", "go to X", "browse X"
    patterns = ["open website ", "go to ", "browse ", "open "]

    for pattern in patterns:
        if pattern in command_lower:
            parts = command_lower.split(pattern, 1)
            if len(parts) > 1:
                website = parts[1].strip()
                website = website.replace("website", "").strip()
                return website

    return None


def extract_folder_name(command: str) -> Optional[str]:
    """
    Extract folder name from various folder creation command patterns.
    Handles: 'create folder X', 'create a folder named X', 'create folder on desktop named X'
    """
    command_lower = command.lower().strip()

    # Remove common filler words
    command_clean = command_lower.replace(" a ", " ").replace(" the ", " ")

    # Pattern 1: "create folder named X" or "make folder named X"
    named_patterns = [
        r"named\s+(.+)",
        r"called\s+(.+)",
    ]

    import re
    for pattern in named_patterns:
        match = re.search(pattern, command_clean)
        if match:
            folder_name = match.group(1).strip()
            # Remove trailing words like "on desktop", "on the desktop"
            folder_name = re.sub(r'\s+on\s+(desktop|the\s+desktop).*$', '', folder_name)
            if folder_name:
                return folder_name

    # Pattern 2: "create folder X" (simple pattern)
    simple_patterns = ["create folder ", "make folder ", "new folder "]

    for pattern in simple_patterns:
        if pattern in command_clean:
            parts = command_clean.split(pattern, 1)
            if len(parts) > 1:
                folder_name = parts[1].strip()
                # Remove trailing words
                folder_name = re.sub(r'\s+on\s+(desktop|the\s+desktop).*$', '', folder_name)
                # Remove "named" prefix if present
                folder_name = re.sub(r'^named\s+', '', folder_name)
                if folder_name and folder_name not in ['on', 'the', 'desktop', 'a']:
                    return folder_name

    return None


# ==================== COMMAND REGISTRY ====================

COMMAND_REGISTRY: list[CommandPattern] = [
    # ===== HIGH PRIORITY COMMANDS =====
    # Shutdown (highest priority)
    CommandPattern(
        keywords=config.SHUTDOWN_TRIGGERS,
        handler=cmd_shutdown,
        description="Shutdown Gideon",
        priority=100
    ),

    # YouTube commands (high priority - key feature)
    CommandPattern(
        keywords=[
            "play on youtube",
            "search on youtube",
            "youtube play",
            "play video",
            "youtube",
            "play",
            "search youtube",
            "play on yt",
            "open youtube",
            "search on yt"
        ],
        handler=cmd_youtube,
        description="Play video on YouTube",
        requires_param=True,
        param_extractor=utils.extract_youtube_query,
        priority=90
    ),

    # ===== WORKFLOWS (Multi-task automation) =====
    CommandPattern(
        keywords=["start my workday", "start workday", "begin workday", "workday start"],
        handler=cmd_start_workday,
        description="Start workday workflow (opens apps, creates folder)",
        priority=85
    ),

    CommandPattern(
        keywords=["start coding", "start coding session", "begin coding", "setup coding"],
        handler=cmd_start_coding,
        description="Start coding session workflow",
        priority=85
    ),

    CommandPattern(
        keywords=["end workday", "finish workday", "end my workday", "wrap up work"],
        handler=cmd_end_workday,
        description="End workday workflow",
        priority=85
    ),

    CommandPattern(
        keywords=["start focus mode", "focus mode", "deep focus", "enter focus"],
        handler=cmd_focus_mode,
        description="Start focus mode workflow",
        priority=85
    ),

    CommandPattern(
        keywords=["prepare for meeting", "meeting prep", "ready for meeting", "setup meeting"],
        handler=cmd_meeting_prep,
        description="Prepare for meeting workflow",
        priority=85
    ),

    CommandPattern(
        keywords=["take a break", "start break", "break time", "need a break"],
        handler=cmd_break,
        description="Start break workflow",
        priority=85
    ),

    # ===== SYSTEM INFORMATION =====
    CommandPattern(
        keywords=["what time is it", "tell me the time", "current time", "time"],
        handler=cmd_time,
        description="Tell current time",
        priority=50
    ),

    CommandPattern(
        keywords=["what date is it", "tell me the date", "current date", "date", "what day"],
        handler=cmd_date,
        description="Tell current date",
        priority=50
    ),

    # ===== GREETINGS & SOCIAL =====
    CommandPattern(
        keywords=["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
        handler=cmd_greeting,
        description="Respond to greetings",
        priority=40
    ),

    CommandPattern(
        keywords=["thank you", "thanks", "thank you gideon"],
        handler=cmd_thank_you,
        description="Respond to thanks",
        priority=40
    ),

    # ===== HELP & INFO =====
    CommandPattern(
        keywords=["help", "what can you do", "list commands", "your capabilities"],
        handler=cmd_help,
        description="List available commands",
        priority=80
    ),

    CommandPattern(
        keywords=["who are you", "what are you", "introduce yourself"],
        handler=cmd_who_are_you,
        description="Introduce Gideon",
        priority=40
    ),

    CommandPattern(
        keywords=["tell me a joke", "joke", "make me laugh", "say something funny"],
        handler=cmd_joke,
        description="Tell a joke",
        priority=30
    ),

    # ===== APPLICATION COMMANDS =====
    CommandPattern(
        keywords=["open notepad", "notepad", "launch notepad", "start notepad"],
        handler=lambda: cmd_open_app("notepad"),
        description="Open Notepad",
        priority=60
    ),

    CommandPattern(
        keywords=["open calculator", "calculator", "calc", "open calc", "launch calculator"],
        handler=lambda: cmd_open_app("calculator"),
        description="Open Calculator",
        priority=60
    ),

    CommandPattern(
        keywords=["open excel"],
        handler=lambda: cmd_open_app("excel"),
        description="Open Excel",
        priority=60
    ),

    CommandPattern(
        keywords=["open word"],
        handler=lambda: cmd_open_app("word"),
        description="Open Word",
        priority=60
    ),

    CommandPattern(
        keywords=["open powerpoint"],
        handler=lambda: cmd_open_app("powerpoint"),
        description="Open PowerPoint",
        priority=60
    ),

    CommandPattern(
        keywords=["open vs code", "open visual studio code", "open code"],
        handler=lambda: cmd_open_app("vs code"),
        description="Open VS Code",
        priority=60
    ),

    CommandPattern(
        keywords=["open chrome", "open google chrome", "chrome", "launch chrome", "start chrome", "google chrome"],
        handler=lambda: cmd_open_app("chrome"),
        description="Open Chrome",
        priority=60
    ),

    CommandPattern(
        keywords=["open edge"],
        handler=lambda: cmd_open_app("edge"),
        description="Open Edge",
        priority=60
    ),

    CommandPattern(
        keywords=["open file explorer", "open explorer"],
        handler=lambda: cmd_open_app("file explorer"),
        description="Open File Explorer",
        priority=60
    ),

    CommandPattern(
        keywords=["open task manager"],
        handler=lambda: cmd_open_app("task manager"),
        description="Open Task Manager",
        priority=60
    ),

    CommandPattern(
        keywords=["open settings"],
        handler=lambda: cmd_open_app("settings"),
        description="Open Windows Settings",
        priority=60
    ),

    CommandPattern(
        keywords=["open command prompt", "open cmd"],
        handler=lambda: cmd_open_app("command prompt"),
        description="Open Command Prompt",
        priority=60
    ),

    # ===== WEBSITE COMMANDS =====
    CommandPattern(
        keywords=["open google"],
        handler=lambda: cmd_open_website("google"),
        description="Open Google",
        priority=60
    ),

    CommandPattern(
        keywords=["open gmail", "open mail"],
        handler=lambda: cmd_open_website("gmail"),
        description="Open Gmail",
        priority=60
    ),

    CommandPattern(
        keywords=["open youtube"],
        handler=lambda: cmd_open_website("youtube"),
        description="Open YouTube",
        priority=60
    ),

    CommandPattern(
        keywords=["open github"],
        handler=lambda: cmd_open_website("github"),
        description="Open GitHub",
        priority=60
    ),

    CommandPattern(
        keywords=["open stack overflow"],
        handler=lambda: cmd_open_website("stack overflow"),
        description="Open Stack Overflow",
        priority=60
    ),

    CommandPattern(
        keywords=["open linkedin"],
        handler=lambda: cmd_open_website("linkedin"),
        description="Open LinkedIn",
        priority=60
    ),

    CommandPattern(
        keywords=["open chatgpt"],
        handler=lambda: cmd_open_website("chatgpt"),
        description="Open ChatGPT",
        priority=60
    ),

    # ===== FILE OPERATIONS =====
    CommandPattern(
        keywords=["create folder", "make folder", "new folder"],
        handler=cmd_create_folder,
        description="Create a folder",
        requires_param=True,
        param_extractor=extract_folder_name,
        priority=50
    ),

    CommandPattern(
        keywords=["create dated folder", "create folder with date", "make today's folder"],
        handler=cmd_create_dated_folder,
        description="Create folder with today's date",
        priority=50
    ),

    CommandPattern(
        keywords=["clean downloads", "organize downloads", "clean download folder", "organize download folder"],
        handler=cmd_clean_downloads,
        description="Clean and organize downloads folder (with confirmation)",
        priority=50
    ),

    CommandPattern(
        keywords=["empty recycle bin", "clean recycle bin", "clear recycle bin", "empty trash", "clean trash", "clear trash", "clean up recycle bin", "clean up recyclebin"],
        handler=cmd_empty_recycle_bin,
        description="Empty recycle bin (with confirmation)",
        priority=50
    ),

    # ===== SCHEDULING COMMANDS =====
    CommandPattern(
        keywords=["list scheduled tasks", "show scheduled tasks", "scheduled tasks", "list tasks"],
        handler=cmd_list_scheduled_tasks,
        description="List all scheduled tasks",
        priority=60
    ),

    CommandPattern(
        keywords=["clear scheduled tasks", "remove scheduled tasks", "delete scheduled tasks", "clear tasks"],
        handler=cmd_clear_scheduled_tasks,
        description="Clear all scheduled tasks (with confirmation)",
        priority=60
    ),

    # ===== MULTILINGUAL COMMANDS =====
    CommandPattern(
        keywords=["show urdu commands", "urdu commands", "roman urdu", "urdu help"],
        handler=cmd_show_urdu_commands,
        description="Show Roman Urdu command reference",
        priority=50
    ),

    CommandPattern(
        keywords=["language support", "supported languages", "which languages", "language info"],
        handler=cmd_language_info,
        description="Show supported languages",
        priority=50
    ),

    # ===== MUSIC =====
    CommandPattern(
        keywords=["play music", "play song", "play some music"],
        handler=cmd_play_music,
        description="Play random music from Music folder",
        priority=50
    ),

    CommandPattern(
        keywords=["open music folder"],
        handler=cmd_open_music_folder,
        description="Open Music folder",
        priority=50
    ),

    # ===== GENERIC OPEN COMMANDS (Lower priority) =====
    CommandPattern(
        keywords=["open"],
        handler=cmd_open_app,
        description="Open an application (generic)",
        requires_param=True,
        param_extractor=extract_app_name,
        priority=10
    ),
]

# Sort commands by priority (highest first)
COMMAND_REGISTRY.sort(key=lambda x: x.priority, reverse=True)


# ==================== COMMAND EXECUTION ====================

def execute_command(command: str) -> Tuple[bool, str]:
    """
    Execute a voice command by matching it against the command registry.

    Args:
        command: The voice command to execute

    Returns:
        (success: bool, message: str) tuple
    """
    if not command or command.strip() == "":
        return False, "Empty command"

    # Normalize command
    normalized_command = utils.normalize_command(command)

    # Strip wake words from the beginning of the command
    # This prevents "gideon create folder" from matching "gideon quit"
    for wake_word in config.WAKE_WORDS:
        if normalized_command.startswith(wake_word + " "):
            normalized_command = normalized_command[len(wake_word):].strip()
            logger.debug(f"Stripped wake word '{wake_word}' from command")
            break

    logger.info(f"🎤 RAW COMMAND: '{command}'")
    logger.info(f"📝 NORMALIZED: '{normalized_command}'")
    print(f"\n🔍 Searching for match: '{command}'")

    # Try to match against registered commands
    for pattern in COMMAND_REGISTRY:
        if pattern.matches(normalized_command):
            logger.info(f"✓ MATCHED: {pattern.description} (keywords: {pattern.keywords})")
            print(f"✓ Matched: {pattern.description}")
            try:
                # Extract parameter if needed
                if pattern.requires_param:
                    param = pattern.extract_param(command)
                    if param:
                        return pattern.handler(param)
                    else:
                        message = "I couldn't understand the full command"
                        utils.speak(message)
                        return False, message
                else:
                    return pattern.handler()

            except Exception as e:
                error_msg = utils.handle_error(e, f"Command execution: {command}")
                utils.speak(error_msg)
                return False, error_msg

    # No matching command found
    logger.warning(f"Unknown command: {command}")
    utils.speak(config.RESPONSES["unknown_command"])
    return False, "Unknown command"


def get_all_commands() -> list[Dict[str, Any]]:
    """
    Get list of all available commands for documentation.

    Returns:
        List of command dictionaries with description and keywords
    """
    commands = []
    for pattern in COMMAND_REGISTRY:
        commands.append({
            "keywords": pattern.keywords,
            "description": pattern.description,
            "requires_param": pattern.requires_param
        })
    return commands
