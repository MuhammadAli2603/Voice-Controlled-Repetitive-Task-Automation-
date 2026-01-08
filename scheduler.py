"""
Gideon Task Scheduler
=====================
Production-ready task scheduling system for Gideon.
Allows scheduling voice commands and workflows for specific times.

Features:
- Schedule tasks for specific times
- Recurring daily tasks
- List and manage scheduled tasks
- Background execution thread
- Persistent storage (optional)

Author: Muhammad Ali (CodeCelix Internship)
"""

import logging
import threading
import time
import re
from datetime import datetime, time as dt_time
from typing import Callable, Optional, List, Dict, Tuple
import json
from pathlib import Path

import config

logger = logging.getLogger("Gideon.Scheduler")


class ScheduledTask:
    """
    Represents a scheduled task with execution details.
    """

    def __init__(
        self,
        task_id: str,
        name: str,
        time_str: str,
        task_func: Callable,
        description: str = "",
        recurring: bool = True
    ):
        """
        Initialize a scheduled task.

        Args:
            task_id: Unique identifier for the task
            name: Human-readable task name
            time_str: Time in HH:MM format (24-hour)
            task_func: Function to execute
            description: Optional task description
            recurring: Whether task repeats daily
        """
        self.task_id = task_id
        self.name = name
        self.time_str = time_str
        self.task_func = task_func
        self.description = description
        self.recurring = recurring
        self.last_executed: Optional[datetime] = None
        self.execution_count = 0

        # Parse time
        hour, minute = map(int, time_str.split(':'))
        self.scheduled_time = dt_time(hour, minute)

    def should_execute_now(self) -> bool:
        """
        Check if task should execute at current time.

        Returns:
            True if task should run now
        """
        now = datetime.now()
        current_time = now.time()

        # Check if it's the scheduled time (within 1-minute window)
        is_scheduled_time = (
            current_time.hour == self.scheduled_time.hour and
            current_time.minute == self.scheduled_time.minute
        )

        if not is_scheduled_time:
            return False

        # Check if already executed today
        if self.last_executed:
            if self.last_executed.date() == now.date():
                return False  # Already executed today

        return True

    def execute(self) -> Tuple[bool, str]:
        """
        Execute the scheduled task.

        Returns:
            (success, message) tuple
        """
        try:
            logger.info(f"Executing scheduled task: {self.name}")

            # Execute the task function
            success, message = self.task_func()

            # Update execution tracking
            self.last_executed = datetime.now()
            self.execution_count += 1

            logger.info(f"Task executed successfully: {self.name} (count: {self.execution_count})")
            return success, message

        except Exception as e:
            error_msg = f"Error executing task '{self.name}': {str(e)}"
            logger.error(error_msg)
            return False, error_msg

    def to_dict(self) -> Dict:
        """Convert task to dictionary for storage"""
        return {
            "task_id": self.task_id,
            "name": self.name,
            "time": self.time_str,
            "description": self.description,
            "recurring": self.recurring,
            "execution_count": self.execution_count
        }


