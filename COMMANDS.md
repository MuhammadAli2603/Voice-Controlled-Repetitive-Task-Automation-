# Gideon - Complete Command Reference

This document contains a comprehensive list of all voice commands supported by Gideon.

## 📚 Table of Contents

- [YouTube Commands](#-youtube-commands-key-feature)
- [Application Commands](#-application-commands)
- [Website Commands](#-website-commands)
- [System Information](#-system-information)
- [File Operations](#-file-operations)
- [Music Commands](#-music-commands)
- [Help & Information](#-help--information)
- [Shutdown Commands](#-shutdown-commands)
- [Greetings & Social](#-greetings--social)
- [Command Aliases](#-command-aliases)

---

## 🎬 YouTube Commands (KEY FEATURE)

| Voice Command | Action | Example Usage | Notes |
|---------------|--------|---------------|-------|
| play [video/song] on youtube | Plays video on YouTube | "play Bohemian Rhapsody on youtube" | Opens browser and plays automatically |
| search [topic] on youtube | Searches and plays on YouTube | "search Python tutorial on youtube" | Plays first result |
| play [artist] on youtube | Plays artist's songs | "play Taylor Swift on youtube" | Good for music |
| youtube play [video] | Plays video on YouTube | "youtube play funny cats" | Alternative syntax |
| play video [name] | Plays video on YouTube | "play video Avengers trailer" | Flexible phrasing |

**Tips**:
- Be specific with video/song names for best results
- Internet connection required
- Opens in default browser
- Plays immediately after opening

---

## 💻 Application Commands

### Office Applications

| Voice Command | Application | Executable | Notes |
|---------------|-------------|------------|-------|
| open notepad | Notepad | notepad.exe | Always available |
| open calculator | Calculator | calc.exe | Windows calculator |
| open paint | MS Paint | mspaint.exe | Image editor |
| open excel | Microsoft Excel | excel.exe | Requires Office |
| open word | Microsoft Word | winword.exe | Requires Office |
| open powerpoint | Microsoft PowerPoint | powerpnt.exe | Requires Office |

### Development Tools

| Voice Command | Application | Executable | Notes |
|---------------|-------------|------------|-------|
| open vs code | Visual Studio Code | code | Requires VS Code installed |
| open visual studio code | Visual Studio Code | code | Alternative phrasing |
| open code | Visual Studio Code | code | Short form |
| open command prompt | Command Prompt | cmd.exe | Windows terminal |
| open cmd | Command Prompt | cmd.exe | Short form |
| open powershell | PowerShell | powershell.exe | Admin rights needed for some commands |

### Web Browsers

| Voice Command | Application | Executable | Notes |
|---------------|-------------|------------|-------|
| open chrome | Google Chrome | chrome.exe | Requires Chrome installed |
| open google chrome | Google Chrome | chrome.exe | Full name |
| open edge | Microsoft Edge | msedge.exe | Built into Windows |
| open firefox | Mozilla Firefox | firefox.exe | Requires Firefox installed |

### System Applications

| Voice Command | Application | Executable | Notes |
|---------------|-------------|------------|-------|
| open file explorer | File Explorer | explorer.exe | Windows file manager |
| open explorer | File Explorer | explorer.exe | Short form |
| open task manager | Task Manager | taskmgr.exe | System monitor |
| open settings | Windows Settings | ms-settings: | Windows 10/11 |
| open control panel | Control Panel | control.exe | Legacy settings |

---

## 🌐 Website Commands

### Search & Email

| Voice Command | Website URL | Notes |
|---------------|-------------|-------|
| open google | https://www.google.com | Search engine |
| open gmail | https://mail.google.com | Google email |
| open mail | https://mail.google.com | Alternative |

### Video & Entertainment

| Voice Command | Website URL | Notes |
|---------------|-------------|-------|
| open youtube | https://www.youtube.com | Video platform |

### Development Resources

| Voice Command | Website URL | Notes |
|---------------|-------------|-------|
| open github | https://github.com | Code hosting |
| open stack overflow | https://stackoverflow.com | Programming Q&A |

### Social Media

| Voice Command | Website URL | Notes |
|---------------|-------------|-------|
| open linkedin | https://www.linkedin.com | Professional network |
| open twitter | https://twitter.com | Social media |
| open facebook | https://www.facebook.com | Social media |
| open reddit | https://www.reddit.com | Discussion forum |

### AI Tools

| Voice Command | Website URL | Notes |
|---------------|-------------|-------|
| open chatgpt | https://chat.openai.com | OpenAI ChatGPT |
| open claude | https://claude.ai | Anthropic Claude |

### Utilities

| Voice Command | Website URL | Notes |
|---------------|-------------|-------|
| open weather | https://weather.com | Weather forecast |
| open news | https://news.google.com | News aggregator |
| open maps | https://maps.google.com | Google Maps |

---

## 🕐 System Information

| Voice Command | Response | Example Output | Notes |
|---------------|----------|----------------|-------|
| what time is it | Current time | "The time is 02:30 PM" | 12-hour format |
| tell me the time | Current time | "The time is 02:30 PM" | Alternative |
| current time | Current time | "The time is 02:30 PM" | Alternative |
| time | Current time | "The time is 02:30 PM" | Short form |
| what date is it | Current date | "Today is January 07, 2026" | Full date |
| tell me the date | Current date | "Today is January 07, 2026" | Alternative |
| current date | Current date | "Today is January 07, 2026" | Alternative |
| date | Current date | "Today is January 07, 2026" | Short form |
| what day is it | Current date | "Today is January 07, 2026" | Alternative |
| today's date | Current date | "Today is January 07, 2026" | Alternative |

---

## 📁 File Operations

| Voice Command | Action | Example | Result |
|---------------|--------|---------|--------|
| create folder [name] | Creates folder on Desktop | "create folder Project Files" | Desktop/Project Files/ |
| make folder [name] | Creates folder on Desktop | "make folder Documents" | Desktop/Documents/ |
| new folder [name] | Creates folder on Desktop | "new folder Photos" | Desktop/Photos/ |
| create dated folder | Creates folder with date | "create dated folder" | Desktop/Folder_2026-01-07/ |
| create folder with date | Creates folder with date | "create folder with date" | Desktop/Folder_2026-01-07/ |
| make today's folder | Creates folder with date | "make today's folder" | Desktop/Folder_2026-01-07/ |
| open music folder | Opens Music folder | "open music folder" | Opens C:\Users\...\Music |

**Notes**:
- Folders created on Desktop by default
- Date format: YYYY-MM-DD
- Folder names can include spaces
- If folder exists, no error (exist_ok=True)

---

## 🎵 Music Commands

| Voice Command | Action | Example | Notes |
|---------------|--------|---------|-------|
| play music | Plays random song from Music folder | "play music" | Requires music files in Music folder |
| play song | Plays random song from Music folder | "play song" | Alternative |
| play some music | Plays random song from Music folder | "play some music" | Alternative |
| open music folder | Opens Music folder | "open music folder" | To add/manage music |

**Supported Audio Formats**:
- MP3 (.mp3)
- WAV (.wav)
- FLAC (.flac)
- M4A (.m4a)
- AAC (.aac)
- OGG (.ogg)
- WMA (.wma)

**Requirements**:
- Music files must be in `C:\Users\[YourName]\Music`
- Default media player will be used

---

## ℹ️ Help & Information

| Voice Command | Response | Action |
|---------------|----------|--------|
| help | Lists available commands | Gideon explains capabilities |
| what can you do | Lists available commands | Alternative |
| list commands | Lists available commands | Alternative |
| show commands | Lists available commands | Alternative |
| available commands | Lists available commands | Alternative |
| your capabilities | Lists available commands | Alternative |
| who are you | Gideon introduces itself | Explains purpose and inspiration |
| what are you | Gideon introduces itself | Alternative |
| introduce yourself | Gideon introduces itself | Alternative |
| tell me a joke | Programming joke | Random joke from collection |
| joke | Programming joke | Short form |
| make me laugh | Programming joke | Alternative |
| say something funny | Programming joke | Alternative |

---

## 🛑 Shutdown Commands

| Voice Command | Action | Notes |
|---------------|--------|-------|
| shutdown gideon | Stops Gideon | Primary shutdown command |
| gideon shutdown | Stops Gideon | Alternative word order |
| exit gideon | Stops Gideon | Alternative |
| gideon exit | Stops Gideon | Alternative |
| quit gideon | Stops Gideon | Alternative |
| gideon quit | Stops Gideon | Alternative |
| stop gideon | Stops Gideon | Alternative |
| gideon stop | Stops Gideon | Alternative |

**Important Notes**:
- These are the ONLY ways to stop Gideon
- Pressing Ctrl+C will NOT stop Gideon (it will ask you to use proper command)
- Gideon will say "Shutting down. Goodbye!" before exiting
- All these commands are case-insensitive

---

## 👋 Greetings & Social

| Voice Command | Response Type | Example Response |
|---------------|---------------|------------------|
| hello | Time-based greeting | "Good morning! How may I assist you?" |
| hi | Time-based greeting | "Good afternoon! How may I assist you?" |
| hey | Time-based greeting | "Good evening! How may I assist you?" |
| good morning | Appropriate greeting | "Good morning! How may I assist you?" |
| good afternoon | Appropriate greeting | "Good afternoon! How may I assist you?" |
| good evening | Appropriate greeting | "Good evening! How may I assist you?" |
| thank you | Polite response | "You're welcome!" / "Happy to help!" |
| thanks | Polite response | "Anytime!" / "My pleasure!" |
| thank you gideon | Polite response | Random friendly response |

**Response Timing**:
- **Morning**: 5:00 AM - 11:59 AM → "Good morning"
- **Afternoon**: 12:00 PM - 4:59 PM → "Good afternoon"
- **Evening**: 5:00 PM - 8:59 PM → "Good evening"
- **Night**: 9:00 PM - 4:59 AM → "Good night"

---

## 🔄 Command Aliases

Gideon understands variations and alternative phrasings. Here are some examples:

### Time Commands
```
"what time is it"
"tell me the time"
"current time"
"time"
```
All of these do the same thing!

### Date Commands
```
"what date is it"
"tell me the date"
"current date"
"date"
"what day is it"
"today's date"
```

### Help Commands
```
"help"
"what can you do"
"list commands"
"show commands"
"available commands"
"your capabilities"
```

### Application Opening
```
"open notepad"    ✓ Standard
"open the notepad" ✗ "the" is removed automatically
```

---

## 📊 Command Priority System

Gideon uses a priority system to match commands:

1. **Priority 100**: Shutdown commands (checked first)
2. **Priority 90**: YouTube commands (key feature)
3. **Priority 80**: Help commands
4. **Priority 60**: Specific app/website commands
5. **Priority 50**: Time, date, file operations
6. **Priority 40**: Greetings, social responses
7. **Priority 30**: Jokes, fun commands
8. **Priority 10**: Generic "open" commands

This ensures important commands like "shutdown" are never missed.

---

## 🎯 Best Practices

### For Best Recognition:

1. **Be Specific**: "play Bohemian Rhapsody on youtube" > "play music"
2. **Use Full Names**: "open visual studio code" > "open vscode"
3. **Speak Clearly**: Normal speaking volume, clear pronunciation
4. **Reduce Noise**: Minimize background sounds
5. **Wait for Response**: Let Gideon finish before next command

### Common Mistakes to Avoid:

❌ **Don't say**: "open the notepad"
✓ **Instead say**: "open notepad"

❌ **Don't say**: "play video of cats on youtube"
✓ **Instead say**: "play cats on youtube"

❌ **Don't say**: "can you open chrome"
✓ **Instead say**: "open chrome"

---

## 🆕 Adding Custom Commands

See [README.md - Adding New Commands](README.md#-adding-new-commands) for detailed instructions.

Quick example:

```python
# In commands.py
CommandPattern(
    keywords=["your command phrase"],
    handler=your_function,
    description="What it does",
    priority=60
)
```

---

## 📞 Support

If a command isn't working:

1. Check this document for correct syntax
2. Verify the application/website is installed/accessible
3. Check logs in `logs/` directory
4. See [README.md - Troubleshooting](README.md#-troubleshooting)

---

<div align="center">

**Total Commands: 75+**

**Command Categories: 9**

**Continuous Operation: ∞**

---

*Last Updated: January 2026*

*Gideon Version: 1.0.0*

</div>
