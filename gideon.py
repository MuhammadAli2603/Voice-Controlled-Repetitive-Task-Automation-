"""
Gideon - Voice-Controlled Task Automation System
================================================
Main entry point for the Gideon voice assistant.
Named after the AI from The Flash - always ready to assist.

This system runs in an infinite loop, continuously listening for voice commands
and only shutting down when explicitly told to do so.

Author: Muhammad Ali (CodeCelix Internship)
Project: AI Engineer Intern - CodeCelix
Version: 1.0.0
"""

import logging
import sys
from typing import Optional

# Fix Unicode encoding issues on Windows
if sys.platform == 'win32':
    import os
    os.system('chcp 65001 > nul')
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')

import config
import utils
import commands
import scheduler
import multilingual
from audio_handler import VoskAudioHandler

# Initialize logger
logger: Optional[logging.Logger] = None

# Global audio handler
audio_handler: Optional[VoskAudioHandler] = None


def initialize_system() -> bool:
    """
    Initialize all Gideon systems and verify functionality.

    Returns:
        True if initialization successful, False otherwise
    """
    global logger, audio_handler

    try:
        # Display startup banner
        utils.display_startup_banner()

        # Setup logging
        logger = utils.setup_logging()
        logger.info("Starting Gideon initialization sequence...")

        # Initialize Vosk audio handler
        print("\n[1/5] Loading Vosk offline speech recognition...")
        try:
            audio_handler = VoskAudioHandler(
                model_path=config.VOSK_MODEL_PATH,
                sample_rate=config.SAMPLE_RATE,
                device=config.AUDIO_DEVICE_INDEX
            )
            print("✓ Vosk audio handler initialized (offline mode)")
            logger.info("Vosk audio handler loaded successfully")
        except FileNotFoundError as e:
            print("❌ ERROR: Vosk model not found!")
            print("\n📥 Please download the Vosk model:")
            print("   python vosk_setup.py")
            print("\nOr download manually from:")
            print("   https://alphacephei.com/vosk/models")
            logger.error(f"Vosk model not found: {e}")
            return False
        except Exception as e:
            print(f"❌ ERROR: Failed to initialize Vosk: {e}")
            logger.error(f"Vosk initialization failed: {e}")
            return False

        # Validate microphone access
        print("\n[2/5] Checking microphone access...")
        if not utils.validate_microphone():
            print("❌ ERROR: Cannot access microphone!")
            print("Please check:")
            print("  - Microphone is connected")
            print("  - Microphone permissions are granted")
            print("  - No other application is using the microphone")
            return False
        print("✓ Microphone access confirmed")
        logger.info("Microphone validation successful")

        # Initialize text-to-speech engine
        print("\n[3/5] Initializing text-to-speech engine...")
        try:
            utils.initialize_tts()
            print("✓ Text-to-speech engine ready")
            logger.info("TTS engine initialized")
        except Exception as e:
            print(f"❌ ERROR: TTS initialization failed: {e}")
            return False

        # Load command registry
        print("\n[4/5] Loading command registry...")
        total_commands = len(commands.COMMAND_REGISTRY)
        print(f"✓ Loaded {total_commands} command patterns")
        logger.info(f"Command registry loaded with {total_commands} patterns")

        # Initialize task scheduler
        print("\n[5/5] Starting task scheduler...")
        task_scheduler = scheduler.get_scheduler()
        print("✓ Task scheduler ready")
        logger.info("Task scheduler initialized and started")

        # System ready
        print("\n✅ All systems operational\n")
        logger.info("Gideon initialization complete")

        return True

    except Exception as e:
        print(f"\n❌ CRITICAL ERROR during initialization: {e}")
        if logger:
            logger.critical(f"Initialization failed: {e}")
        return False


