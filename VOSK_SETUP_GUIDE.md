# Vosk Setup Guide for Gideon

Complete guide to setting up offline speech recognition for Gideon using Vosk.

## Table of Contents

- [What is Vosk?](#what-is-vosk)
- [Why Vosk?](#why-vosk)
- [Quick Start](#quick-start)
- [Detailed Installation](#detailed-installation)
- [Model Selection Guide](#model-selection-guide)
- [Troubleshooting](#troubleshooting)
- [Performance Tips](#performance-tips)
- [Multi-Language Setup](#multi-language-setup)
- [Advanced Configuration](#advanced-configuration)

---

## What is Vosk?

Vosk is an offline open-source speech recognition toolkit that provides:
- **100% Offline Operation** - No internet required after setup
- **Cross-Platform** - Works on Windows, Linux, macOS, Android, iOS
- **Lightweight** - Models start at 40MB (vs 1GB+ for alternatives)
- **Fast** - Real-time recognition with low latency
- **Privacy-Focused** - All processing happens locally

## Why Vosk?

Gideon migrated from PyAudio/Google Speech Recognition to Vosk to solve critical issues:

### Problems with PyAudio (OLD)
- ❌ Requires PortAudio DLL (installation nightmare on Windows)
- ❌ Requires Visual Studio Build Tools
- ❌ Frequent DLL not found errors
- ❌ Complex wheel file installation
- ❌ Incompatible with newer Python versions

### Benefits of Vosk (NEW)
- ✅ Pure Python dependencies (sounddevice + numpy)
- ✅ No DLL issues or build tools required
- ✅ Works offline (no Google API dependency)
- ✅ Faster recognition (no network latency)
- ✅ Privacy-focused (all local processing)
- ✅ Easy installation in 2 minutes

---

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Working microphone
- ~100 MB free disk space

### 3-Step Installation

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Download Vosk model (interactive wizard)
python vosk_setup.py

# Step 3: Test setup
python audio_handler.py
```

That's it! You're ready to run Gideon.

---

## Detailed Installation

### Step 1: Install Python Dependencies

```bash
pip install vosk sounddevice soundfile numpy tqdm
```

**What gets installed:**
- `vosk` - Speech recognition engine
- `sounddevice` - Audio input/output (replaces PyAudio)
- `soundfile` - Audio file handling
- `numpy` - Numerical operations
- `tqdm` - Progress bars for downloads

### Step 2: Download Vosk Model

Run the interactive setup wizard:

```bash
python vosk_setup.py
```

The wizard will:
1. Display available models with recommendations
2. Let you choose the right model for your needs
3. Download and extract the model automatically
4. Update config.py with the model path

**Available Models:**

| Model | Size | Accuracy | Speed | Best For |
|-------|------|----------|-------|----------|
| small-en | 40 MB | Good | Very Fast | Voice commands (Recommended) |
| large-en | 1.8 GB | Excellent | Moderate | Dictation, transcription |
| urdu | 45 MB | Good | Fast | Roman Urdu commands |
| tiny-en | 40 MB | Moderate | Extremely Fast | Low-end hardware |

**Recommendation:** Use `small-en` (default) for Gideon voice commands.

### Step 3: Verify Installation

Run diagnostics to ensure everything works:

```bash
python audio_handler.py
```

This will:
- ✅ Check Vosk installation
- ✅ Check sounddevice installation
- ✅ Verify model loading
- ✅ List available audio devices
- ✅ Test your microphone with live volume display

---

## Model Selection Guide

### For Voice Commands (Gideon) - Use `small-en`
- **Size:** 40 MB
- **Accuracy:** Good (85-90% for clear commands)
- **Speed:** Very fast real-time recognition
- **Use Case:** Voice assistants, command recognition
- **Download:** Automatic via `python vosk_setup.py`

**Best for:**
- Quick responses
- Limited vocabulary (commands, apps, websites)
- Low-end hardware
- Fast startup time

### For Dictation - Use `large-en`
- **Size:** 1.8 GB
- **Accuracy:** Excellent (95%+ with clear speech)
- **Speed:** Moderate (still real-time)
- **Use Case:** Transcription, long-form dictation
- **Download:** `python vosk_setup.py --model large-en`

**Best for:**
- Professional transcription
- Complex sentences
- High accuracy requirements
- Powerful hardware

### For Roman Urdu - Use `urdu`
- **Size:** 45 MB
- **Accuracy:** Good for Roman Urdu
- **Speed:** Fast
- **Use Case:** Bilingual support (English + Urdu)
- **Download:** `python vosk_setup.py --model urdu`

**Best for:**
- Pakistani users
- Roman Urdu commands
- Bilingual environments
- Multi-language support

---

## Troubleshooting

### Issue 1: Model Not Found

**Error:**
```
❌ Vosk model not found at: vosk-model-small-en-us-0.15
```

**Solution:**
```bash
# Re-run setup wizard
python vosk_setup.py

# Or manually download from:
# https://alphacephei.com/vosk/models
# Extract to project root folder
```

### Issue 2: Microphone Not Detected

**Error:**
```
❌ Microphone test failed: No input device found
```

**Solution:**
1. Check microphone is physically connected
2. Grant microphone permissions to Python/Terminal
3. Close other apps using microphone (Zoom, Discord, etc.)
4. List available devices:
   ```bash
   python -c "from audio_handler import VoskAudioHandler; VoskAudioHandler().list_audio_devices()"
   ```
5. If you have multiple microphones, specify device in config.py:
   ```python
   AUDIO_DEVICE_INDEX = 0  # Change to your device index
   ```

### Issue 3: Low Volume / Recognition Issues

**Error:**
```
⚠️ Warning: Volume very low
```

**Solution:**
1. Speak louder and closer to microphone
2. Increase microphone volume in system settings:
   - Windows: Settings → Sound → Input → Device Properties
3. Adjust sensitivity threshold in config.py:
   ```python
   SILENCE_THRESHOLD = 300.0  # Lower = more sensitive (default: 500)
   ```
4. Test microphone levels:
   ```bash
   python audio_handler.py
   ```

### Issue 4: Recognition Inaccurate

**Problem:** Vosk doesn't understand commands correctly

**Solutions:**

**1. Speak clearly and naturally**
- Don't shout or whisper
- Avoid background noise
- Use consistent pronunciation

**2. Adjust phrase time limit in config.py:**
```python
RECOGNITION_PHRASE_LIMIT = 15  # Allow more time (default: 10)
```

**3. Use larger model for better accuracy:**
```bash
python vosk_setup.py --model large-en
```

**4. Check command format:**
- Good: "open chrome"
- Good: "play coldplay on youtube"
- Bad: "umm... can you... like... open chrome?"

### Issue 5: Slow Performance

**Problem:** Recognition is slow or delayed

**Solutions:**

**1. Use smaller model:**
```bash
python vosk_setup.py --model small-en  # Faster than large-en
```

**2. Close other applications**
- Free up CPU and memory
- Close browser tabs, video players

**3. Disable unused features in config.py:**
```python
ENABLE_URDU_RECOGNITION = False  # If not using Urdu
```

**4. Adjust audio settings:**
```python
SAMPLE_RATE = 8000  # Lower quality but faster (default: 16000)
```

### Issue 6: ModuleNotFoundError

**Error:**
```
ModuleNotFoundError: No module named 'vosk'
```

**Solution:**
```bash
# Ensure you're in correct virtual environment
pip install vosk sounddevice numpy

# If using virtual environment:
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate

# Then install:
pip install -r requirements.txt
```

---

## Performance Tips

### Optimize for Speed

**1. Use small model:**
```bash
python vosk_setup.py --model small-en
```

**2. Reduce sample rate (if quality not critical):**
```python
# config.py
SAMPLE_RATE = 8000  # Faster but lower quality
```

**3. Reduce phrase time limit:**
```python
RECOGNITION_PHRASE_LIMIT = 5  # Process faster (default: 10)
```

### Optimize for Accuracy

**1. Use large model:**
```bash
python vosk_setup.py --model large-en
```

**2. Increase phrase time limit:**
```python
RECOGNITION_PHRASE_LIMIT = 15  # Allow complete sentences
```

**3. Adjust silence threshold:**
```python
SILENCE_THRESHOLD = 400.0  # Detect quieter speech
```

**4. Use high-quality microphone**
- USB microphone recommended
- Reduce background noise
- Proper positioning (6-12 inches from mouth)

### Balance Speed & Accuracy

**Recommended settings for Gideon (default):**
```python
# config.py
VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"  # Fast & accurate enough
SAMPLE_RATE = 16000  # Good quality
RECOGNITION_PHRASE_LIMIT = 10  # Reasonable time
SILENCE_THRESHOLD = 500.0  # Moderate sensitivity
```

---

## Multi-Language Setup

### English + Roman Urdu (Bilingual Mode)

**Step 1: Download Urdu model**
```bash
python vosk_setup.py --model urdu
```

**Step 2: Enable in config.py**
```python
ENABLE_URDU_RECOGNITION = True
URDU_MODEL_PATH = "vosk-model-small-ur-0.3"
```

**Step 3: Test bilingual commands**
```bash
python gideon.py

# Try commands:
"chrome kholo"  # Opens Chrome
"youtube pe coldplay chalao"  # Plays on YouTube
"help"  # Works in English too
```

**Supported Roman Urdu Commands:**
- Application control: "chrome kholo", "notepad band karo"
- YouTube: "youtube pe despacito chalao"
- Time/Date: "time kya hai", "date batao"
- System: "gideon band karo"

See `multilingual.py` for complete list of 47+ Urdu commands.

---

## Advanced Configuration

### Custom Audio Device

If you have multiple microphones, specify which one to use:

```python
# config.py
AUDIO_DEVICE_INDEX = 0  # Change to your device index
```

**Find your device index:**
```bash
python -c "from audio_handler import VoskAudioHandler; VoskAudioHandler().list_audio_devices()"
```

### Continuous Listening Mode

For always-on voice control (not default in Gideon):

```python
from audio_handler import get_audio_handler

def handle_command(text):
    print(f"Heard: {text}")
    # Process command here

handler = get_audio_handler()
handler.continuous_listen(handle_command)
```

### Custom Model Path

To use a model from a different location:

```python
# config.py
import os
VOSK_MODEL_PATH = os.path.expanduser("~/models/vosk-model-en-us-0.22")
```

### Adjust Recognition Parameters

Fine-tune recognition behavior:

```python
# config.py

# How long to wait for speech to start (seconds)
RECOGNITION_TIMEOUT = 5

# Maximum length of a single command (seconds)
RECOGNITION_PHRASE_LIMIT = 10

# Volume threshold to detect speech (lower = more sensitive)
SILENCE_THRESHOLD = 500.0

# Number of retry attempts on failure
MAX_RETRY_ATTEMPTS = 3
```

### Logging and Debugging

Enable detailed logging for troubleshooting:

```python
# config.py
LOG_LEVEL = "DEBUG"  # More verbose logs (default: "INFO")
```

View Vosk-specific logs:
```bash
tail -f logs/gideon_log_*.log
```

---

## Model Management

### Download Additional Models

```bash
# Download specific model
python vosk_setup.py --model large-en

# Force re-download (if corrupted)
python vosk_setup.py --model small-en --force

# List all available models
python vosk_setup.py --list
```

### Manual Model Installation

If automatic download fails:

1. Go to https://alphacephei.com/vosk/models
2. Download desired model ZIP file
3. Extract to project root folder
4. Update config.py:
   ```python
   VOSK_MODEL_PATH = "vosk-model-small-en-us-0.15"
   ```

### Remove Old Models

```bash
# On Windows
rmdir /s vosk-model-old-version

# On Linux/Mac
rm -rf vosk-model-old-version
```

---

## Testing and Validation

### Run Full Diagnostics

```bash
python audio_handler.py
```

Runs 5 comprehensive tests:
1. ✅ Check Vosk installation
2. ✅ Check sounddevice installation
3. ✅ Verify model loading
4. ✅ List audio devices
5. ✅ Test microphone with live volume

### Test Specific Features

```bash
# List audio devices
python -c "from audio_handler import VoskAudioHandler; VoskAudioHandler().list_audio_devices()"

# Test microphone for 5 seconds
python -c "from audio_handler import VoskAudioHandler; VoskAudioHandler().test_microphone(5)"

# Check model info
python -c "from audio_handler import get_audio_handler; import json; print(json.dumps(get_audio_handler().get_model_info(), indent=2))"
```

---

## Comparison: Vosk vs PyAudio

| Feature | PyAudio (OLD) | Vosk (NEW) |
|---------|--------------|-----------|
| Installation | ❌ Complex (DLL issues) | ✅ Simple (2 commands) |
| Dependencies | ❌ PortAudio DLL required | ✅ Pure Python |
| Internet | ❌ Required for recognition | ✅ 100% offline |
| Privacy | ❌ Sends audio to Google | ✅ All local processing |
| Speed | ⚠️ Moderate (network latency) | ✅ Fast (local) |
| Accuracy | ✅ Good | ✅ Good (configurable) |
| Cost | ⚠️ API rate limits | ✅ Free unlimited |
| Setup Time | ❌ Hours (troubleshooting) | ✅ 2 minutes |
| Cross-platform | ⚠️ Windows issues | ✅ Works everywhere |

---

## Frequently Asked Questions

### Q: Do I need internet for Vosk?
**A:** No! After downloading the model once, Vosk works 100% offline. You only need internet to download the initial model file.

### Q: How accurate is Vosk compared to Google?
**A:** For clear voice commands, Vosk small-en achieves 85-90% accuracy. For dictation, large-en achieves 95%+ accuracy, comparable to Google.

### Q: Can I use Vosk in other languages?
**A:** Yes! Vosk supports 20+ languages including English, Urdu, Hindi, French, German, Spanish, Russian, Chinese, and more. See https://alphacephei.com/vosk/models

### Q: Will Vosk work on Raspberry Pi?
**A:** Yes! Use the `tiny-en` model for best performance on resource-constrained devices.

### Q: How much disk space does Vosk need?
**A:** Small model: 40 MB. Large model: 1.8 GB. Plus ~50 MB for Python libraries.

### Q: Can I use Vosk commercially?
**A:** Yes! Vosk is Apache 2.0 licensed, allowing commercial use without restrictions.

---

## Getting Help

### Still having issues?

1. **Run diagnostics:**
   ```bash
   python audio_handler.py
   ```

2. **Check logs:**
   ```bash
   # View latest log file
   type logs\gideon_log_*.log  # Windows
   cat logs/gideon_log_*.log   # Linux/Mac
   ```

3. **Verify installation:**
   ```bash
   pip list | findstr /i "vosk sounddevice"  # Windows
   pip list | grep -i "vosk\|sounddevice"    # Linux/Mac
   ```

4. **Report issues:**
   - Check Vosk documentation: https://alphacephei.com/vosk/
   - Vosk GitHub: https://github.com/alphacep/vosk-api/issues
   - Gideon project maintainer

---

## Additional Resources

- **Vosk Official Site:** https://alphacephei.com/vosk/
- **Model Downloads:** https://alphacephei.com/vosk/models
- **Vosk Documentation:** https://alphacephei.com/vosk/install
- **Vosk GitHub:** https://github.com/alphacep/vosk-api
- **sounddevice Docs:** https://python-sounddevice.readthedocs.io/

---

**Version:** 1.0.0
**Last Updated:** January 2026
**Gideon Developer:** Muhammad Ali (CodeCelix Internship)
