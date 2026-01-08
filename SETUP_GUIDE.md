# Gideon Setup & Configuration Guide

**Version 1.0.0 Enhanced**
**Complete Setup Guide for Advanced Features**

This guide covers installation, configuration, and usage of all Gideon features including task scheduling, multi-language support, and workflows.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [First-Time Setup](#first-time-setup)
- [Configuration](#configuration)
- [Advanced Features Setup](#advanced-features-setup)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

---

## Prerequisites

### System Requirements

- **Operating System:** Windows 10/11 (primary support)
- **Python:** 3.8 or higher (3.10+ recommended)
- **RAM:** Minimum 4GB (8GB recommended)
- **Microphone:** Working microphone with proper permissions
- **Internet:** Active internet connection (required for speech recognition)
- **Audio Output:** Speakers or headphones for Gideon's responses

### Hardware Checklist

- [ ] Microphone connected and functioning
- [ ] Speakers/headphones connected
- [ ] Internet connection active
- [ ] Sufficient disk space (100MB minimum)

---

## Installation

### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. **Important:** Check "Add Python to PATH" during installation
3. Verify installation:
   ```bash
   python --version
   ```

### Step 2: Clone/Download Project

```bash
cd "C:\Users\YourName\Desktop\Internship"
cd "Voice-Controlled Repetitive Task Automation"
```

### Step 3: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# You should see (venv) in your command prompt
```

### Step 4: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

**If PyAudio Installation Fails:**

**Option 1: Use pipwin**
```bash
pip install pipwin
pipwin install pyaudio
```

**Option 2: Manual installation**
1. Download appropriate wheel from [Unofficial Windows Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
2. Install: `pip install PyAudio‑0.2.14‑cp310‑cp310‑win_amd64.whl`

### Step 5: Verify Installation

```bash
python test_installation.py
```

Expected output:
```
✓ All dependencies installed successfully!
✓ Microphone access confirmed
✓ Text-to-speech engine ready
```

---

## First-Time Setup

### Initial Configuration

1. **Grant Microphone Permissions:**
   - Windows Settings → Privacy → Microphone
   - Allow apps to access microphone
   - Allow Python and Command Prompt

2. **Test Microphone:**
   ```bash
   # Open Sound settings
   # Settings → System → Sound → Input
   # Speak into microphone and check levels
   ```

3. **Configure TTS (Optional):**

   Edit `config.py`:
   ```python
   TTS_RATE = 175  # Speed (150-200)
   TTS_VOLUME = 0.9  # Volume (0.0-1.0)
   TTS_VOICE_INDEX = 1  # 0: Male, 1: Female
   ```

4. **Set Microphone Sensitivity:**

   Edit `config.py`:
   ```python
   RECOGNITION_ENERGY_THRESHOLD = 4000  # Lower = more sensitive
   RECOGNITION_TIMEOUT = 5  # Seconds to wait for speech
   ```

### First Run

```bash
python gideon.py
```

You should see:
```
╔═══════════════════════════════════════════════════════════╗
║                      GIDEON                               ║
╚═══════════════════════════════════════════════════════════╝

[1/5] Checking microphone access...
✓ Microphone access confirmed

[2/5] Initializing text-to-speech engine...
✓ Text-to-speech engine ready

[3/5] Loading command registry...
✓ Loaded XX command patterns

[4/5] Starting task scheduler...
✓ Task scheduler ready

[5/5] Final system check...
✓ All systems operational

Gideon is now online!
```

**First Command to Try:**
Say: "help" or "what can you do"

---

## Configuration

### Speech Recognition Settings

Edit `config.py` to adjust speech recognition:

```python
# Speech Recognition Settings
RECOGNITION_TIMEOUT = 5  # Seconds to wait for speech (increase for slower speech)
RECOGNITION_PHRASE_LIMIT = 5  # Maximum seconds for a phrase
RECOGNITION_ENERGY_THRESHOLD = 4000  # Microphone sensitivity
RECOGNITION_PAUSE_THRESHOLD = 0.8  # Seconds of silence to consider phrase complete
MAX_RETRY_ATTEMPTS = 3  # Number of retries on recognition failure
```

**Troubleshooting Settings:**

- **Too sensitive (picks up background noise):**
  - Increase `RECOGNITION_ENERGY_THRESHOLD` to 5000-6000

- **Not sensitive enough (doesn't hear you):**
  - Decrease `RECOGNITION_ENERGY_THRESHOLD` to 3000-3500

- **Times out too quickly:**
  - Increase `RECOGNITION_TIMEOUT` to 7-10

- **Cuts off before you finish:**
  - Increase `RECOGNITION_PHRASE_LIMIT` to 7-10

### Text-to-Speech Settings

```python
# Text-to-Speech Configuration
TTS_RATE = 175  # Words per minute (default: 200)
TTS_VOLUME = 0.9  # Volume level (0.0 to 1.0)
TTS_VOICE_INDEX = 1  # Voice index (0: male, 1: female)
```

**Voice Selection:**
```python
# To list available voices on your system:
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name}")
```

### Application Paths

Add custom applications in `config.py`:

```python
APPLICATIONS: Dict[str, str] = {
    # Add your custom applications:
    "spotify": "spotify.exe",
    "discord": "Discord.exe",
    "slack": "slack.exe",
    "pycharm": "pycharm64.exe",
    # ... existing apps ...
}
```

### Website URLs

Add custom websites in `config.py`:

```python
WEBSITES: Dict[str, str] = {
    # Add your custom websites:
    "company portal": "https://portal.yourcompany.com",
    "jira": "https://yourcompany.atlassian.net",
    "confluence": "https://yourcompany.atlassian.net/wiki",
    # ... existing websites ...
}
```

---

## Advanced Features Setup

### Task Scheduling

#### Basic Usage

Schedule tasks to run automatically at specific times:

```python
# Say: "at 9 AM create project folder"
# Say: "at 2 PM take a break"
# Say: "at 5 PM end workday"
```

#### View Scheduled Tasks

```python
# Say: "list scheduled tasks"
# Or: "show scheduled tasks"
```

#### Programmatic Scheduling

Create custom scheduled tasks in your code:

```python
from scheduler import get_scheduler
import commands

# Get scheduler instance
scheduler = get_scheduler()

# Schedule a task
scheduler.schedule_task(
    name="Morning Setup",
    time_str="09:00",  # 24-hour format
    task_func=commands.cmd_start_workday,
    description="Start workday workflow",
    recurring=True  # Runs daily
)
```

#### Persistent Scheduling

Scheduled tasks are automatically saved to:
```
logs/scheduled_tasks.json
```

### Multi-Language Support

#### Enabling Roman Urdu

Roman Urdu is enabled by default! Just speak naturally:

```
English: "open chrome"
Roman Urdu: "chrome kholo"
Both work!
```

#### Adding More Urdu Commands

Edit `multilingual.py` to add custom Urdu commands:

```python
APPLICATIONS_URDU = {
    # Add your custom commands:
    "spotify kholo": "open spotify",
    "discord chalao": "open discord",
    # ... existing commands ...
}
```

#### View Urdu Command Reference

```python
# Say: "show urdu commands"
# Or: "urdu help"
```

### Custom Workflows

Create custom workflows in `workflows.py`:

```python
def custom_project_setup() -> Tuple[bool, str]:
    """
    Custom workflow: Setup project environment
    """
    tasks = [
        ("Opening VS Code", lambda: utils.open_application("vs code")),
        ("Opening GitHub", lambda: utils.open_chrome_with_url("https://github.com")),
        ("Opening project folder", lambda: utils.create_folder("My Project")),
        ("Playing background music", lambda: utils.play_on_youtube("ambient coding music")),
    ]

    workflow = Workflow("project setup", tasks)
    return workflow.execute()

# Register in WORKFLOW_REGISTRY:
WORKFLOW_REGISTRY = {
    # ... existing workflows ...
    "setup project": custom_project_setup,
    "project setup": custom_project_setup,
}
```

Then use it:
```
Say: "setup project"
```

### Confirmation Prompts

Configure which operations require confirmation in `config.py`:

```python
# Safety Settings
DANGEROUS_OPERATIONS = [
    "delete",
    "remove",
    "clean",
    "format",
    "shutdown system",
    "restart system",
]

REQUIRE_CONFIRMATION = True  # Set to False to disable confirmations
```

---

## Troubleshooting

### Common Issues

#### Issue: Microphone Not Working

**Symptoms:**
- "I'm having trouble accessing the microphone"
- No speech detection

**Solutions:**
1. Check microphone connection
2. Grant microphone permissions:
   - Settings → Privacy → Microphone → Allow
3. Close other apps using microphone (Zoom, Discord, etc.)
4. Test microphone in Windows Sound settings
5. Restart Gideon

#### Issue: Speech Recognition Not Accurate

**Symptoms:**
- Commands not recognized
- Frequent "unknown command" errors

**Solutions:**
1. Speak more clearly and slowly
2. Reduce background noise
3. Adjust `RECOGNITION_ENERGY_THRESHOLD` in config
4. Check internet connection (speech recognition requires internet)
5. Move closer to microphone

#### Issue: Gideon Not Speaking

**Symptoms:**
- No audio output from Gideon
- Commands execute but no voice response

**Solutions:**
1. Check speakers/headphones are connected
2. Verify system volume is not muted
3. Test TTS:
   ```python
   python -c "import pyttsx3; e = pyttsx3.init(); e.say('test'); e.runAndWait()"
   ```
4. Try different voice in config: change `TTS_VOICE_INDEX`

#### Issue: Shutdown Command Not Working

**Symptoms:**
- "quit gideon" doesn't exit
- Gideon continues running

**Solutions:**
1. Use full phrase: "quit gideon" (include "gideon")
2. Try alternatives:
   - "exit gideon"
   - "goodbye gideon"
   - "gideon quit"
3. Try simple: "quit" or "exit"
4. Last resort: Press Ctrl+C (but Gideon will ask you to use voice command)

#### Issue: YouTube Videos Not Playing

**Symptoms:**
- "play X on youtube" doesn't work
- Browser doesn't open

**Solutions:**
1. Check internet connection
2. Verify default browser is set
3. Update pywhatkit: `pip install --upgrade pywhatkit`
4. Try exact video name: "play [exact title] on youtube"
5. Check Chrome is installed (preferred for YouTube)

#### Issue: Scheduled Tasks Not Running

**Symptoms:**
- Tasks scheduled but don't execute at specified time

**Solutions:**
1. Keep Gideon running (scheduler runs in background)
2. Check time format: use 24-hour format (e.g., "14:00" not "2 PM")
3. Verify task was scheduled: "list scheduled tasks"
4. Check logs: `logs/gideon_log_*.log`

### Log Files

All activity is logged to timestamped files in the `logs/` directory:

```
logs/
  ├── gideon_log_20260107_143022.log
  ├── gideon_log_20260108_090530.log
  └── scheduled_tasks.json
```

**To view logs:**
```bash
# View latest log
cd logs
notepad gideon_log_YYYYMMDD_HHMMSS.log
```

**Log Levels:**
- **INFO:** Normal operations
- **WARNING:** Non-critical issues
- **ERROR:** Errors that were handled
- **CRITICAL:** System failures

### Getting Help

1. **Say "help"** - Hear available commands
2. **Check logs** - Review `logs/` directory
3. **Read documentation:**
   - `README.md` - Overview and introduction
   - `COMMANDS_ENHANCED.md` - Complete command reference
   - `TROUBLESHOOTING.md` - Detailed troubleshooting
4. **Test installation:**
   ```bash
   python test_installation.py
   ```

---

## Best Practices

### Daily Usage Tips

1. **Start Gideon at Login:**
   - Create shortcut to `gideon.py`
   - Add to Windows Startup folder

2. **Use Workflows:**
   - "start my workday" instead of opening apps individually
   - "take a break" for scheduled breaks

3. **Schedule Recurring Tasks:**
   - "at 9 AM start my workday"
   - "at 12 PM take a break"
   - "at 5 PM end workday"

4. **Speak Naturally:**
   - Gideon understands variations
   - Include "Gideon" for better recognition

5. **Check Console:**
   - Detailed information shown in console
   - Useful for debugging

### Performance Optimization

1. **Close Unused Applications:**
   - Frees system resources
   - Improves recognition speed

2. **Reduce Background Noise:**
   - Better speech recognition accuracy
   - Fewer false positives

3. **Use Wired Microphone:**
   - More reliable than built-in laptop mic
   - Better audio quality

4. **Regular Updates:**
   - Keep Python and packages updated
   - Check for Gideon updates

### Security Best Practices

1. **Review Dangerous Operations:**
   - Gideon asks for confirmation on critical actions
   - Review config for dangerous operation list

2. **Don't Disable Confirmations:**
   - Keep `REQUIRE_CONFIRMATION = True`
   - Prevents accidental deletions

3. **Regular Backups:**
   - Use "end workday" workflow to create backups
   - Schedule automatic backups

4. **Review Logs:**
   - Check logs periodically
   - Identify unusual activity

---

## Testing Your Setup

### Quick Test Checklist

Run these commands to verify everything works:

```
✓ "help" - Should display command list
✓ "what time is it" - Should tell time
✓ "open notepad" - Should open Notepad
✓ "play lofi music on youtube" - Should play music
✓ "create folder test" - Should create folder on Desktop
✓ "list scheduled tasks" - Should show tasks (or "no tasks")
✓ "chrome kholo" (Roman Urdu) - Should open Chrome
✓ "quit gideon" - Should exit gracefully
```

### Performance Benchmarks

Expected response times:
- **Command Recognition:** 1-3 seconds
- **Simple Commands:** < 1 second execution
- **YouTube Commands:** 2-5 seconds (including browser launch)
- **Workflows:** 10-30 seconds (multiple tasks)

---

## Advanced Customization

### Custom Command Patterns

Add custom commands in `commands.py`:

```python
def cmd_my_custom_command() -> Tuple[bool, str]:
    """Custom command handler"""
    utils.speak("Executing custom command")
    # Your custom logic here
    return True, "Custom command executed"

# Add to COMMAND_REGISTRY:
CommandPattern(
    keywords=["my custom command", "custom action"],
    handler=cmd_my_custom_command,
    description="My custom command",
    priority=60
),
```

### Integration with Other Tools

Gideon can integrate with external tools:

```python
# Example: Slack notification
def send_slack_message(message: str):
    # Your Slack integration code
    pass

# Example: Database logging
def log_to_database(action: str):
    # Your database code
    pass
```

---

## Update & Maintenance

### Updating Gideon

```bash
# Activate virtual environment
venv\Scripts\activate

# Update packages
pip install --upgrade -r requirements.txt

# Restart Gideon
python gideon.py
```

### Backing Up Configuration

Backup these files periodically:
```
config.py
workflows.py
multilingual.py
logs/scheduled_tasks.json
```

---

## Support & Resources

### Documentation

- **README.md** - Project overview
- **COMMANDS_ENHANCED.md** - Complete command reference
- **TROUBLESHOOTING.md** - Detailed troubleshooting guide
- **SETUP_GUIDE.md** - This file

### Contact

- **Developer:** Muhammad Ali
- **Organization:** CodeCelix
- **Project:** AI Engineer Internship

---

<div align="center">

**Gideon Setup Complete!**

*You're now ready to use all advanced features*

Say "start my workday" to begin!

</div>
