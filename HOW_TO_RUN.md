# How to Run Gideon

Quick reference guide for running Gideon Voice Assistant.

## 🚀 First Time Setup (One-time only)

### Step 1: Open Command Prompt
```bash
# Windows: Press Win + R, type 'cmd', press Enter
# Or search for "Command Prompt" in Start Menu
```

### Step 2: Navigate to Project
```bash
cd "C:\Users\hb\Desktop\Internship\Voice-Controlled Repetitive Task Automation"
```

### Step 3: Create Virtual Environment
```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment
```bash
venv\Scripts\activate
```
You should see `(venv)` at the start of your prompt.

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

Wait for installation to complete (~2-3 minutes).

### Step 6: Test Installation (Optional but Recommended)
```bash
python test_installation.py
```

This will verify everything is working correctly.

---

## 🎯 Running Gideon (Every time)

### Quick Start
```bash
# 1. Open Command Prompt
# 2. Navigate to project
cd "C:\Users\hb\Desktop\Internship\Voice-Controlled Repetitive Task Automation"

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Run Gideon!
python gideon.py
```

### What to Expect
```
================================================================
             GIDEON - Voice Assistant Starting...
================================================================

[1/4] Checking microphone access...
✓ Microphone access confirmed

[2/4] Initializing text-to-speech engine...
✓ Text-to-speech engine ready

[3/4] Loading command registry...
✓ Loaded 50+ command patterns

[4/4] Final system check...
✓ All systems operational

================================================================
Gideon is now online!
================================================================

🎤 Gideon: "Gideon online. All systems operational. How may I assist you?"
🎤 Gideon: "Good morning!"

💡 TIP: Say 'help' to see what I can do
🛑 To stop me, say: 'shutdown gideon'

----------------------------------------------------------------
🎤 Listening for commands...
```

---

## 🎤 First Commands to Try

### 1. Test Time Command
**Say**: "what time is it"
**Gideon**: "The time is 2:30 PM"

### 2. Test Application Opening
**Say**: "open notepad"
**Gideon**: "Opening Notepad for you"
**Result**: Notepad launches

### 3. Test YouTube (KEY FEATURE!)
**Say**: "play Imagine Dragons on youtube"
**Gideon**: "Playing Imagine Dragons on YouTube"
**Result**: Browser opens and video plays

### 4. Get Help
**Say**: "help"
**Gideon**: Lists available commands

### 5. Shutdown Properly
**Say**: "shutdown gideon"
**Gideon**: "Shutting down. Goodbye!"

---

## 🛑 How to Stop Gideon

### Proper Way (RECOMMENDED)
**Say**: "shutdown gideon"

Alternative shutdown commands:
- "gideon shutdown"
- "exit gideon"
- "quit gideon"

### Emergency Stop (NOT RECOMMENDED)
If voice commands aren't working:
1. Press `Ctrl + Shift + Esc` (Task Manager)
2. Find "Python" process
3. Click "End Task"

**Note**: Always prefer voice shutdown commands!

---

## ⚠️ Before Running - Checklist

Make sure these are ready:

- [ ] Microphone connected and working
- [ ] Speakers/headphones connected
- [ ] Internet connection active
- [ ] No other app using microphone (close Zoom, Discord)
- [ ] Microphone permissions granted to Python
- [ ] Virtual environment activated (see `(venv)` in prompt)

---

## 🔧 Common Issues When Running

### Issue: "python is not recognized"
**Solution**:
- Install Python from python.org
- Make sure "Add to PATH" was checked during installation

### Issue: "No module named 'speech_recognition'"
**Solution**:
```bash
# Make sure virtual environment is activated
venv\Scripts\activate

# Then reinstall
pip install -r requirements.txt
```

### Issue: Can't hear Gideon
**Solution**:
- Check system volume
- Verify speakers are connected and working
- Test: `python -c "import pyttsx3; e=pyttsx3.init(); e.say('test'); e.runAndWait()"`

### Issue: Microphone not working
**Solution**:
- Check Windows Privacy Settings > Microphone
- Grant permissions to Python
- Close other apps using microphone

---

## 📖 Full Documentation

For complete documentation, see:

| File | Purpose |
|------|---------|
| [README.md](README.md) | Complete documentation |
| [QUICKSTART.md](QUICKSTART.md) | 5-minute quick start |
| [COMMANDS.md](COMMANDS.md) | All 75+ commands |
| [INSTALLATION.md](INSTALLATION.md) | Detailed setup guide |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Problem solving |

---

## 🎯 Quick Reference Card

```
┌─────────────────────────────────────────────────────┐
│            GIDEON QUICK REFERENCE                   │
├─────────────────────────────────────────────────────┤
│                                                     │
│  START:                                             │
│    python gideon.py                                 │
│                                                     │
│  STOP:                                              │
│    Say: "shutdown gideon"                           │
│                                                     │
│  HELP:                                              │
│    Say: "help"                                      │
│                                                     │
│  YOUTUBE:                                           │
│    Say: "play [video] on youtube"                   │
│                                                     │
│  APPS:                                              │
│    Say: "open [app name]"                           │
│                                                     │
│  WEBSITES:                                          │
│    Say: "open [website]"                            │
│                                                     │
│  TIME/DATE:                                         │
│    Say: "what time is it"                           │
│    Say: "what date is it"                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🎉 You're Ready!

That's everything you need to run Gideon!

**Next Steps**:
1. Run `python gideon.py`
2. Try the test commands above
3. Say "help" to see all capabilities
4. Explore [COMMANDS.md](COMMANDS.md) for full command list

---

**Tip**: Keep this file open for quick reference while using Gideon!
