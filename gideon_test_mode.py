"""
Gideon Test Mode
================
Run Gideon without microphone for testing features.
Use text input instead of voice commands.
"""

import logging
import sys
from typing import Optional

import config
import utils
import commands
import scheduler
import multilingual

logger: Optional[logging.Logger] = None


def initialize_system_test_mode() -> bool:
    """Initialize Gideon in test mode (no microphone required)."""
    global logger

    try:
        utils.display_startup_banner()
        logger = utils.setup_logging()
        logger.info("Starting Gideon in TEST MODE (no microphone)")

        print("\n[TEST MODE] Skipping microphone check...")
        print("✓ Test mode active")

        print("\n[2/4] Initializing text-to-speech engine...")
        try:
            utils.initialize_tts()
            print("✓ Text-to-speech engine ready")
            logger.info("TTS engine initialized")
        except Exception as e:
            print(f"⚠ TTS not available: {e}")
            logger.warning(f"TTS initialization failed: {e}")

        print("\n[3/4] Loading command registry...")
        total_commands = len(commands.COMMAND_REGISTRY)
        print(f"✓ Loaded {total_commands} command patterns")
        logger.info(f"Command registry loaded with {total_commands} patterns")

        print("\n[4/4] Starting task scheduler...")
        task_scheduler = scheduler.get_scheduler()
        print("✓ Task scheduler ready")
        logger.info("Task scheduler initialized")

        print("\n✓ All systems operational (TEST MODE)\n")
        logger.info("Gideon test mode initialization complete")

        return True

    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {e}")
        if logger:
            logger.critical(f"Initialization failed: {e}")
        return False


def test_mode_loop():
    """Main loop using text input instead of voice."""
    print("\n" + "=" * 60)
    print("GIDEON TEST MODE")
    print("=" * 60)
    print("\nType commands instead of speaking them.")
    print("Try these commands:")
    print("  - help")
    print("  - chrome kholo (Roman Urdu)")
    print("  - list scheduled tasks")
    print("  - show urdu commands")
    print("  - quit")
    print("\n" + "-" * 60 + "\n")

    command_count = 0

    while True:
        try:
            # Get text input instead of voice
            command = input("Gideon> ").strip()

            if not command:
                continue

            command_count += 1
            logger.info(f"[Command #{command_count}] Text input: {command}")

            # Process multilingual command
            english_command, metadata = multilingual.process_multilingual_command(command)

            # Display translation if needed
            if metadata['was_translated'] == 'True':
                print(f"[Translation] '{command}' → '{english_command}'")

            # Check for shutdown
            if utils.check_for_shutdown(command) or utils.check_for_shutdown(english_command):
                logger.info("Shutdown command received")
                print("\n" + "=" * 60)
                print("SHUTDOWN INITIATED")
                print("=" * 60)
                print("\n✓ Goodbye!\n")
                break

            # Execute command
            success, message = commands.execute_command(english_command)

            # Display result
            if success:
                logger.info(f"Command executed: {message}")
                print(f"✓ {message}")
            else:
                logger.warning(f"Command failed: {message}")
                print(f"⚠ {message}")

            print()

        except KeyboardInterrupt:
            print("\n\nUse 'quit' command to exit properly.")
            continue

        except EOFError:
            print("\n\nExiting...")
            break

        except Exception as e:
            logger.error(f"Error in test loop: {e}", exc_info=True)
            print(f"\n❌ ERROR: {e}\n")
            continue

    # Statistics
    logger.info(f"Test mode session ended. Commands: {command_count}")
    print(f"\n📊 Session Statistics:")
    print(f"   Commands processed: {command_count}")
    print(f"\nThank you for testing {config.ASSISTANT_NAME}!")


def main() -> int:
    """Main entry point for test mode."""
    try:
        if not initialize_system_test_mode():
            print("\n❌ Initialization failed.")
            return 1

        print("\n💡 TEST MODE: Use text input instead of voice")
        print("   (Microphone not required)\n")

        test_mode_loop()
        return 0

    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        if logger:
            logger.critical(f"Fatal error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print(f"Starting {config.ASSISTANT_NAME} v{config.VERSION} - TEST MODE")
    print(f"Developer: {config.DEVELOPER} @ {config.ORGANIZATION}")
    print("=" * 60 + "\n")

    exit_code = main()
    sys.exit(exit_code)