def startup_greeting() -> None:
    """
    Gideon introduces itself and greets the user.
    """
    print("=" * 60)
    print(f"{config.ASSISTANT_NAME} is now online!")
    print("=" * 60)

    # Speak greeting
    utils.speak(config.GREETING_MESSAGE)

    # Provide usage hint
    time_greeting = utils.get_time_based_greeting()
    utils.speak(f"{time_greeting}!")

    print(f"\n💡 TIP: Say 'help' to see what I can do")
    print(f"🛑 To stop me, say: 'shutdown gideon'\n")
    print("-" * 60)
    logger.info("Startup greeting completed")


def main_loop() -> None:
    """
    Main infinite listening loop.
    Gideon continuously listens for commands until shutdown is triggered.

    This is the CORE of Gideon - it never exits unless explicitly told to.
    """
    logger.info("Entering main command loop")
    print("\n🎤 Listening for commands...\n")

    command_count = 0

    while True:  # ← INFINITE LOOP - Gideon always listens
        try:
            # Listen for voice command
            command = utils.listen_with_retry()

            # Handle no input (timeout or silence)
            if command is None:
                continue  # Keep listening

            command_count += 1
            logger.info(f"[Command #{command_count}] Received: {command}")

            # Process multilingual command (translate if needed)
            english_command, metadata = multilingual.process_multilingual_command(command)

            # Display command
            if metadata['was_translated'] == 'True':
                print(f"\n🗣️  You said: \"{command}\" → \"{english_command}\"")
                utils.speak("Samajh gaya")  # "I understood" in Urdu
            else:
                print(f"\n🗣️  You said: \"{command}\"")

            # Check for shutdown command FIRST (highest priority)
            # Check both original and translated command
            if utils.check_for_shutdown(command) or utils.check_for_shutdown(english_command):
                logger.info("Shutdown command received")
                print("\n" + "=" * 60)
                print("SHUTDOWN INITIATED")
                print("=" * 60)
                commands.cmd_shutdown()
                break  # ← ONLY exit point of the loop

            # Execute the command (use translated English command)
            success, message = commands.execute_command(english_command)

            # Log result
            if success:
                logger.info(f"Command executed successfully: {message}")
                print(f"✓ {message}")
            else:
                logger.warning(f"Command failed: {message}")
                print(f"⚠ {message}")

            # Brief separator for readability
            print("-" * 60)

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            logger.info("Keyboard interrupt received")
            print("\n\n⚠️  Keyboard interrupt detected")
            print("To properly shutdown Gideon, please say: 'shutdown gideon'")
            utils.speak("Please say shutdown gideon to stop me properly")
            continue  # Don't exit - keep listening

        except Exception as e:
            # Handle any unexpected errors without crashing
            logger.error(f"Unexpected error in main loop: {e}", exc_info=True)
            print(f"\n❌ ERROR: {e}")
            utils.speak("I encountered an error, but I'm still running. Please try again.")
            continue  # Keep the loop running even on errors

    # This point is only reached after shutdown command
    logger.info(f"Gideon shutting down. Total commands processed: {command_count}")
    print(f"\n📊 Session Statistics:")
    print(f"   Commands processed: {command_count}")
    print(f"\nThank you for using {config.ASSISTANT_NAME}!")
    print("=" * 60)


def main() -> int:
    """
    Main entry point for Gideon.

    Returns:
        Exit code (0 = success, 1 = failure)
    """
    try:
        # Initialize all systems
        if not initialize_system():
            print("\n❌ Initialization failed. Cannot start Gideon.")
            return 1

        # Greet the user
        startup_greeting()

        # Enter main listening loop (runs until shutdown command)
        main_loop()

        # Clean exit
        return 0

    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        if logger:
            logger.critical(f"Fatal error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    """
    Entry point when script is run directly.
    """
    print("\n" + "=" * 60)
    print(f"Starting {config.ASSISTANT_NAME} v{config.VERSION}")
    print(f"Developer: {config.DEVELOPER} @ {config.ORGANIZATION}")
    print("=" * 60 + "\n")

    # Run Gideon
    exit_code = main()

    # Exit with appropriate code
    sys.exit(exit_code)
