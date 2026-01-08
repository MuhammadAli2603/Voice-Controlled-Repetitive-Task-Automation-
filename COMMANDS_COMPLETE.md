# Gideon Voice Commands - Complete Reference
## All Available Commands with Examples

---

## 📋 BASIC CONTROLS

| Command | Action | Priority |
|---------|--------|----------|
| **help** | Show comprehensive help menu | High |
| **what can you do** | Show capabilities | High |
| **quit gideon** | Exit Gideon (RECOMMENDED) | Highest |
| **exit gideon** | Exit Gideon | Highest |
| **goodbye gideon** | Exit Gideon | Highest |
| **quit / exit / goodbye** | Simple exit commands | Highest |

**Examples:**
```
"Hey Gideon, help"
"What can you do?"
"Quit Gideon"  ← Most reliable
```

---

## 🎬 YOUTUBE & MEDIA (KEY FEATURE)

| Command Pattern | Example |
|----------------|---------|
| **play [name] on youtube** | "play coldplay on youtube" |
| **youtube [name]** | "youtube despacito" |
| **search [name] on youtube** | "search python tutorial on youtube" |
| **play [name]** | "play avengers trailer" |

**Supported Variations:**
- "play on youtube"
- "search on youtube"
- "youtube play"
- "play video"
- "youtube"
- "play"
- "search youtube"
- "play on yt"
- "open youtube"
- "search on yt"

**Examples:**
```
"Play Coldplay on YouTube"
"YouTube Despacito"
"Play some lo-fi music"
"Search Python tutorial on YouTube"
```

**Priority:** 90 (Very High)

---

## 🚀 WORKFLOWS (Multi-Task Automation)

### **Start Workday**
**Commands:** "start my workday", "start workday", "begin workday"

**What It Does:**
1. Creates today's work folder (Work_YYYY-MM-DD)
2. Opens Gmail in Chrome
3. Opens GitHub
4. Opens VS Code
5. Opens Notepad for quick notes
6. Gives time-based greeting

**Example:**
```
"Start my workday"
→ Creates folder: Work_2026-01-07
→ Opens Gmail, GitHub, VS Code, Notepad
→ "Good morning! Ready to start your productive day!"
```

---

### **Start Coding Session**
**Commands:** "start coding", "start coding session", "begin coding"

**What It Does:**
1. Opens VS Code
2. Opens GitHub
3. Opens Stack Overflow
4. Opens ChatGPT
5. Plays lo-fi focus music on YouTube
6. Motivational message

**Example:**
```
"Start coding session"
→ Opens all dev tools
→ Plays focus music
→ "Coding environment ready. Happy coding!"
```

---

### **End Workday**
**Commands:** "end workday", "finish workday", "wrap up work"

**What It Does:**
1. Creates backup folder with timestamp
2. Organizes workspace
3. Farewell message

**Example:**
```
"End workday"
→ Creates Backup_2026-01-07_1845
→ "Great work today! Have a wonderful evening!"
```

---

### **Focus Mode**
**Commands:** "start focus mode", "focus mode", "deep focus"

**What It Does:**
1. Plays 2-hour deep focus music
2. Opens VS Code
3. Focus message

**Example:**
```
"Focus mode"
→ Plays focus music
→ "Focus mode activated. You've got this!"
```

---

### **Meeting Preparation**
**Commands:** "prepare for meeting", "meeting prep", "ready for meeting"

**What It Does:**
1. Opens Notepad for meeting notes
2. Opens Gmail
3. Ready message

**Example:**
```
"Prepare for meeting"
→ "Meeting preparation complete. Good luck!"
```

---

### **Break Time**
**Commands:** "take a break", "start break", "break time"

**What It Does:**
1. Plays relaxing piano music
2. Health reminders (stretch, hydrate, breathe)

**Example:**
```
"Take a break"
→ Plays relaxing music
→ "Stand up and stretch. Hydrate yourself. You deserve this break!"
```

**Workflow Priority:** 85 (High)

---

## 💻 APPLICATIONS

| Command | Opens | Priority |
|---------|-------|----------|
| **open chrome** | Google Chrome | 60 |
| **open notepad** | Notepad | 60 |
| **open calculator** | Calculator | 60 |
| **open excel** | Microsoft Excel | 60 |
| **open word** | Microsoft Word | 60 |
| **open vs code** | Visual Studio Code | 60 |
| **open file explorer** | File Explorer | 60 |
| **open command prompt** | Command Prompt | 60 |

