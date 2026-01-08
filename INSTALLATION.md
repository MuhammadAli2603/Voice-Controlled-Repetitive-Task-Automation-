# Gideon - Detailed Installation Guide

Complete step-by-step installation instructions for Gideon Voice Assistant.

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 10 or Windows 11
- **Python**: Version 3.8 or higher
- **RAM**: 4 GB minimum (8 GB recommended)
- **Storage**: 500 MB free space
- **Internet**: Active connection required
- **Audio**: Microphone and speakers/headphones

### Recommended Setup
- **OS**: Windows 11
- **Python**: Version 3.10+
- **RAM**: 8 GB or more
- **Internet**: Broadband connection (for faster speech recognition)
- **Microphone**: USB microphone or headset (better quality than built-in)

---

## 📥 Step 1: Install Python

### Check if Python is Already Installed

Open Command Prompt and run:
```bash
python --version
```

If you see `Python 3.8.x` or higher, you're good! Skip to Step 2.

### Install Python (If Needed)

1. Download Python from: https://www.python.org/downloads/
2. Run the installer
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Choose "Install Now"
5. Verify installation:
   ```bash
   python --version
   ```

---

## 📂 Step 2: Get Gideon

### Option A: Download ZIP

1. Download the project ZIP file
2. Extract to: `C:\Users\YourName\Desktop\Internship\`
3. Navigate to folder:
   ```bash
   cd "C:\Users\YourName\Desktop\Internship\Voice-Controlled Repetitive Task Automation"
   ```

### Option B: Clone Repository (If using Git)

```bash
cd "C:\Users\YourName\Desktop\Internship"
git clone <repository-url>
cd "Voice-Controlled Repetitive Task Automation"
```

---

## 🔧 Step 3: Create Virtual Environment

Virtual environments isolate project dependencies.

### Create Virtual Environment

```bash
python -m venv venv
```

Wait for completion (takes 30-60 seconds).

### Activate Virtual Environment

**Windows Command Prompt:**
```bash
venv\Scripts\activate
```

**Windows PowerShell:**
```bash
venv\Scripts\Activate.ps1
```

**Git Bash:**
```bash
source venv/Scripts/activate
```

You should see `(venv)` at the start of your command prompt.

---

## 📦 Step 4: Install Dependencies

### Install All Packages

```bash
pip install -r requirements.txt
```

This installs:
- `SpeechRecognition` - Voice recognition
- `pyttsx3` - Text-to-speech
- `pywhatkit` - YouTube integration
- `PyAudio` - Audio processing
- And other dependencies

### Troubleshoot PyAudio (If Install Fails)

**Method 1: Using pipwin (Recommended)**
```bash
pip install pipwin
pipwin install pyaudio
```

**Method 2: Download Wheel File**
1. Visit: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
2. Download file matching your Python version:
   - For Python 3.10 (64-bit): `PyAudio‑0.2.14‑cp310‑cp310‑win_amd64.whl`
   - For Python 3.9 (64-bit): `PyAudio‑0.2.14‑cp39‑cp39‑win_amd64.whl`
3. Install:
   ```bash
   pip install path\to\downloaded\PyAudio-0.2.14-cp310-cp310-win_amd64.whl
   ```

### Verify Installation

```bash
python -c "import speech_recognition; import pyttsx3; import pywhatkit; print('✓ All packages installed successfully!')"
```

If you see the success message, you're ready!

---

## 🎤 Step 5: Configure Microphone

### Windows 10/11 Microphone Setup

1. **Open Settings**: Windows Key + I
2. **Go to**: System > Sound
3. **Input section**: Select your microphone
4. **Test**: Speak and watch the input level bar
5. **Adjust**: Set input volume to 70-80%

### Grant Microphone Permissions

1. **Open Settings**: Windows Key + I
2. **Go to**: Privacy > Microphone
3. **Enable**: "Allow apps to access your microphone"
4. **Enable**: "Allow desktop apps to access your microphone"

### Test Microphone

```bash
# In Python
python -c "import speech_recognition as sr; r = sr.Recognizer(); print('✓ Microphone accessible')"
```

---

## 🔊 Step 6: Configure Audio Output

### Test Text-to-Speech

```bash
python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('Gideon initialization test'); engine.runAndWait(); print('✓ TTS working')"
```

You should hear "Gideon initialization test".

### Adjust Volume

If too quiet/loud, edit `config.py`:
```python
TTS_VOLUME = 0.9  # Change to 0.5-1.0
TTS_RATE = 175    # Change to 150-200 (words per minute)
```

---

## ✅ Step 7: Verify Installation

### Run System Check

Create and run this test script:

```bash
python -c "
import speech_recognition as sr
import pyttsx3
import pywhatkit
print('✓ All imports successful')

# Test TTS
engine = pyttsx3.init()
engine.say('All systems operational')
engine.runAndWait()
print('✓ Text-to-speech working')

# Test microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print('✓ Microphone accessible')

print('\n🎉 Gideon is ready to run!')
"
```

---

## 🚀 Step 8: First Run

### Start Gideon

```bash
python gideon.py
```

You should see:
1. ASCII art logo
2. Initialization messages
3. "Gideon online. How may I assist you?"

### Try Your First Command

Say: **"what time is it"**

Gideon should respond with the current time.

### Test YouTube Feature

Say: **"play Imagine Dragons on youtube"**

Your browser should open and start playing.

### Stop Gideon

Say: **"shutdown gideon"**

Gideon will say goodbye and exit.

---

## 🐛 Common Installation Issues

### Issue: Python not found

**Solution**:
- Reinstall Python with "Add to PATH" checked
- Or manually add Python to PATH
- Restart Command Prompt

### Issue: pip not found

**Solution**:
```bash
python -m ensurepip --upgrade
```

### Issue: Permission denied

**Solution**:
- Run Command Prompt as Administrator
- Or use: `pip install --user -r requirements.txt`

### Issue: SSL Certificate Error

**Solution**:
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Issue: "No module named 'win32com'"

**Solution**:
```bash
pip install pywin32
```

### Issue: Microphone not detected

**Solutions**:
1. Check if microphone is properly connected
2. Install audio drivers from manufacturer
3. Check Device Manager for audio devices
4. Try different USB port (for USB mics)
5. Restart computer

---

## 🔄 Updating Gideon

### Update Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Update Python Packages

```bash
pip list --outdated
pip install --upgrade <package-name>
```

---

## 🗑️ Uninstallation

### Remove Virtual Environment

```bash
deactivate  # Exit virtual environment
rmdir /s venv  # Delete venv folder
```

### Remove Project

Simply delete the project folder.

### Remove Python (Optional)

Windows Settings > Apps > Python > Uninstall

---

## 📞 Need Help?

- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed problem-solving
- Check [QUICKSTART.md](QUICKSTART.md) for quick reference
- Review [README.md](README.md) for full documentation

---

## ✅ Installation Checklist

Print this and check off as you go:

- [ ] Python 3.8+ installed
- [ ] Project downloaded/cloned
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] Dependencies installed successfully
- [ ] PyAudio installed (if failed, used alternate method)
- [ ] Microphone connected and tested
- [ ] Microphone permissions granted
- [ ] Speakers/headphones connected
- [ ] Text-to-speech tested
- [ ] Internet connection verified
- [ ] First run successful
- [ ] "What time is it" command worked
- [ ] YouTube playback worked
- [ ] Shutdown command worked

---

<div align="center">

**Installation Complete!** 🎉

Welcome to Gideon - Your Voice Assistant

[Return to README](README.md) | [Quick Start](QUICKSTART.md) | [Commands List](COMMANDS.md)

</div>
