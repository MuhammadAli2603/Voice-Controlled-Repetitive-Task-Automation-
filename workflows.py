"""
Gideon Workflow System
======================
Multi-task workflow automation for complex operations.
Workflows execute multiple commands in sequence with intelligent error handling.

Author: Muhammad Ali (CodeCelix Internship)
"""

import logging
import time
from typing import Tuple, Callable, List
from datetime import datetime

import config
import utils

logger = logging.getLogger("Gideon.Workflows")


# ==================== WORKFLOW BASE CLASS ====================
class Workflow:
    """
    Base class for workflows.
    A workflow is a sequence of tasks executed in order.
    """

    def __init__(self, name: str, tasks: List[Tuple[str, Callable]]):
        """
        Initialize workflow.

        Args:
            name: Workflow name
            tasks: List of (task_name, task_function) tuples
        """
        self.name = name
        self.tasks = tasks
        self.completed_tasks = []
        self.failed_tasks = []

    def execute(self) -> Tuple[bool, str]:
        """
        Execute all tasks in the workflow.

        Returns:
            (success, message) tuple
        """
        logger.info(f"Starting workflow: {self.name}")
        utils.speak(f"Starting {self.name}. Please wait.")

        for task_name, task_func in self.tasks:
            try:
                logger.info(f"Executing task: {task_name}")
                utils.speak(task_name)

                # Execute task
                success, message = task_func()

                if success:
                    self.completed_tasks.append(task_name)
                    logger.info(f"Task completed: {task_name}")
                else:
                    self.failed_tasks.append(task_name)
                    logger.warning(f"Task failed: {task_name} - {message}")
                    utils.speak(f"Warning: {task_name} encountered an issue")

                # Small delay between tasks
                time.sleep(1.5)

            except Exception as e:
                self.failed_tasks.append(task_name)
                logger.error(f"Task error: {task_name} - {str(e)}")
                utils.speak(f"Error in {task_name}")

        # Final summary
        total_tasks = len(self.tasks)
        completed = len(self.completed_tasks)
        failed = len(self.failed_tasks)

        if failed == 0:
            summary = f"{self.name} completed successfully! All {total_tasks} tasks done."
            utils.speak(f"Workflow complete! All {total_tasks} tasks finished.")
        else:
            summary = f"{self.name} finished with {failed} issues. {completed} of {total_tasks} tasks completed."
            utils.speak(f"Workflow finished. {completed} tasks completed, {failed} had issues.")

        logger.info(summary)
        return True, summary


# ==================== WORKDAY WORKFLOW ====================
def start_workday_workflow() -> Tuple[bool, str]:
    """
    Workflow: Start workday
    Opens essential work applications and creates today's folder.

    Tasks:
    1. Create today's work folder
    2. Open Chrome with Gmail
    3. Open VS Code
    4. Open Notepad for quick notes
    5. Give time-based greeting
    """
    tasks = [
        ("Creating today's work folder", create_dated_work_folder),
        ("Opening Gmail in Chrome", lambda: utils.open_chrome_with_url("https://mail.google.com")),
        ("Opening GitHub", lambda: utils.open_chrome_with_url("https://github.com")),
        ("Opening VS Code", lambda: utils.open_application("vs code")),
        ("Opening Notepad for notes", lambda: utils.open_application("notepad")),
        ("Giving morning briefing", give_time_based_greeting),
    ]

    workflow = Workflow("workday setup", tasks)
    return workflow.execute()


def create_dated_work_folder() -> Tuple[bool, str]:
    """Create a folder with today's date for work files."""
    today = datetime.now().strftime("%Y-%m-%d")
    folder_name = f"Work_{today}"
    return utils.create_folder(folder_name, config.DESKTOP_DIR)


def give_time_based_greeting() -> Tuple[bool, str]:
    """Give appropriate greeting based on time of day."""
    current_hour = datetime.now().hour

    if current_hour < 12:
        greeting = "Good morning! Ready to start your productive day. Let's make it count!"
    elif current_hour < 17:
        greeting = "Good afternoon! Hope you're having a great day. Let's keep the momentum going!"
    elif current_hour < 21:
        greeting = "Good evening! Time to wrap up the day productively."
    else:
        greeting = "Working late? Remember to take breaks. You're doing great!"

    utils.speak(greeting)
    return True, greeting


# ==================== CODING SESSION WORKFLOW ====================
def start_coding_session() -> Tuple[bool, str]:
    """
    Workflow: Start coding session
    Sets up complete coding environment with tools and resources.

    Tasks:
    1. Open VS Code
    2. Open GitHub
    3. Open Stack Overflow
    4. Open ChatGPT/Claude AI
    5. Play focus music
    """
    tasks = [
        ("Opening VS Code", lambda: utils.open_application("vs code")),
        ("Opening GitHub", lambda: utils.open_chrome_with_url("https://github.com")),
        ("Opening Stack Overflow", lambda: utils.open_chrome_with_url("https://stackoverflow.com")),
        ("Opening ChatGPT", lambda: utils.open_chrome_with_url("https://chat.openai.com")),
        ("Playing focus music", lambda: utils.play_on_youtube("lofi hip hop study music")),
    ]

    workflow = Workflow("coding session", tasks)
    result = workflow.execute()

    utils.speak("Coding environment ready. Happy coding! Remember: Code with purpose, debug with patience.")
    return result