**Examples:**
```
"Open Chrome"
"Open VS Code"
"Open Calculator"
```

---

## 🌐 WEBSITES

| Command | Opens | Priority |
|---------|-------|----------|
| **open google** | Google.com | 60 |
| **open gmail** | Gmail | 60 |
| **open github** | GitHub | 60 |
| **open youtube** | YouTube | 60 |
| **open stackoverflow** | Stack Overflow | 60 |
| **open linkedin** | LinkedIn | 60 |
| **open chatgpt** | ChatGPT | 60 |

**Examples:**
```
"Open Gmail"
"Open GitHub"
"Open ChatGPT"
```

---

## 📁 FILES & FOLDERS

| Command | Action | Confirmation? | Priority |
|---------|--------|---------------|----------|
| **create folder [name]** | Creates folder on Desktop | No | 50 |
| **create dated folder** | Creates folder with today's date | No | 50 |
| **clean downloads** | Organizes downloads by type | ✅ YES | 50 |

**Examples:**
```
"Create folder ProjectX"
→ Creates folder on Desktop

"Create dated folder"
→ Creates Work_2026-01-07

"Clean downloads"
→ Asks: "Are you sure?"
→ Say "yes" to confirm
→ Organizes files into Documents, Images, Videos, etc.
```

**Download Organization Categories:**
- Documents: .pdf, .doc, .docx, .txt, .xlsx, .pptx
- Images: .jpg, .jpeg, .png, .gif, .bmp, .svg
- Videos: .mp4, .avi, .mkv, .mov, .wmv
- Archives: .zip, .rar, .7z, .tar, .gz
- Installers: .exe, .msi, .dmg
- Others: Everything else

---

## ⏰ SYSTEM INFORMATION

| Command | Response | Priority |
|---------|----------|----------|
| **what time is it** | Current time | 50 |
| **what's the date** | Current date | 50 |
| **what day is it** | Current date | 50 |
| **tell me the time** | Current time | 50 |

**Examples:**
```
"What time is it?"
→ "The time is 2:45 PM"

"What's the date?"
→ "Today is Tuesday, January 7th, 2026"
```

---

## 💬 SOCIAL & FUN

| Command | Response | Priority |
|---------|----------|----------|
| **hello / hi** | Greets back | 40 |
| **how are you** | Friendly response | 40 |
| **thank you** | "You're welcome!" | 40 |
| **tell me a joke** | Programming joke | 30 |

**Examples:**
```
"Hello Gideon"
→ "Good morning! How may I assist you?"

"Thank you"
→ "Happy to help!"

"Tell me a joke"
→ "Why do programmers prefer dark mode? Because light attracts bugs!"
```

---

## 🔒 CONFIRMATION PROMPTS

Commands that require confirmation for safety:

### **Clean Downloads**
```
You: "Clean downloads"
Gideon: "Are you sure you want to organize your downloads folder? Say yes or no."
You: "Yes"
Gideon: "Confirmed. Proceeding."
→ Organizes files
Gideon: "Done! Organized 25 files."
```

**Confirmation Responses:**
- **Yes:** yes, yeah, sure, confirm, do it, go ahead, proceed, ok, okay, affirmative
- **No:** no, nope, cancel, don't, stop, nevermind, never mind, negative
- **No Response:** Auto-cancels after 10 seconds for safety

---

## 🎯 COMMAND PRIORITY SYSTEM

Gideon uses priority-based command matching:

| Priority | Command Type | Examples |
|----------|-------------|----------|
| **100** | Shutdown | quit, exit, goodbye |
| **90** | YouTube | play on youtube |
| **85** | Workflows | start workday |
| **80** | Help | help, what can you do |
| **60** | Apps/Websites | open chrome, open gmail |
| **50** | System/Files | time, date, create folder |
| **40** | Social | hello, thank you |
| **30** | Fun | tell me a joke |
| **10** | Generic | open [anything] |

Higher priority commands are matched first.

---

## 💡 TIPS FOR BEST RESULTS

### **1. Speak Clearly**
- Use natural pace
- Enunciate words clearly
- Reduce background noise

### **2. Use "Gideon" in Commands**
```
✅ "Gideon, open Chrome"
✅ "Hey Gideon, what time is it?"
✅ "Quit Gideon"
```

