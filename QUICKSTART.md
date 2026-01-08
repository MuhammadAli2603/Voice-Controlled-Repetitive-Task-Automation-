# Gideon Quick Start Guide

Get Gideon running in under 5 minutes!

## ⚡ Super Quick Start

```bash
# 1. Navigate to project directory
cd "Voice-Controlled Repetitive Task Automation"

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run Gideon!
python gideon.py
```

## 🎤 First Commands to Try

Once Gideon says "Gideon online. How may I assist you?", try these:

1. **"what time is it"** - Gideon will tell you the current time
2. **"open notepad"** - Opens Notepad application
3. **"play Imagine Dragons on youtube"** - Plays video on YouTube (KEY FEATURE!)
4. **"help"** - Lists all available commands
5. **"shutdown gideon"** - Stops Gideon properly

## ✅ Pre-Flight Checklist

Before running Gideon, make sure:

- [ ] Python 3.8+ installed (`python --version`)
- [ ] Microphone connected and working
- [ ] Speakers/headphones connected
- [ ] Internet connection active
- [ ] No other app using microphone (close Zoom, Discord, etc.)

## 🔧 Installation Troubleshooting

### PyAudio Won't Install?

Try this:
```bash
pip install pipwin
pipwin install pyaudio
```

### Can't Hear Gideon?

- Check system volume
- Verify speakers are connected
- Test: `python -c "import pyttsx3; e=pyttsx3.init(); e.say('test'); e.runAndWait()"`

### Microphone Not Working?

- Check Windows Settings > Privacy > Microphone
- Grant permissions to Python
- Close other apps using microphone

## 📝 Quick Command Reference

| Say This | Gideon Does |
|----------|-------------|
| "play [song] on youtube" | Plays YouTube video |
| "open [app name]" | Opens application |
| "what time is it" | Tells current time |
| "create folder [name]" | Creates folder on Desktop |
| "help" | Lists all commands |
| "shutdown gideon" | Stops Gideon |

## 🚀 Ready to Go!

That's it! You're ready to use Gideon.

For complete documentation, see [README.md](README.md)

For all commands, see [COMMANDS.md](COMMANDS.md)

---

**Pro Tip**: Say "help" to Gideon anytime to hear what it can do!
