# Gideon - Troubleshooting Guide

Comprehensive solutions for common issues with Gideon Voice Assistant.

## 📑 Quick Navigation

- [Microphone Issues](#-microphone-issues)
- [Speech Recognition Issues](#-speech-recognition-issues)
- [Text-to-Speech Issues](#-text-to-speech-issues)
- [YouTube Playback Issues](#-youtube-playback-issues)
- [Application Launch Issues](#-application-launch-issues)
- [Installation Issues](#-installation-issues)
- [Performance Issues](#-performance-issues)
- [General Issues](#-general-issues)

---

## 🎤 Microphone Issues

### Problem: "I'm having trouble accessing the microphone"

**Symptoms**: Gideon can't hear you, initialization fails, microphone check fails

**Solutions**:

1. **Check Physical Connection**
   ```bash
   # Verify microphone in Device Manager
   # Windows Key + X > Device Manager > Audio inputs and outputs
   ```
   - Look for your microphone in the list
   - If you see a yellow exclamation mark, update drivers

2. **Grant Permissions**
   - Windows Settings > Privacy > Microphone
   - Enable "Allow apps to access your microphone"
   - Enable "Allow desktop apps to access your microphone"

3. **Close Conflicting Applications**
   - Close: Zoom, Discord, Skype, Teams
   - Close: OBS, Audacity, or any recording software
   - Only ONE application can use microphone at a time

4. **Set as Default Device**
   - Right-click speaker icon in taskbar
   - Open Sound settings
   - Input > Select your microphone as default

5. **Test Microphone**
   ```bash
   # Windows Voice Recorder test
   # Start > Voice Recorder > Record something
   ```

6. **Update Audio Drivers**
   - Visit manufacturer website
   - Download latest audio drivers
   - Restart computer after installation

7. **Try Different USB Port**
   - For USB microphones, try different USB port
   - Avoid USB hubs, connect directly to computer

### Problem: Microphone volume too low

**Solutions**:

1. **Increase Windows Volume**
   - Settings > System > Sound > Input
   - Adjust input volume to 80-90%

2. **Adjust Microphone Boost**
   - Right-click speaker icon > Sounds
   - Recording tab > Your microphone > Properties
   - Levels tab > Microphone Boost: +20 to +30 dB

3. **Adjust Gideon Sensitivity**
   Edit `config.py`:
   ```python
   RECOGNITION_ENERGY_THRESHOLD = 3000  # Lower = more sensitive
   # Try values: 2000, 2500, 3000, 3500, 4000
   ```

### Problem: Too much background noise triggering false commands

**Solutions**:

1. **Reduce Ambient Noise**
   - Close windows
   - Turn off fans/AC
   - Move away from noisy equipment

2. **Increase Threshold**
   Edit `config.py`:
   ```python
   RECOGNITION_ENERGY_THRESHOLD = 5000  # Higher = less sensitive
   ```

3. **Use Better Microphone**
   - Headset microphones are better than built-in
   - USB microphones have better noise cancellation
   - Position microphone 6-12 inches from mouth

---

## 🗣️ Speech Recognition Issues

### Problem: Commands not recognized / "I didn't catch that"

**Solutions**:

1. **Speak Clearly**
   - Normal speaking volume
   - Clear pronunciation
   - Don't speak too fast or too slow
   - Face the microphone

2. **Check Internet Connection**
   ```bash
   ping google.com
   ```
   Google Speech Recognition requires internet!

3. **Wait for "Listening..." indicator**
   - Don't speak immediately after Gideon finishes
   - Wait for the listening confirmation

4. **Reduce Background Noise**
   - Turn off music/TV
   - Close windows
   - Quiet environment = better recognition

5. **Try Alternative Phrasing**
   - Instead of: "can you open notepad"
   - Say: "open notepad"
   - Use exact command phrases from COMMANDS.md

6. **Check Microphone Quality**
   ```bash
   # Test with Windows Speech Recognition
   # Settings > Speech > Get started
   ```

### Problem: Wrong command executed

**Solutions**:

1. **Be More Specific**
   - Instead of: "play music"
   - Say: "play music on youtube" or "play song" (for local music)

2. **Use Exact Application Names**
   - "open visual studio code" not "open vscode"
   - "open google chrome" not "open chrome browser"

3. **Check Command List**
   - See [COMMANDS.md](COMMANDS.md) for exact phrases
   - Commands are case-insensitive but word-order matters

### Problem: "Unknown command" for valid commands

**Solutions**:

1. **Update Command Registry**
   Check if command exists in `commands.py`:
   ```python
   # Search for your command in COMMAND_REGISTRY
   ```

2. **Check Command Aliases**
   See `config.py` > `COMMAND_ALIASES` for alternative phrasings

3. **Add Custom Command**
   See [README.md - Adding New Commands](README.md#-adding-new-commands)

---

## 🔊 Text-to-Speech Issues

### Problem: Can't hear Gideon speaking

**Solutions**:

1. **Check System Volume**
   - Ensure not muted
   - Volume at 50% or higher
   - Check both system and application volume

2. **Test TTS Engine**
   ```bash
   python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('Test'); engine.runAndWait()"
   ```

3. **Check Audio Output Device**
   - Settings > System > Sound > Output
   - Select correct speakers/headphones

4. **Increase Gideon Volume**
   Edit `config.py`:
   ```python
   TTS_VOLUME = 1.0  # Maximum volume (0.0 to 1.0)
   ```

5. **Reinstall pyttsx3**
   ```bash
   pip uninstall pyttsx3
   pip install pyttsx3
   ```

### Problem: Gideon speaks too fast/slow

**Solution**:

Edit `config.py`:
```python
TTS_RATE = 150  # Slower (default: 175, range: 100-250)
# or
TTS_RATE = 200  # Faster
```

### Problem: Voice sounds robotic or wrong

**Solution**:

Change voice in `config.py`:
```python
TTS_VOICE_INDEX = 0  # Try 0, 1, or 2
```

List available voices:
```bash
python -c "import pyttsx3; engine = pyttsx3.init(); voices = engine.getProperty('voices'); [print(f'{i}: {v.name}') for i, v in enumerate(voices)]"
```

---

## 🎬 YouTube Playback Issues

### Problem: YouTube videos don't play

**Solutions**:

1. **Check Internet Connection**
   ```bash
   ping youtube.com
   ```

2. **Check Default Browser**
   - Set default browser: Settings > Apps > Default apps > Web browser
   - Recommended: Chrome or Edge

3. **Update pywhatkit**
   ```bash
   pip install --upgrade pywhatkit
   ```

4. **Test pywhatkit Directly**
   ```bash
   python -c "import pywhatkit; pywhatkit.playonyt('test video')"
   ```

5. **Disable Browser Extensions**
   - Ad blockers might interfere
   - Temporarily disable extensions

6. **Clear Browser Cache**
   - Ctrl+Shift+Delete in browser
   - Clear cached images and files

### Problem: Wrong video plays

**Solutions**:

1. **Be More Specific**
   - Instead of: "play Coldplay"
   - Say: "play Coldplay Viva La Vida on youtube"

2. **Include Artist Name**
   - "play Yellow by Coldplay on youtube"

3. **Add Year for Movies**
   - "play Avengers 2019 on youtube"

### Problem: Browser opens but video doesn't autoplay

**Solutions**:

1. **Check YouTube Autoplay Setting**
   - YouTube website > Click autoplay toggle (should be ON)

2. **Browser Settings**
   - Chrome: Settings > Privacy and security > Site settings > Media > Allow autoplay

3. **Update Browser**
   - Ensure latest version of browser installed

---

## 💻 Application Launch Issues

### Problem: "I couldn't find [application]"

**Solutions**:

1. **Verify Application is Installed**
   - Check Start Menu for the application
   - Try launching manually first

2. **Check Application Path**
   Edit `config.py`:
   ```python
   APPLICATIONS = {
       "app name": "correct_executable.exe",
   }
   ```

3. **Add to System PATH**
   - For VS Code, Chrome, etc.
   - Add installation directory to Windows PATH

4. **Use Full Path**
   Edit `config.py`:
   ```python
   "app name": r"C:\Program Files\App\app.exe",
   ```

5. **Common Application Paths**
   ```python
   "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
   "vscode": r"C:\Users\YourName\AppData\Local\Programs\Microsoft VS Code\Code.exe",
   ```

### Problem: Application opens but immediately closes

**Solutions**:

1. **Check Application Logs**
   - See `logs/` directory for errors

2. **Try Manual Launch**
   - If works manually but not via Gideon, it's a path issue

3. **Use START Command**
   Edit `commands.py`:
   ```python
   subprocess.Popen(["start", app_executable], shell=True)
   ```

---

## 📦 Installation Issues

### Problem: PyAudio installation fails

**Error**: "Microsoft Visual C++ 14.0 is required"

**Solutions**:

**Method 1: Use pipwin (Easiest)**
```bash
pip install pipwin
pipwin install pyaudio
```

**Method 2: Download Wheel**
1. Go to: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
2. Download matching Python version:
   - Python 3.10 (64-bit): `PyAudio‑0.2.14‑cp310‑cp310‑win_amd64.whl`
   - Python 3.9 (64-bit): `PyAudio‑0.2.14‑cp39‑cp39‑win_amd64.whl`
3. Install:
   ```bash
   pip install PyAudio-0.2.14-cp310-cp310-win_amd64.whl
   ```

**Method 3: Install Visual C++ Build Tools**
- Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Install "Desktop development with C++"
- Restart, then: `pip install pyaudio`

### Problem: "pip is not recognized"

**Solutions**:

1. **Use python -m pip**
   ```bash
   python -m pip install -r requirements.txt
   ```

2. **Add Python to PATH**
   - Reinstall Python with "Add to PATH" checked

3. **Install pip**
   ```bash
   python -m ensurepip --upgrade
   ```

### Problem: SSL Certificate Error

**Solutions**:

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Problem: Permission denied

**Solutions**:

1. **Run as Administrator**
   - Right-click Command Prompt > Run as administrator

2. **User Install**
   ```bash
   pip install --user -r requirements.txt
   ```

3. **Fix Permissions**
   ```bash
   python -m pip install --upgrade pip
   ```

---

## ⚡ Performance Issues

### Problem: High CPU usage

**Normal Behavior**:
- 20-40% CPU during listening is normal
- Spikes to 60-80% during speech recognition is normal

**If Excessive (90-100% constantly)**:

1. **Close Background Apps**
   - Close unnecessary programs
   - Check Task Manager

2. **Increase Timeout**
   Edit `config.py`:
   ```python
   RECOGNITION_TIMEOUT = 10  # Increase from 5 to 10
   ```

3. **Reduce Logging**
   Edit `config.py`:
   ```python
   LOG_LEVEL = "WARNING"  # Instead of "INFO"
   ```

### Problem: Slow response time

**Solutions**:

1. **Check Internet Speed**
   - Speech recognition needs good connection
   - Minimum 1 Mbps recommended

2. **Reduce Timeout**
   Edit `config.py`:
   ```python
   RECOGNITION_TIMEOUT = 3  # Faster response
   ```

3. **Close Background Apps**
   - Free up system resources

### Problem: Memory leak / increasing RAM usage

**Solutions**:

1. **Restart Gideon Periodically**
   - Normal to have slight increase over time
   - Restart every few hours if needed

2. **Update Dependencies**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

---

## 🔧 General Issues

### Problem: Gideon won't start

**Solutions**:

1. **Check Python Version**
   ```bash
   python --version
   # Must be 3.8 or higher
   ```

2. **Check Virtual Environment**
   ```bash
   # Make sure venv is activated
   # You should see (venv) in prompt
   venv\Scripts\activate
   ```

3. **Reinstall Dependencies**
   ```bash
   pip install --force-reinstall -r requirements.txt
   ```

4. **Check Logs**
   - See `logs/` directory for error details
   - Look for CRITICAL or ERROR level messages

5. **Run Diagnostics**
   ```bash
   python -c "import config, utils, commands; print('✓ All modules load successfully')"
   ```

### Problem: "ModuleNotFoundError"

**Solutions**:

1. **Activate Virtual Environment**
   ```bash
   venv\Scripts\activate
   ```

2. **Reinstall Missing Module**
   ```bash
   pip install <module_name>
   ```

3. **Reinstall All**
   ```bash
   pip install -r requirements.txt
   ```

### Problem: Gideon won't shutdown with Ctrl+C

**This is BY DESIGN!**

Gideon only stops with voice command:
- Say: "shutdown gideon"
- Or: "gideon shutdown"

If absolutely necessary, use Task Manager:
- Ctrl+Shift+Esc > Find Python > End Task

### Problem: Log files growing too large

**Solutions**:

1. **Delete Old Logs**
   ```bash
   cd logs
   del *.log
   ```

2. **Reduce Logging Level**
   Edit `config.py`:
   ```python
   LOG_LEVEL = "WARNING"  # Less verbose
   ```

3. **Add Log Rotation**
   (Future feature - manual deletion for now)

---

## 🆘 Still Having Issues?

### Diagnostic Information to Collect

When reporting issues, include:

1. **System Info**
   ```bash
   python --version
   python -c "import platform; print(platform.platform())"
   ```

2. **Installed Packages**
   ```bash
   pip list
   ```

3. **Error Logs**
   - Copy relevant logs from `logs/` directory

4. **Steps to Reproduce**
   - Exact commands that cause the issue
   - What you expected vs what happened

5. **Audio Setup**
   - Microphone model
   - Connection type (USB, 3.5mm, Bluetooth)
   - Speakers/headphones info

### Emergency Reset

If nothing works:

```bash
# 1. Deactivate virtual environment
deactivate

# 2. Delete virtual environment
rmdir /s venv

# 3. Recreate virtual environment
python -m venv venv
venv\Scripts\activate

# 4. Reinstall everything
pip install -r requirements.txt

# 5. Test
python gideon.py
```

---

## 📞 Getting Help

1. Check [README.md](README.md) for general info
2. See [COMMANDS.md](COMMANDS.md) for command syntax
3. Review [INSTALLATION.md](INSTALLATION.md) for setup
4. Check logs in `logs/` directory
5. Search existing GitHub issues
6. Create new issue with diagnostic info

---

## ✅ Quick Troubleshooting Checklist

When something goes wrong, check:

- [ ] Virtual environment activated?
- [ ] All dependencies installed?
- [ ] Internet connection working?
- [ ] Microphone connected and detected?
- [ ] Microphone permissions granted?
- [ ] No other app using microphone?
- [ ] Speakers/headphones working?
- [ ] Python 3.8+ installed?
- [ ] Recent Windows updates?
- [ ] Checked log files?

---

<div align="center">

**Still stuck? Don't worry!**

Most issues are quick fixes. Take a break, come back fresh, and try the solutions systematically.

[Return to README](README.md) | [Installation Guide](INSTALLATION.md) | [Commands List](COMMANDS.md)

</div>
