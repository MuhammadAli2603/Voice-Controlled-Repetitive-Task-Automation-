"""
Vosk Model Download and Setup Utility
======================================
Automatically downloads and configures Vosk models for Gideon.

Features:
- Automatic model download with progress bar
- Model verification
- Multiple model options (small/large, English/Urdu)
- Interactive setup wizard
- Configuration file updates

Author: Muhammad Ali (CodeCelix Internship)
"""

import os
import sys
import zipfile
import urllib.request
import shutil
from pathlib import Path
from typing import Optional, Tuple

# Fix Unicode encoding issues on Windows
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')

try:
    from tqdm import tqdm
except ImportError:
    print("Installing tqdm for progress bars...")
    os.system(f"{sys.executable} -m pip install tqdm")
    from tqdm import tqdm

# ============================================================================
# AVAILABLE VOSK MODELS
# ============================================================================

MODELS = {
    "small-en": {
        "name": "vosk-model-small-en-us-0.15",
        "url": "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip",
        "size": "40 MB",
        "accuracy": "Good",
        "speed": "Very Fast",
        "description": "Small English model - Recommended for voice commands",
        "use_case": "Voice commands, quick responses, low-end hardware",
        "recommended": True
    },
    "large-en": {
        "name": "vosk-model-en-us-0.22",
        "url": "https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip",
        "size": "1.8 GB",
        "accuracy": "Excellent",
        "speed": "Moderate",
        "description": "Large English model - Best accuracy for dictation",
        "use_case": "Dictation, transcription, complex commands",
        "recommended": False
    },
    "urdu": {
        "name": "vosk-model-small-ur-0.3",
        "url": "https://alphacephei.com/vosk/models/vosk-model-small-ur-0.3.zip",
        "size": "45 MB",
        "accuracy": "Good",
        "speed": "Fast",
        "description": "Urdu model - For Roman Urdu support",
        "use_case": "Roman Urdu commands, bilingual support",
        "recommended": False
    },
    "tiny-en": {
        "name": "vosk-model-small-en-us-0.22",
        "url": "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.22.zip",
        "size": "40 MB",
        "accuracy": "Moderate",
        "speed": "Extremely Fast",
        "description": "Tiny English model - For resource-constrained systems",
        "use_case": "Raspberry Pi, old computers, embedded systems",
        "recommended": False
    }
}


