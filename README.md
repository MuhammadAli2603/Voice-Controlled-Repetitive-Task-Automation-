# Gideon - Voice-Controlled Task Automation System

<div align="center">

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     ██████╗ ██╗██████╗ ███████╗ ██████╗ ███╗   ██╗        ║
║    ██╔════╝ ██║██╔══██╗██╔════╝██╔═══██╗████╗  ██║        ║
║    ██║  ███╗██║██║  ██║█████╗  ██║   ██║██╔██╗ ██║        ║
║    ██║   ██║██║██║  ██║██╔══╝  ██║   ██║██║╚██╗██║        ║
║    ╚██████╔╝██║██████╔╝███████╗╚██████╔╝██║ ╚████║        ║
║     ╚═════╝ ╚═╝╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝        ║
║                                                           ║
║           Voice-Controlled Task Automation System         ║
║                      Version 1.0.0                        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

**Your AI Assistant - Always Ready to Help**

*Named after the intelligent AI from The Flash*

</div>

---

## 📋 Table of Contents

- [About Gideon](#-about-gideon)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Voice Commands](#-voice-commands)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Adding New Commands](#-adding-new-commands)
- [Troubleshooting](#-troubleshooting)
- [Known Limitations](#-known-limitations)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [Developer](#-developer)

---

## 🤖 About Gideon

**Gideon** is an intelligent voice-controlled task automation system designed to simplify daily computing tasks through natural voice commands. Named after the helpful AI from *The Flash*, Gideon is always listening, always ready to assist, and never stops until explicitly told to shut down.

### Key Characteristics:

- **Always Listening**: Runs in an infinite loop, continuously monitoring for voice commands
- **YouTube Master**: Seamlessly plays any video or song on YouTube
- **Intelligent**: Understands natural language and command variations
- **Reliable**: Robust error handling ensures Gideon never crashes
- **Professional**: Clean code, comprehensive logging, and maintainable architecture

### Why Gideon?

This project showcases:
- Advanced voice recognition and natural language processing
- Continuous operation and state management
- Integration with multiple APIs (YouTube, Google Speech Recognition)
- Production-ready error handling and logging
- Modular, extensible architecture

---

## ✨ Features

### Core Capabilities

#### 🎤 Voice Control
- **100% Offline voice recognition** using Vosk (no internet required)
- Natural language understanding with command aliases
- Automatic retry mechanism for failed recognition
- Real-time recognition with low latency
- No dependency on external APIs or services

#### 🔊 Text-to-Speech
- Gideon speaks back to confirm actions
- Configurable voice, rate, and volume
- Friendly, helpful personality

#### 🎬 YouTube Integration (KEY FEATURE)
- Play any video or song on YouTube instantly
- Natural commands: "play [video name] on YouTube"
- Automatic search and playback using `pywhatkit`

#### 🚀 Application Launching
Launch Windows applications with voice:
- Notepad, Calculator, Paint
- Microsoft Office (Word, Excel, PowerPoint)
- VS Code, Chrome, Edge
- File Explorer, Task Manager
- Command Prompt, PowerShell
- And more...

#### 🌐 Website Navigation
Open websites instantly:
- Gmail, YouTube, Google
- GitHub, Stack Overflow
- LinkedIn, Twitter, Facebook
- ChatGPT, Claude AI
- Weather, News, Maps

#### 📁 File Management
- Create folders with custom or date-based names
- Organize files on Desktop
- List and manage files
- Open Music folder

#### 🎵 Music Playback
- Play random music from Music folder
- Support for MP3, WAV, FLAC, M4A, AAC, OGG, WMA

#### 🕐 System Information
- Current time and date
- Time-based greetings
- System status

#### 🛡️ Robust Operation
- Comprehensive error handling
- Automatic recovery from failures
- Detailed logging for debugging
- Never crashes - continues listening even on errors

---

## 🎥 Demo

### Starting Gideon

```bash
python gideon.py
```

### Sample Interaction

```
🗣️  You said: "play Bohemian Rhapsody on youtube"
🤖 Gideon: "Playing Bohemian Rhapsody on YouTube"
✓ Playing 'Bohemian Rhapsody' on YouTube

🗣️  You said: "open notepad"
🤖 Gideon: "Opening Notepad for you"
✓ Opened notepad

🗣️  You said: "what time is it"
🤖 Gideon: "The time is 02:30 PM"
✓ The time is 02:30 PM

🗣️  You said: "shutdown gideon"
🤖 Gideon: "Shutting down. Goodbye!"
```

---

## 📦 Installation

### Prerequisites

- **Python 3.8+** (recommended: Python 3.10+)
- **Windows 10/11** (primary support)
- **Working microphone** with proper permissions
- **~100 MB free disk space** (for Vosk model)
- **Internet connection** (only for initial setup and YouTube - speech recognition works offline!)

### Step-by-Step Installation

#### 1. Clone or Download the Project

```bash
cd "C:\Users\YourName\Desktop\Internship"
cd "Voice-Controlled Repetitive Task Automation"
```

#### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On Linux/Mac:
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
- `vosk` - Offline speech recognition engine
- `sounddevice` - Audio input/output (no DLL issues!)
- `pyttsx3` - Text-to-speech
- `pywhatkit` - YouTube integration
- `schedule` - Task scheduling
- And more...

#### 4. Download Vosk Model (One-Time Setup)

```bash
python vosk_setup.py
```

This interactive wizard will:
- Guide you through model selection
- Download the optimal model for Gideon (40 MB)
- Configure everything automatically
- Verify installation

**Recommended model:** small-en (40 MB, perfect for voice commands)

#### 5. Verify Installation

```bash
# Run comprehensive diagnostics
python audio_handler.py
```

This will check:
- ✅ Vosk installation
- ✅ Model loading
- ✅ Microphone detection
- ✅ Audio levels

**Quick verification:**
```bash
python -c "from audio_handler import get_audio_handler; print('✓ All systems ready!')"
```

---

## 🚀 Quick Start

### Running Gideon

```bash
# Make sure virtual environment is activated
python gideon.py
```

### First Time Setup Checklist

1. ✅ Microphone connected and working
2. ✅ Microphone permissions granted to Python
3. ✅ Vosk model downloaded (run `python vosk_setup.py`)
4. ✅ Speakers/headphones connected for Gideon's responses
5. ✅ No other application using the microphone

**Note:** After initial setup, no internet is required for voice commands!

### Stopping Gideon

Gideon runs in an **infinite loop** and only stops when you say:

```
"shutdown gideon"
"gideon shutdown"
"exit gideon"
"quit gideon"
```

**Important**: Pressing `Ctrl+C` will NOT stop Gideon - it will ask you to use the proper shutdown command.

---

## 💬 Usage

### Basic Usage Pattern

1. **Start Gideon**: Run `python gideon.py`
2. **Wait for greeting**: Gideon will say "Gideon online. How may I assist you?"
3. **Speak your command**: Clearly state what you want
4. **Gideon responds**: Confirms action and executes it
5. **Repeat**: Gideon continues listening for next command
6. **Shutdown**: Say "shutdown gideon" when done

### Tips for Best Results

- **Speak clearly** and at normal volume
- **Use natural language** - Gideon understands variations
- **Wait for Gideon's response** before giving next command
- **Check microphone levels** if Gideon doesn't respond
- **Reduce background noise** for better recognition

### Command Format Examples

```plaintext
✓ "play Imagine Dragons on youtube"
✓ "open notepad"
✓ "what time is it"
✓ "create folder Project Files"
✓ "open gmail"
✓ "tell me a joke"
✓ "help"
✓ "shutdown gideon"
```

---

## 🎙️ Voice Commands

### 📺 YouTube Commands (KEY FEATURE)

| Command | Example |
|---------|---------|
| Play video/song | "play Coldplay on youtube" |
| Search and play | "search Python tutorial on youtube" |
| Play by artist | "play Taylor Swift songs" |
| Play music | "play some music on youtube" |

### 💻 Application Commands

| Command | Opens |
|---------|-------|
| "open notepad" | Notepad |
| "open calculator" | Calculator |
| "open excel" | Microsoft Excel |
| "open word" | Microsoft Word |
| "open powerpoint" | Microsoft PowerPoint |
| "open vs code" | Visual Studio Code |
| "open chrome" | Google Chrome |
| "open edge" | Microsoft Edge |
| "open file explorer" | File Explorer |
| "open task manager" | Task Manager |
| "open settings" | Windows Settings |
| "open command prompt" | Command Prompt |

### 🌐 Website Commands

| Command | Opens |
|---------|-------|
| "open google" | Google.com |
| "open gmail" | Gmail |
| "open youtube" | YouTube |
| "open github" | GitHub |
| "open stack overflow" | Stack Overflow |
| "open linkedin" | LinkedIn |
| "open chatgpt" | ChatGPT |

### 🕐 System Information

| Command | Response |
|---------|----------|
| "what time is it" | Current time |
| "what date is it" | Current date |
| "hello" / "hi" | Time-based greeting |

### 📁 File Operations

| Command | Action |
|---------|--------|
| "create folder [name]" | Creates folder on Desktop |
| "create dated folder" | Creates folder with today's date |
| "open music folder" | Opens Music folder |

### 🎵 Music Commands

| Command | Action |
|---------|--------|
| "play music" | Plays random song from Music folder |
| "play song" | Plays random song from Music folder |

### ℹ️ Information Commands

| Command | Response |
|---------|----------|
| "help" | Lists available commands |
| "who are you" | Gideon introduces itself |
| "tell me a joke" | Programming joke |

### 🛑 Shutdown Commands

| Command | Action |
|---------|--------|
| "shutdown gideon" | Stops Gideon |
| "gideon shutdown" | Stops Gideon |
| "exit gideon" | Stops Gideon |
| "quit gideon" | Stops Gideon |

**See [COMMANDS.md](COMMANDS.md) for complete command reference.**

---

## 📂 Project Structure

```
Voice-Controlled Repetitive Task Automation/
│
├── gideon.py                    # Main entry point - infinite listening loop
├── commands.py                  # Command registry and handlers
├── utils.py                     # Helper functions (speech, file ops, etc.)
├── config.py                    # Configuration and constants
├── audio_handler.py             # Vosk audio handler (offline speech recognition)
├── vosk_setup.py                # Automated Vosk model downloader
├── scheduler.py                 # Task scheduling system
├── multilingual.py              # Roman Urdu translation support
├── workflows.py                 # Multi-task workflow automation
├── requirements.txt             # Python dependencies
│
├── README.md                    # This file
├── COMMANDS.md                  # Basic command reference
├── COMMANDS_ENHANCED.md         # Enhanced commands + scheduling + Urdu
├── SETUP_GUIDE.md               # Detailed setup instructions
├── VOSK_SETUP_GUIDE.md          # Complete Vosk troubleshooting guide
├── VOSK_MIGRATION_STATUS.md     # Migration progress tracking
├── ENHANCEMENTS_SUMMARY.md      # Summary of v1.0 enhancements
├── .gitignore                   # Git ignore rules
│
├── vosk-model-small-en-us-0.15/ # Vosk English model (download via setup)
│
└── logs/                        # Timestamped log files
    ├── gideon_log_20260108_*.log
    └── ...
```

### File Descriptions

**Core System:**
- **`gideon.py`**: Main application with initialization and infinite listening loop
- **`commands.py`**: Enhanced command registry with 44+ patterns and handlers
- **`utils.py`**: Reusable utilities (now using Vosk for speech recognition)
- **`config.py`**: Centralized configuration with Vosk settings
- **`requirements.txt`**: All Python package dependencies (Vosk-based)

**Audio System:**
- **`audio_handler.py`**: Vosk offline speech recognition (600+ lines)
- **`vosk_setup.py`**: Automated model downloader with interactive wizard (450+ lines)

**Advanced Features:**
- **`scheduler.py`**: Background task scheduling system (446 lines)
- **`multilingual.py`**: English ↔ Roman Urdu translation (581 lines, 47+ commands)
- **`workflows.py`**: Multi-task workflow automation with error recovery

**Documentation:**
- **`VOSK_SETUP_GUIDE.md`**: Complete Vosk troubleshooting and optimization guide
- **`COMMANDS_ENHANCED.md`**: All 133 commands including scheduling and Urdu
- **`SETUP_GUIDE.md`**: Detailed setup instructions for all features

---

## ⚙️ How It Works

### Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                     USER SPEAKS                         │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│       Offline Speech Recognition (Vosk)                 │
│         - Captures audio from microphone                │
│         - Converts speech to text (100% offline)        │
│         - No internet required                          │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              Command Processing                         │
│         - Normalize command                             │
│         - Match against command registry                │
│         - Extract parameters                            │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              Execute Command                            │
│         - Open application                              │
│         - Play YouTube video                            │
│         - Create folder                                 │
│         - etc.                                          │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│          Text-to-Speech Response (pyttsx3)              │
│         - Gideon speaks confirmation                    │
│         - Returns to listening                          │
└────────────────┬────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────┐
│              LOOP BACK TO START                         │
│         (Unless shutdown command received)              │
└─────────────────────────────────────────────────────────┘
```

### Main Loop (Simplified)

```python
def main_loop():
    while True:  # Infinite loop
        command = listen_for_command()

        if "shutdown gideon" in command:
            speak("Shutting down. Goodbye!")
            break  # ONLY exit point

        execute_command(command)
        # Continues listening...
```

### Error Handling Strategy

- **Speech Recognition Errors**: Ask user to repeat (up to 3 times)
- **Microphone Errors**: Inform user to check audio settings
- **Network Errors**: Notify user and continue listening
- **Command Errors**: Report error but keep running
- **Unexpected Errors**: Log, report, and continue operation

Gideon **never crashes** - all errors are handled gracefully.

---

## 🔧 Adding New Commands

Gideon's modular design makes adding new commands simple!

### Step 1: Define Command Handler

Add to `commands.py`:

```python
def cmd_open_spotify() -> Tuple[bool, str]:
    """Open Spotify application."""
    success, message = utils.open_application("spotify")
    if success:
        utils.speak("Opening Spotify for you")
    return success, message
```

### Step 2: Register Command Pattern

Add to `COMMAND_REGISTRY` in `commands.py`:

```python
CommandPattern(
    keywords=["open spotify", "play spotify", "start spotify"],
    handler=cmd_open_spotify,
    description="Open Spotify",
    priority=60
),
```

### Step 3: (Optional) Add to Configuration

If it's an application, add to `config.py`:

```python
APPLICATIONS: Dict[str, str] = {
    # ... existing apps ...
    "spotify": "spotify.exe",
}
```

### Step 4: Test

```bash
python gideon.py
# Say: "open spotify"
```

That's it! The new command is now active.

---

## 🔍 Troubleshooting

### 📘 Complete Troubleshooting Guide

For detailed troubleshooting, see **[VOSK_SETUP_GUIDE.md](VOSK_SETUP_GUIDE.md)** which includes:
- Step-by-step diagnostics
- Performance optimization
- Model selection guide
- Multi-language setup
- Advanced configuration

### Quick Fixes

#### Vosk Model Not Found

**Error**: `❌ Vosk model not found`

**Solution**:
```bash
# Run the automated setup wizard
python vosk_setup.py
```

#### Microphone Not Working

**Problem**: Gideon can't access microphone

**Solutions**:
1. Run diagnostics: `python audio_handler.py`
2. Grant microphone permissions to Python/Terminal
3. Close other apps using microphone (Zoom, Discord, etc.)
4. List available devices:
   ```bash
   python -c "from audio_handler import VoskAudioHandler; VoskAudioHandler().list_audio_devices()"
   ```

#### Speech Recognition Inaccurate

**Problem**: Commands not recognized correctly

**Solutions**:
1. **Speak clearly** at normal volume (don't shout or whisper)
2. **Reduce background noise**
3. **Test microphone levels**: `python audio_handler.py`
4. **Adjust sensitivity** in `config.py`:
   ```python
   SILENCE_THRESHOLD = 400.0  # Lower = more sensitive (default: 500)
   ```
5. **Use larger model** for better accuracy:
   ```bash
   python vosk_setup.py --model large-en
   ```

### YouTube Videos Not Playing

**Problem**: "play X on youtube" doesn't work

**Solutions**:
1. Check internet connection
2. Verify default browser is set
3. Update `pywhatkit`: `pip install --upgrade pywhatkit`
4. Try saying: "play [exact video name] on youtube"

### Gideon Not Speaking

**Problem**: No audio output from Gideon

**Solutions**:
1. Check speakers/headphones are connected
2. Verify system volume is not muted
3. Test TTS: `python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('test'); engine.runAndWait()"`
4. Try different voice in `config.py`: change `TTS_VOICE_INDEX`

### Application Not Found

**Problem**: "I couldn't find [app]"

**Solutions**:
1. Verify application is installed
2. Check `config.py` > `APPLICATIONS` for correct executable name
3. For custom apps, add to configuration:
   ```python
   APPLICATIONS = {
       "my app": "myapp.exe",  # Add this line
   }
   ```

### High CPU Usage

**Problem**: Python process using too much CPU

**Solutions**:
1. This is normal during active listening
2. Close other background applications
3. Increase `RECOGNITION_TIMEOUT` in `config.py` for less frequent checks

---

## ⚠️ Known Limitations

### Current Limitations

1. **Windows Only**: Primarily designed for Windows 10/11
   - Some commands (applications) are Windows-specific
   - Cross-platform support requires additional configuration

2. **Internet Required**: Only for these features:
   - YouTube playback
   - Opening web URLs
   - **Speech recognition works 100% offline!** (using Vosk)

3. **Multi-Language Support**: English (primary) + Roman Urdu
   - Additional languages available via Vosk models
   - See [VOSK_SETUP_GUIDE.md](VOSK_SETUP_GUIDE.md) for multi-language setup

4. **Application Paths**: Assumes standard Windows installation paths
   - Custom installations may need configuration updates

5. **Microphone Exclusive**: One application at a time can use microphone
   - Close Zoom, Discord, etc. before running Gideon

### Performance Considerations

- **Model Loading**: Initial startup takes 2-3 seconds to load Vosk model
- **Real-time Recognition**: Fast offline processing with low latency
- **Background Noise**: Affects recognition accuracy (adjustable sensitivity)
- **Model Size**: Small model (40MB) vs Large model (1.8GB) trade-off

---

## 🚀 Future Enhancements

### Planned Features

- [ ] **Multi-language Support**: Hindi, Urdu, Spanish
- [ ] **Custom Wake Words**: "Hey Gideon" activation
- [ ] **Email Integration**: Send predefined emails
- [ ] **Calendar Management**: Add events, set reminders
- [ ] **Weather Information**: Real-time weather updates
- [ ] **Smart Home Integration**: Control IoT devices
- [ ] **Command Workflows**: Execute multiple commands sequentially
- [ ] **Voice Customization**: Choose Gideon's voice
- [ ] **GUI Dashboard**: Visual command history and settings
- [ ] **Mobile App**: Control Gideon remotely
- [ ] **Cloud Sync**: Sync commands across devices
- [ ] **AI Learning**: Learn user preferences over time

### Contributions Welcome!

See [Contributing](#-contributing) section.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Reporting Issues

1. Check existing issues first
2. Create detailed bug report with:
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages/logs
   - System information

### Suggesting Features

1. Open an issue with `[Feature Request]` tag
2. Describe the feature and use case
3. Explain why it would be valuable

### Submitting Code

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Follow code style (PEP 8)
4. Add docstrings and type hints
5. Test thoroughly
6. Commit: `git commit -m "Add amazing feature"`
7. Push: `git push origin feature/amazing-feature`
8. Open Pull Request

### Code Style Guidelines

- Follow PEP 8
- Use type hints
- Write docstrings (Google style)
- Add comments for complex logic
- Keep functions focused and small
- Handle errors gracefully

---

## 👨‍💻 Developer

**Muhammad Ali**


**Project Details**:

- **Timeline**: January 2026
- **Inspiration**: Named after Gideon, the AI from *The Flash*

**Contact**:

- LinkedIn: www.linkedin.com/in/muhammad-ali-903b18235
- Email: muhammadaliaps1234@gmail.com

---

## 📄 License

This project is created for educational purposes as part of an AI Engineer internship at CodeCelix.

---

## 🙏 Acknowledgments

- **The Flash (TV Series)**: Inspiration for Gideon's name and personality
- **CodeCelix**: Internship opportunity and project guidance
- **Python Community**: For excellent libraries and documentation
- **Open Source Contributors**:
  - **Vosk** (Alpha Cephei): Amazing offline speech recognition
  - **pyttsx3**: Reliable text-to-speech engine
  - **pywhatkit**: YouTube integration
  - **sounddevice**: Clean audio I/O without DLL nightmares

---

## 📞 Support

If you encounter issues or have questions:

1. Check [Troubleshooting](#-troubleshooting) section
2. Review [COMMANDS.md](COMMANDS.md) for command syntax
3. Check log files in `logs/` directory
4. Open an issue on GitHub

---

<div align="center">

**Gideon - Always Ready to Assist** 🤖

*Built with by Muhammad Ali*

**Version 1.0.0** | January 2026

</div>