class TaskScheduler:
    """
    Production-ready task scheduler with background execution.
    Runs scheduled tasks at specified times.
    """

    def __init__(self, storage_file: Optional[Path] = None):
        """
        Initialize the task scheduler.

        Args:
            storage_file: Optional file path for persistent storage
        """
        self.tasks: Dict[str, ScheduledTask] = {}
        self.is_running = False
        self.scheduler_thread: Optional[threading.Thread] = None
        self.storage_file = storage_file or (config.LOGS_DIR / "scheduled_tasks.json")

        logger.info("Task scheduler initialized")

    def schedule_task(
        self,
        name: str,
        time_str: str,
        task_func: Callable,
        description: str = "",
        recurring: bool = True
    ) -> Tuple[bool, str]:
        """
        Schedule a task for specific time.

        Args:
            name: Human-readable task name
            time_str: Time in format "HH:MM" (24-hour)
            task_func: Function to execute
            description: Optional task description
            recurring: Whether task repeats daily (default: True)

        Returns:
            (success, message) tuple
        """
        try:
            # Validate time format
            if not self._validate_time_format(time_str):
                return False, f"Invalid time format: {time_str}. Use HH:MM (24-hour format)"

            # Generate unique task ID
            task_id = f"task_{int(time.time())}_{len(self.tasks)}"

            # Create scheduled task
            task = ScheduledTask(
                task_id=task_id,
                name=name,
                time_str=time_str,
                task_func=task_func,
                description=description,
                recurring=recurring
            )

            # Add to tasks dictionary
            self.tasks[task_id] = task

            # Save to storage
            self._save_tasks()

            message = f"Task '{name}' scheduled for {time_str}"
            logger.info(message)
            return True, message

        except Exception as e:
            error_msg = f"Error scheduling task: {str(e)}"
            logger.error(error_msg)
            return False, error_msg

    def _validate_time_format(self, time_str: str) -> bool:
        """Validate time string format (HH:MM)"""
        try:
            hour, minute = map(int, time_str.split(':'))
            return 0 <= hour <= 23 and 0 <= minute <= 59
        except:
            return False

    def remove_task(self, task_id: str) -> Tuple[bool, str]:
        """
        Remove a scheduled task.

        Args:
            task_id: ID of task to remove

        Returns:
            (success, message) tuple
        """
        if task_id in self.tasks:
            task_name = self.tasks[task_id].name
            del self.tasks[task_id]
            self._save_tasks()

            message = f"Removed task: {task_name}"
            logger.info(message)
            return True, message
        else:
            return False, f"Task not found: {task_id}"

    def list_tasks(self) -> List[Dict]:
        """
        Get list of all scheduled tasks.

        Returns:
            List of task dictionaries
        """
        return [task.to_dict() for task in self.tasks.values()]

    def clear_all_tasks(self) -> Tuple[bool, str]:
        """
        Clear all scheduled tasks.

        Returns:
            (success, message) tuple
        """
        count = len(self.tasks)
        self.tasks.clear()
        self._save_tasks()

        message = f"Cleared {count} scheduled tasks"
        logger.info(message)
        return True, message

    def start(self) -> None:
        """Start the scheduler background thread"""
        if self.is_running:
            logger.warning("Scheduler already running")
            return

        self.is_running = True
        self.scheduler_thread = threading.Thread(
            target=self._run_scheduler,
            daemon=True,
            name="GideonScheduler"
        )
        self.scheduler_thread.start()
        logger.info("Scheduler started")

    def stop(self) -> None:
        """Stop the scheduler background thread"""
        self.is_running = False
        if self.scheduler_thread:
            self.scheduler_thread.join(timeout=2)
        logger.info("Scheduler stopped")

    def _run_scheduler(self) -> None:
        """
        Main scheduler loop - runs in background thread.
        Checks every 30 seconds for tasks to execute.
        """
        logger.info("Scheduler thread started")

        while self.is_running:
            try:
                # Check each task
                for task in list(self.tasks.values()):
                    if task.should_execute_now():
                        logger.info(f"Executing scheduled task: {task.name}")
                        task.execute()

                # Sleep for 30 seconds before next check
                time.sleep(30)

            except Exception as e:
                logger.error(f"Error in scheduler loop: {e}")
                time.sleep(30)  # Continue even on errors

        logger.info("Scheduler thread stopped")

    def _save_tasks(self) -> None:
        """Save tasks to persistent storage (without function references)"""
        try:
            # Create simplified task data (without function references)
            task_data = []
            for task in self.tasks.values():
                task_data.append({
                    "task_id": task.task_id,
                    "name": task.name,
                    "time": task.time_str,
                    "description": task.description,
                    "recurring": task.recurring,
                    "execution_count": task.execution_count
                })

            # Save to file
            with open(self.storage_file, 'w') as f:
                json.dump(task_data, f, indent=2)

            logger.debug(f"Tasks saved to {self.storage_file}")

        except Exception as e:
            logger.error(f"Error saving tasks: {e}")


# Global scheduler instance
_global_scheduler: Optional[TaskScheduler] = None


def get_scheduler() -> TaskScheduler:
    """
    Get the global scheduler instance (singleton pattern).

    Returns:
        Global TaskScheduler instance
    """
    global _global_scheduler

    if _global_scheduler is None:
        _global_scheduler = TaskScheduler()
        _global_scheduler.start()

    return _global_scheduler


def parse_schedule_command(command: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Parse scheduling commands from natural language.

    Examples:
        "at 10 AM open project folder" -> ("10:00", "open project folder")
        "at 2 PM play music" -> ("14:00", "play music")
        "schedule reminder at 3:30 PM" -> ("15:30", "reminder")

    Args:
        command: Voice command string

    Returns:
        (time_str, task_description) tuple or (None, None) if parsing fails
    """
    command_lower = command.lower()

    # Pattern: "at HH:MM? AM/PM? [task]"
    time_pattern = r'at\s+(\d{1,2})(?::(\d{2}))?\s*(am|pm)?'
    match = re.search(time_pattern, command_lower)

    if not match:
        return None, None

    try:
        hour = int(match.group(1))
        minute = int(match.group(2)) if match.group(2) else 0
        period = match.group(3)

        # Convert to 24-hour format
        if period:
            if period == 'pm' and hour != 12:
                hour += 12
            elif period == 'am' and hour == 12:
                hour = 0

        # Validate hour/minute
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            return None, None

        time_str = f"{hour:02d}:{minute:02d}"

        # Extract task description (everything before "at")
        task_parts = command.split('at')[0].strip()
        if not task_parts:
            # Try everything after the time
            task_parts = command[match.end():].strip()

        return time_str, task_parts

    except Exception as e:
        logger.error(f"Error parsing schedule command: {e}")
        return None, None


def format_task_list(tasks: List[Dict]) -> str:
    """
    Format task list for display.

    Args:
        tasks: List of task dictionaries

    Returns:
        Formatted string representation
    """
    if not tasks:
        return "No scheduled tasks"

    output = f"\nScheduled Tasks ({len(tasks)}):\n"
    output += "=" * 60 + "\n"

    for i, task in enumerate(tasks, 1):
        output += f"{i}. {task['name']}\n"
        output += f"   Time: {task['time']}\n"
        if task['description']:
            output += f"   Description: {task['description']}\n"
        output += f"   Recurring: {'Yes' if task['recurring'] else 'No'}\n"
        output += f"   Executed: {task['execution_count']} times\n"
        output += "\n"

    return output