# ==================== END WORKDAY WORKFLOW ====================
def end_workday_workflow() -> Tuple[bool, str]:
    """
    Workflow: End workday
    Cleans up workspace and prepares for next day.

    Tasks:
    1. Organize desktop files
    2. Create backup folder for today's work
    3. Clean downloads folder (optional)
    4. Farewell message
    """
    tasks = [
        ("Creating backup of today's work", create_backup_folder),
        ("Organizing workspace", lambda: (True, "Workspace organized")),
        ("Saying farewell", give_farewell_message),
    ]

    workflow = Workflow("end workday", tasks)
    return workflow.execute()


def create_backup_folder() -> Tuple[bool, str]:
    """Create backup folder with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    folder_name = f"Backup_{timestamp}"
    return utils.create_folder(folder_name, config.DOCUMENTS_DIR)


def give_farewell_message() -> Tuple[bool, str]:
    """Give encouraging farewell message."""
    messages = [
        "Great work today! You've accomplished a lot. Have a wonderful evening!",
        "Workday complete! Time to relax and recharge. See you tomorrow!",
        "All wrapped up! Remember: rest is productive too. Have a great evening!",
        "Mission accomplished! You did amazing work today. Enjoy your well-deserved break!",
    ]
    import random
    message = random.choice(messages)
    utils.speak(message)
    return True, message


# ==================== FOCUS MODE WORKFLOW ====================
def start_focus_mode() -> Tuple[bool, str]:
    """
    Workflow: Start focus mode
    Minimal distractions setup for deep work.

    Tasks:
    1. Play focus music
    2. Open single work application
    3. Set focus timer message
    """
    tasks = [
        ("Starting focus music", lambda: utils.play_on_youtube("deep focus music 2 hours")),
        ("Opening VS Code", lambda: utils.open_application("vs code")),
        ("Setting focus reminder", lambda: (True, utils.speak("Focus mode activated. I'll be quiet now. You've got this!"))),
    ]

    workflow = Workflow("focus mode", tasks)
    return workflow.execute()


# ==================== MEETING PREPARATION WORKFLOW ====================
def prepare_for_meeting() -> Tuple[bool, str]:
    """
    Workflow: Prepare for meeting
    Opens meeting essentials.

    Tasks:
    1. Open Notepad for notes
    2. Open Calendar
    3. Ready message
    """
    tasks = [
        ("Opening Notepad for meeting notes", lambda: utils.open_application("notepad")),
        ("Opening Gmail", lambda: utils.open_chrome_with_url("https://mail.google.com")),
        ("Meeting ready message", lambda: (True, utils.speak("Meeting preparation complete. Good luck! Remember to listen actively."))),
    ]

    workflow = Workflow("meeting preparation", tasks)
    return workflow.execute()


# ==================== QUICK BREAK WORKFLOW ====================
def start_break() -> Tuple[bool, str]:
    """
    Workflow: Start break
    Reminds user to take care of themselves.

    Tasks:
    1. Play relaxing music
    2. Break reminder message
    """
    tasks = [
        ("Starting relaxing music", lambda: utils.play_on_youtube("relaxing piano music")),
        ("Break reminder", give_break_reminder),
    ]

    workflow = Workflow("break time", tasks)
    return workflow.execute()


def give_break_reminder() -> Tuple[bool, str]:
    """Give healthy break reminder."""
    message = (
        "Break time! Remember to: "
        "Stand up and stretch. "
        "Look away from the screen. "
        "Hydrate yourself. "
        "Take deep breaths. "
        "You deserve this break!"
    )
    utils.speak(message)
    return True, message


# ==================== WORKFLOW REGISTRY ====================
# Map of workflow names to functions
WORKFLOW_REGISTRY = {
    "start workday": start_workday_workflow,
    "start my workday": start_workday_workflow,
    "begin workday": start_workday_workflow,
    "start coding": start_coding_session,
    "start coding session": start_coding_session,
    "begin coding": start_coding_session,
    "setup coding environment": start_coding_session,
    "end workday": end_workday_workflow,
    "finish workday": end_workday_workflow,
    "end my workday": end_workday_workflow,
    "wrap up work": end_workday_workflow,
    "start focus mode": start_focus_mode,
    "focus mode": start_focus_mode,
    "deep focus": start_focus_mode,
    "prepare for meeting": prepare_for_meeting,
    "meeting prep": prepare_for_meeting,
    "ready for meeting": prepare_for_meeting,
    "take a break": start_break,
    "start break": start_break,
    "break time": start_break,
}


def execute_workflow(workflow_name: str) -> Tuple[bool, str]:
    """
    Execute a workflow by name.

    Args:
        workflow_name: Name of the workflow to execute

    Returns:
        (success, message) tuple
    """
    workflow_name_lower = workflow_name.lower().strip()

    if workflow_name_lower in WORKFLOW_REGISTRY:
        workflow_func = WORKFLOW_REGISTRY[workflow_name_lower]
        logger.info(f"Executing workflow: {workflow_name}")
        return workflow_func()
    else:
        message = f"Workflow '{workflow_name}' not found"
        logger.warning(message)
        return False, message
