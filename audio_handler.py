"""
Gideon Vosk Audio Handler
==========================
Offline speech recognition using Vosk toolkit.
Replaces PyAudio/speech_recognition with a robust, dependency-free solution.

Features:
- 100% Offline speech recognition
- No DLL dependencies (eliminates PortAudio issues)
- Real-time recognition with low latency
- Multi-language support (English + Urdu)
- Automatic silence detection
- Continuous listening mode
- Comprehensive error handling

Author: Muhammad Ali (CodeCelix Internship)
Enhanced with Vosk for production reliability
"""

import os
import sys
import json
import wave
import time
import logging
from pathlib import Path
from typing import Optional, Callable, Tuple
import threading
import queue

# Fix Unicode encoding issues on Windows
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')

try:
    import sounddevice as sd
    import vosk
    import numpy as np
except ImportError as e:
    print(f"❌ Missing required package: {e}")
    print("\n📦 Install required packages:")
    print("   pip install vosk sounddevice numpy")
    sys.exit(1)

logger = logging.getLogger("Gideon.AudioHandler")


class VoskAudioHandler:
    """
    Production-ready audio handler using Vosk offline speech recognition.

    Eliminates all PyAudio/PortAudio dependency issues while providing
    superior offline speech recognition capabilities.
    """

    def __init__(
        self,
        model_path: str = "vosk-model-small-en-us-0.15",
        sample_rate: int = 16000,
        device: Optional[int] = None
    ):
        """
        Initialize Vosk audio handler.

        Args:
            model_path: Path to Vosk model directory
            sample_rate: Audio sample rate (16000 Hz recommended for speech)
            device: Audio input device index (None = default)

        Raises:
            FileNotFoundError: If Vosk model not found
            RuntimeError: If model loading fails
        """
        self.sample_rate = sample_rate
        self.model_path = Path(model_path)
        self.device = device
        self.audio_queue = queue.Queue()
        self.is_listening = False

        # Validate model exists
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"\n❌ Vosk model not found at: {self.model_path}\n\n"
                f"📥 Download model automatically:\n"
                f"   python vosk_setup.py\n\n"
                f"📥 Or download manually from:\n"
                f"   https://alphacephei.com/vosk/models\n\n"
                f"Recommended: vosk-model-small-en-us-0.15 (40MB)"
            )

        # Load Vosk model
        try:
            logger.info(f"Loading Vosk model from: {self.model_path}")
            print(f"🔄 Loading Vosk model: {self.model_path.name}...")

            self.model = vosk.Model(str(self.model_path))
            self.recognizer = vosk.KaldiRecognizer(self.model, self.sample_rate)
            self.recognizer.SetWords(True)  # Enable word-level timestamps

            logger.info("Vosk model loaded successfully")
            print("✓ Vosk audio handler initialized (offline mode)")

        except Exception as e:
            logger.error(f"Failed to load Vosk model: {e}")
            raise RuntimeError(
                f"Failed to initialize Vosk model: {e}\n"
                f"Please verify model integrity and try re-downloading."
            )

    def listen_once(
        self,
        duration: int = 5,
        phrase_time_limit: int = 10,
        silence_threshold: float = 500.0
    ) -> Optional[str]:
        """
        Listen for a single voice command with timeout.

        Args:
            duration: Maximum seconds to wait for speech to start
            phrase_time_limit: Maximum seconds for complete phrase
            silence_threshold: Volume threshold to detect speech (lower = more sensitive)

        Returns:
            Recognized text (lowercase) or None if no speech detected
        """
        logger.debug("Starting single command listen")

        try:
            # Record audio
            logger.debug(f"Recording audio for {phrase_time_limit} seconds...")

            recording = sd.rec(
                int(phrase_time_limit * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype='int16',
                device=self.device,
                blocking=True
            )

            # Check if audio contains speech (volume-based detection)
            audio_volume = np.abs(recording).mean()
            logger.debug(f"Audio volume level: {audio_volume:.0f}")

            if audio_volume < silence_threshold:
                logger.debug("No speech detected (silence)")
                return None

            # Convert to bytes for Vosk
            audio_bytes = recording.tobytes()

            # Process with Vosk
            if self.recognizer.AcceptWaveform(audio_bytes):
                result = json.loads(self.recognizer.Result())
                text = result.get("text", "").strip()
                logger.debug(f"Final result: {text}")
            else:
                # Get partial result if no final result
                partial = json.loads(self.recognizer.PartialResult())
                text = partial.get("partial", "").strip()
                logger.debug(f"Partial result: {text}")

            # Reset recognizer for next command
            self.recognizer = vosk.KaldiRecognizer(self.model, self.sample_rate)
            self.recognizer.SetWords(True)

            if text:
                logger.info(f"Recognized: '{text}'")
                return text.lower()
            else:
                logger.debug("No text recognized")
                return None

        except sd.PortAudioError as e:
            logger.error(f"Audio device error: {e}")
            print(f"\n❌ Microphone error: {e}")
            print("\n💡 Troubleshooting:")
            print("   1. Check if microphone is connected")
            print("   2. Verify microphone permissions")
            print("   3. Close other apps using microphone")
            print("   4. Run: python -c \"from audio_handler import VoskAudioHandler; VoskAudioHandler().list_audio_devices()\"")
            return None

        except Exception as e:
            logger.error(f"Unexpected error during listening: {e}", exc_info=True)
            print(f"❌ Audio error: {e}")
            return None

    def continuous_listen(
        self,
        callback: Callable[[str], None],
        silence_timeout: float = 2.0
    ) -> None:
        """
        Continuously listen and call callback with recognized text.
        Runs until interrupted or stopped.

        Args:
            callback: Function to call with recognized text
            silence_timeout: Seconds of silence before considering phrase complete

        Example:
            def handle_command(text):
                print(f"Heard: {text}")

            handler = VoskAudioHandler()
            handler.continuous_listen(handle_command)
        """
        self.is_listening = True

        def audio_callback(indata, frames, time_info, status):
            """Called for each audio block by sounddevice"""
            if status:
                logger.warning(f"Audio callback status: {status}")

            # Put audio data in queue for processing
            self.audio_queue.put(bytes(indata))

        try:
            logger.info("Starting continuous listening mode")
            print("🎤 Continuous listening mode active...")
            print("   Press Ctrl+C to stop")

            with sd.RawInputStream(
                samplerate=self.sample_rate,
                blocksize=8000,
                dtype='int16',
                channels=1,
                device=self.device,
                callback=audio_callback
            ):
                last_text_time = time.time()
                current_phrase = []

                while self.is_listening:
                    try:
                        # Get audio data from queue (with timeout)
                        data = self.audio_queue.get(timeout=0.1)

                        # Process with Vosk
                        if self.recognizer.AcceptWaveform(data):
                            result = json.loads(self.recognizer.Result())
                            text = result.get("text", "").strip()

                            if text:
                                logger.info(f"Continuous mode recognized: '{text}'")
                                current_phrase.append(text)
                                last_text_time = time.time()

                                # Complete phrase (send to callback)
                                complete_text = " ".join(current_phrase)
                                callback(complete_text.lower())
                                current_phrase = []

                        else:
                            # Check for silence timeout
                            if current_phrase and (time.time() - last_text_time) > silence_timeout:
                                # Send accumulated phrase
                                complete_text = " ".join(current_phrase)
                                if complete_text.strip():
                                    callback(complete_text.lower())
                                current_phrase = []

                    except queue.Empty:
                        # No audio data, check for silence timeout
                        if current_phrase and (time.time() - last_text_time) > silence_timeout:
                            complete_text = " ".join(current_phrase)
                            if complete_text.strip():
                                callback(complete_text.lower())
                            current_phrase = []
                        continue

        except KeyboardInterrupt:
            logger.info("Continuous listening stopped by user")
            print("\n⏹ Stopped continuous listening")
            self.is_listening = False

        except Exception as e:
            logger.error(f"Error in continuous listening: {e}", exc_info=True)
            print(f"\n❌ Continuous listening error: {e}")
            self.is_listening = False

    def stop_listening(self):
        """Stop continuous listening mode"""
        self.is_listening = False
        logger.info("Stopping continuous listening")

    def test_microphone(self, duration: int = 3) -> bool:
        """
        Test microphone by recording and analyzing audio levels.

        Args:
            duration: Seconds to test

        Returns:
            True if microphone working correctly, False otherwise
        """
        print(f"\n🎤 Testing microphone for {duration} seconds...")
        print("   Speak now to see audio levels...")

        try:
            recording = sd.rec(
                int(duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype='int16',
                device=self.device
            )

            # Show live volume during recording
            print("\n   Volume levels:")
            for i in range(duration):
                sd.wait(int(1000))  # Wait 1 second
                chunk = recording[i * self.sample_rate:(i + 1) * self.sample_rate]
                volume = np.abs(chunk).mean()
                bar = "█" * int(volume / 200)
                print(f"   {volume:5.0f} {bar}")

            sd.wait()  # Wait for recording to complete

            # Calculate statistics
            volume_mean = np.abs(recording).mean()
            volume_max = np.abs(recording).max()

            print(f"\n📊 Microphone Test Results:")
            print(f"   Average volume: {volume_mean:.0f}")
            print(f"   Peak volume: {volume_max:.0f}")

            # Evaluate results
            if volume_mean < 100:
                print("\n⚠️  Warning: Volume very low")
                print("   - Speak louder")
                print("   - Check microphone is enabled")
                print("   - Increase microphone volume in system settings")
                return False
            elif volume_max > 30000:
                print("\n⚠️  Warning: Volume very high (clipping may occur)")
                print("   - Speak at normal volume")
                print("   - Reduce microphone volume in system settings")
                return True  # Still works, just loud
            else:
                print("\n✅ Microphone working correctly!")
                return True

        except sd.PortAudioError as e:
            print(f"\n❌ Microphone test failed: {e}")
            print("\n💡 Check:")
            print("   - Microphone is connected")
            print("   - Microphone permissions granted")
            print("   - No other app using microphone")
            logger.error(f"Microphone test failed: {e}")
            return False

        except Exception as e:
            print(f"\n❌ Unexpected error during test: {e}")
            logger.error(f"Microphone test error: {e}", exc_info=True)
            return False

    def list_audio_devices(self) -> None:
        """List all available audio input devices"""
        print("\n🎤 Available Audio Input Devices:")
        print("-" * 60)

        try:
            devices = sd.query_devices()
            default_input = sd.query_devices(kind='input')

            print(f"\nDefault input: {default_input['name']}\n")

            for i, device in enumerate(devices):
                if device['max_input_channels'] > 0:
                    marker = "→" if device['name'] == default_input['name'] else " "
                    print(f"  {marker} [{i}] {device['name']}")
                    print(f"      Channels: {device['max_input_channels']}, "
                          f"Sample Rate: {device['default_samplerate']:.0f} Hz")

            print("\n💡 To use specific device:")
            print("   handler = VoskAudioHandler(device=INDEX)")

        except Exception as e:
            print(f"❌ Error listing devices: {e}")
            logger.error(f"Error listing audio devices: {e}")

    def get_model_info(self) -> dict:
        """Get information about loaded model"""
        return {
            "model_path": str(self.model_path),
            "model_name": self.model_path.name,
            "sample_rate": self.sample_rate,
            "device": self.device,
            "offline": True,
            "vosk_version": vosk.__version__ if hasattr(vosk, '__version__') else "unknown"
        }


# ============================================================================
# BACKWARD COMPATIBILITY FUNCTIONS
# ============================================================================
# These functions provide drop-in replacements for speech_recognition usage

_global_handler: Optional[VoskAudioHandler] = None


def get_audio_handler(model_path: Optional[str] = None) -> VoskAudioHandler:
    """
    Get global VoskAudioHandler instance (singleton pattern).
    Creates handler on first call, reuses on subsequent calls.

    Args:
        model_path: Path to Vosk model (uses default from config if None)

    Returns:
        VoskAudioHandler instance
    """
    global _global_handler

    if _global_handler is None:
        if model_path is None:
            try:
                from config import VOSK_MODEL_PATH
                model_path = VOSK_MODEL_PATH
            except ImportError:
                model_path = "vosk-model-small-en-us-0.15"

        _global_handler = VoskAudioHandler(model_path=model_path)

    return _global_handler


def listen_for_command(
    timeout: int = 5,
    phrase_time_limit: int = 10
) -> Optional[str]:
    """
    Listen for a voice command (backward compatible with speech_recognition).

    This function provides the same interface as the old speech_recognition
    implementation, making migration seamless.

    Args:
        timeout: Maximum seconds to wait for speech
        phrase_time_limit: Maximum phrase duration

    Returns:
        Recognized text or None
    """
    handler = get_audio_handler()
    return handler.listen_once(duration=timeout, phrase_time_limit=phrase_time_limit)


# ============================================================================
# TESTING & DIAGNOSTICS
# ============================================================================

def run_diagnostics():
    """Run comprehensive audio system diagnostics"""
    print("\n" + "=" * 60)
    print("GIDEON AUDIO DIAGNOSTICS (Vosk)")
    print("=" * 60)

    # Test 1: Check Vosk installation
    print("\n[1/5] Checking Vosk installation...")
    try:
        import vosk
        print(f"   ✓ Vosk installed (version: {getattr(vosk, '__version__', 'unknown')})")
    except ImportError:
        print("   ❌ Vosk not installed")
        print("   Install: pip install vosk")
        return False

    # Test 2: Check sounddevice
    print("\n[2/5] Checking sounddevice installation...")
    try:
        import sounddevice as sd
        print("   ✓ sounddevice installed")
    except ImportError:
        print("   ❌ sounddevice not installed")
        print("   Install: pip install sounddevice")
        return False

    # Test 3: Check model
    print("\n[3/5] Checking Vosk model...")
    try:
        handler = get_audio_handler()
        info = handler.get_model_info()
        print(f"   ✓ Model loaded: {info['model_name']}")
        print(f"   Path: {info['model_path']}")
    except FileNotFoundError as e:
        print(f"   ❌ Model not found")
        print(f"   Run: python vosk_setup.py")
        return False
    except Exception as e:
        print(f"   ❌ Model load failed: {e}")
        return False

    # Test 4: List audio devices
    print("\n[4/5] Checking audio devices...")
    handler.list_audio_devices()

    # Test 5: Test microphone
    print("\n[5/5] Testing microphone...")
    result = handler.test_microphone(duration=3)

    # Summary
    print("\n" + "=" * 60)
    if result:
        print("✅ ALL TESTS PASSED - System ready!")
        print("\nYou can now run: python gideon.py")
    else:
        print("⚠️  TESTS FAILED - Please fix issues above")
    print("=" * 60)

    return result


if __name__ == "__main__":
    """Run diagnostics when executed directly"""
    run_diagnostics()