### **3. Wait for Confirmation**
- Gideon speaks after each action
- Wait for "Listening for commands..." before next command

### **4. For Reliable Exit**
```
✅ BEST: "quit gideon"
✅ GOOD: "exit gideon"
✅ GOOD: "goodbye gideon"
⚠️  OK: "quit" (works but less specific)
```

### **5. Workflow Commands**
- Workflows run multiple tasks
- Wait for "All tasks finished" message
- Check console for detailed progress

### **6. Confirmation Commands**
- Say "yes" or "no" clearly
- Don't say "maybe" or "I think so"
- Timeout = 10 seconds (auto-cancel)

---

## 🔍 COMMAND EXAMPLES BY CATEGORY

### **Quick Daily Tasks**
```
"What time is it?"
"Open Gmail"
"Play some music on YouTube"
"Create folder Meeting Notes"
```

### **Start Your Day**
```
"Start my workday"
→ Sets up complete workspace in 30 seconds
```

### **Productive Coding**
```
"Start coding session"
→ Opens all dev tools + focus music
```

### **Safe File Management**
```
"Clean downloads"
Gideon: "Are you sure?"
"Yes"
→ Organizes everything automatically
```

### **Take Care of Yourself**
```
"Take a break"
→ Relaxing music + health reminders
```

### **End of Day**
```
"End workday"
→ Backs up files, farewell message
```

---

## 🚨 TROUBLESHOOTING

### **Command Not Recognized?**
1. Check if command is in this list
2. Speak more clearly
3. Say "help" to see available commands
4. Try adding "Gideon" before the command

### **Gideon Not Responding?**
1. Check microphone is working
2. Check internet connection (needed for speech recognition)
3. Look for "Listening for commands..." message

### **Want to Exit?**
- **BEST WAY:** Say "quit gideon" (most reliable)
- Alternative: Ctrl+C in terminal

### **Workflow Not Working?**
1. Check if apps are installed (Chrome, VS Code, etc.)
2. Check internet for YouTube features
3. Watch console for error messages

---

## 📊 COMMAND STATISTICS

**Total Commands:** 75+
**Workflows:** 6
**Applications:** 15+
**Websites:** 15+
**File Operations:** 3
**With Confirmation:** 1 (clean downloads)

---

## 🎓 ADVANCED USAGE

### **Chaining Commands**
Wait for each command to complete:
```
"Open Chrome"
[Wait for response]
"Play Coldplay on YouTube"
[Wait for music to start]
"Create folder Music Notes"
```

### **Using Workflows Efficiently**
```
Morning: "Start my workday" (1 command = 6 actions)
Coding: "Start coding session" (1 command = 5 actions)
Focus: "Focus mode" (minimal distractions)
Break: "Take a break" (health reminders)
Evening: "End workday" (backup + cleanup)
```

### **Safe File Operations**
Always confirm critical actions:
```
"Clean downloads" → Asks confirmation
"Yes" → Proceeds
"No" → Cancels safely
```

---

## 📝 COMMAND VARIATIONS

Many commands have multiple ways to say them:

### **Time**
- "What time is it"
- "Tell me the time"
- "Current time"
- "Time"

### **Date**
- "What's the date"
- "Tell me the date"
- "What day is it"
- "Today's date"

### **Exit**
- "Quit Gideon" ← BEST
- "Exit Gideon"
- "Goodbye Gideon"
- "Stop Gideon"

### **Help**
- "Help"
- "What can you do"
- "Show commands"
- "Gideon help"

---

## 🌟 MOST POPULAR COMMANDS

Based on typical usage:

1. **"Start my workday"** - Complete workspace setup
2. **"Play [song] on YouTube"** - Entertainment
3. **"Open Chrome"** - Most used app
4. **"What time is it"** - Quick info
5. **"Start coding session"** - Dev environment
6. **"Help"** - Command reference
7. **"Take a break"** - Self-care reminder
8. **"Quit Gideon"** - Reliable exit

---

**For more information, see:**
- README.md - Project overview
- ENHANCEMENTS.md - Latest features
- PROJECT_INFO.md - Technical details

---

*Gideon v1.0.0*
*Voice-Controlled Task Automation System*
*Developer: Muhammad Ali @ CodeCelix*
*January 2026*