class DownloadProgressBar(tqdm):
    """Progress bar for file downloads"""

    def update_to(self, b=1, bsize=1, tsize=None):
        """
        Update progress bar.

        Args:
            b: Number of blocks transferred
            bsize: Size of each block (bytes)
            tsize: Total size (bytes)
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def check_disk_space(required_mb: int) -> bool:
    """
    Check if sufficient disk space available.

    Args:
        required_mb: Required space in megabytes

    Returns:
        True if sufficient space available
    """
    try:
        import shutil
        total, used, free = shutil.disk_usage(os.getcwd())
        free_mb = free // (1024 * 1024)

        if free_mb < required_mb:
            print(f"\n⚠️  Warning: Low disk space")
            print(f"   Required: {required_mb} MB")
            print(f"   Available: {free_mb} MB")
            return False
        return True
    except Exception:
        # If check fails, assume sufficient space
        return True


def download_model(
    model_key: str = "small-en",
    target_dir: str = ".",
    force: bool = False
) -> Tuple[bool, str]:
    """
    Download and extract Vosk model.

    Args:
        model_key: Model identifier (small-en, large-en, urdu, tiny-en)
        target_dir: Directory to extract model
        force: Force re-download if model exists

    Returns:
        (success, model_path) tuple
    """
    if model_key not in MODELS:
        print(f"❌ Unknown model: '{model_key}'")
        print(f"Available models: {', '.join(MODELS.keys())}")
        return False, ""

    model_info = MODELS[model_key]
    model_name = model_info["name"]
    model_url = model_info["url"]

    target_path = Path(target_dir).resolve()
    target_path.mkdir(parents=True, exist_ok=True)

    model_path = target_path / model_name

    # Check if already downloaded
    if model_path.exists() and not force:
        print(f"\n✓ Model already exists at: {model_path}")
        print(f"\n💡 To re-download, use: python vosk_setup.py --force")
        return True, str(model_path)

    # Display model info
    print(f"\n{'=' * 70}")
    print(f"📥 DOWNLOADING: {model_info['description']}")
    print(f"{'=' * 70}")
    print(f"\n📊 Model Details:")
    print(f"   Name: {model_name}")
    print(f"   Size: {model_info['size']}")
    print(f"   Accuracy: {model_info['accuracy']}")
    print(f"   Speed: {model_info['speed']}")
    print(f"   Use Case: {model_info['use_case']}")
    print(f"   URL: {model_url}")
    print()

    # Check disk space (rough estimate: size * 2 for download + extraction)
    size_mb = int(model_info['size'].split()[0])
    if size_mb > 100:
        size_mb = 1800  # Large model
    if not check_disk_space(size_mb * 2):
        print("\n❌ Insufficient disk space. Please free up space and try again.")
        return False, ""

    zip_path = target_path / f"{model_name}.zip"

    try:
        # Download with progress bar
        print("📥 Downloading model (this may take a few minutes)...")

        with DownloadProgressBar(
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            miniters=1,
            desc=model_name
        ) as progress_bar:
            urllib.request.urlretrieve(
                model_url,
                zip_path,
                reporthook=progress_bar.update_to
            )

        print(f"\n✓ Downloaded to: {zip_path}")

        # Verify download
        if not zip_path.exists() or zip_path.stat().st_size < 1000:
            raise Exception("Download failed or file corrupted")

        # Extract
        print(f"\n📦 Extracting model (please wait)...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Show extraction progress
            members = zip_ref.namelist()
            for i, member in enumerate(members, 1):
                zip_ref.extract(member, target_path)
                if i % 100 == 0:
                    print(f"   Extracted {i}/{len(members)} files...")

        print(f"✓ Extracted {len(members)} files")

        # Clean up zip file
        print(f"\n🗑️  Cleaning up download...")
        zip_path.unlink()

        # Verify extraction
        if not model_path.exists():
            raise Exception(f"Model directory not found after extraction: {model_path}")

        print(f"\n{'=' * 70}")
        print(f"✅ MODEL READY!")
        print(f"{'=' * 70}")
        print(f"\n📂 Model location: {model_path}")
        print(f"\n💡 Configuration:")
        print(f'   Add to config.py: VOSK_MODEL_PATH = "{model_name}"')

        return True, str(model_path)

    except urllib.error.URLError as e:
        print(f"\n❌ Download failed: {e}")
        print(f"\n💡 Check your internet connection and try again")
        print(f"   Or download manually from: {model_url}")

        # Clean up partial downloads
        if zip_path.exists():
            zip_path.unlink()

        return False, ""

    except zipfile.BadZipFile:
        print(f"\n❌ Downloaded file is corrupted")
        print(f"   Please try again or download manually from: {model_url}")

        if zip_path.exists():
            zip_path.unlink()

        return False, ""

    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        print(f"\n💡 Manual setup:")
        print(f"   1. Download from: {model_url}")
        print(f"   2. Extract to: {target_path}")
        print(f"   3. Verify folder name: {model_name}")

        # Clean up
        if zip_path.exists():
            zip_path.unlink()

        return False, ""


def update_config_file(model_path: str) -> bool:
    """
    Update config.py with model path.

    Args:
        model_path: Path to Vosk model

    Returns:
        True if updated successfully
    """
    config_file = Path("config.py")

    if not config_file.exists():
        print(f"\n⚠️  config.py not found - skipping auto-update")
        return False

    try:
        # Read current config
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if VOSK_MODEL_PATH already exists
        if "VOSK_MODEL_PATH" in content:
            print(f"\n✓ config.py already has VOSK_MODEL_PATH")
            return True

        # Add Vosk configuration
        vosk_config = f'''

# ============================================================================
# VOSK AUDIO CONFIGURATION (Offline Speech Recognition)
# ============================================================================

# Path to Vosk model directory
VOSK_MODEL_PATH = "{Path(model_path).name}"

# Audio settings for Vosk
SAMPLE_RATE = 16000  # 16kHz recommended for speech
AUDIO_CHANNELS = 1   # Mono audio
PHRASE_TIME_LIMIT = 10  # Maximum seconds for a command
LISTEN_TIMEOUT = 5   # Seconds to wait for speech

# Audio device (None = default)
AUDIO_DEVICE_INDEX = None

'''

        # Append to config
        with open(config_file, 'a', encoding='utf-8') as f:
            f.write(vosk_config)

        print(f"\n✓ Updated config.py with Vosk settings")
        return True

    except Exception as e:
        print(f"\n⚠️  Could not update config.py: {e}")
        print(f"   Please add manually:")
        print(f'   VOSK_MODEL_PATH = "{Path(model_path).name}"')
        return False


def interactive_setup():
    """Interactive setup wizard"""
    print("\n" + "=" * 70)
    print("🎙️  GIDEON VOSK MODEL SETUP WIZARD")
    print("=" * 70)
    print("\nThis wizard will download and configure a Vosk model for")
    print("offline speech recognition in Gideon.")
    print("\nVosk Benefits:")
    print("  ✓ 100% Offline - No internet required for recognition")
    print("  ✓ No DLL Issues - Pure Python, works everywhere")
    print("  ✓ Fast & Accurate - Production-ready performance")
    print("  ✓ Privacy-Focused - All processing happens locally")
    print("\n" + "-" * 70)

    # Display available models
    print("\n📦 Available Models:\n")

    for i, (key, info) in enumerate(MODELS.items(), 1):
        marker = "★ RECOMMENDED" if info.get("recommended") else ""
        print(f"[{i}] {key:12} - {info['description']} {marker}")
        print(f"    Size: {info['size']:8} | Accuracy: {info['accuracy']:10} | Speed: {info['speed']}")
        print(f"    Use Case: {info['use_case']}")
        print()

    print("-" * 70)
    print("\n💡 Recommendations:")
    print("   • For Gideon voice commands → small-en (default)")
    print("   • For accurate dictation → large-en")
    print("   • For Roman Urdu support → urdu")
    print("   • For low-end hardware → tiny-en")

    # Get user choice
    print("\n" + "-" * 70)
    choice_input = input("\nEnter model number or key (press Enter for small-en): ").strip()

    if not choice_input:
        model_key = "small-en"
    elif choice_input.isdigit():
        model_keys = list(MODELS.keys())
        idx = int(choice_input) - 1
        if 0 <= idx < len(model_keys):
            model_key = model_keys[idx]
        else:
            print(f"❌ Invalid choice. Using default: small-en")
            model_key = "small-en"
    elif choice_input in MODELS:
        model_key = choice_input
    else:
        print(f"❌ Invalid choice. Using default: small-en")
        model_key = "small-en"

    print(f"\n✓ Selected: {model_key}")

    # Confirm download
    model_info = MODELS[model_key]
    print(f"\nAbout to download: {model_info['size']}")

    confirm = input("Proceed with download? (Y/n): ").strip().lower()
    if confirm and confirm != 'y':
        print("\n❌ Setup cancelled")
        return False

    # Download model
    success, model_path = download_model(model_key)

    if success:
        # Update config
        update_config_file(model_path)

        print(f"\n" + "=" * 70)
        print("✅ SETUP COMPLETE!")
        print("=" * 70)
        print(f"\n🎯 Next Steps:")
        print(f"\n1. Test the setup:")
        print(f"   python -c \"from audio_handler import VoskAudioHandler; VoskAudioHandler().test_microphone()\"")
        print(f"\n2. Run Gideon:")
        print(f"   python gideon.py")
        print(f"\n3. If you encounter issues:")
        print(f"   python audio_handler.py  # Run diagnostics")
        print(f"\n" + "=" * 70)

        return True
    else:
        print(f"\n❌ Setup failed. Please try again or follow manual instructions.")
        return False


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Download and setup Vosk models for Gideon",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python vosk_setup.py                    # Interactive setup
  python vosk_setup.py --model small-en   # Download specific model
  python vosk_setup.py --list             # List available models
  python vosk_setup.py --force            # Re-download model
        """
    )

    parser.add_argument(
        '--model',
        choices=list(MODELS.keys()),
        help='Model to download'
    )

    parser.add_argument(
        '--list',
        action='store_true',
        help='List available models and exit'
    )

    parser.add_argument(
        '--force',
        action='store_true',
        help='Force re-download even if model exists'
    )

    parser.add_argument(
        '--dir',
        default='.',
        help='Target directory for model (default: current directory)'
    )

    args = parser.parse_args()

    # List models
    if args.list:
        print("\nAvailable Vosk Models:")
        print("=" * 70)
        for key, info in MODELS.items():
            print(f"\n{key}:")
            for k, v in info.items():
                if k != 'url':
                    print(f"  {k:15}: {v}")
        print("\n" + "=" * 70)
        return

    # Download specific model
    if args.model:
        success, _ = download_model(args.model, args.dir, args.force)
        sys.exit(0 if success else 1)

    # Interactive setup
    try:
        success = interactive_setup()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
