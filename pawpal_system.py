from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class DaytimePreference(str, Enum):
    DAYTIME = "daytime"
    AFTERNOON = "afternoon"
    NIGHTTIME = "nighttime"


class TaskPriority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class TaskFrequency(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    AS_NEEDED = "as_needed"


@dataclass
class Owner:
    name: str
    preference: DaytimePreference = DaytimePreference.DAYTIME
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        if pet not in self.pets:
            self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        tasks: list[Task] = []
        for pet in self.pets:
            tasks.extend(pet.tasks)
        return tasks


@dataclass
class Pet:
    owner: Owner
    name: str
    species: str
    breed: str
    age: int
    tasks: list[Task] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.owner.add_pet(self)

    def add_task(self, task: Task) -> None:
        if task not in self.tasks:
            self.tasks.append(task)

    def pending_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]


@dataclass
class Task:
    description: str
    duration_minutes: int
    frequency: TaskFrequency
    priority: TaskPriority = TaskPriority.MEDIUM
    completed: bool = False
    pets: list[Pet] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.validate_task()
        if self.pets:
            for pet in self.pets:
                pet.add_task(self)

    def validate_task(self) -> bool:
        """Validation skeleton for task-level rules."""
        errors: list[str] = []

        if not self.description.strip():
            errors.append("Task description must not be empty.")
        if self.duration_minutes <= 0:
            errors.append("Task duration must be greater than 0.")

        if errors:
            raise ValueError(" ".join(errors))
        return True

    def complete_task(self) -> None:
        self.completed = True


@dataclass
class ScheduledTask:
    task: Task
    scheduled_start: str
    scheduled_end: str


@dataclass
class Scheduler:
    owner: Owner

    def retrieve_tasks(self) -> list[Task]:
        return self.owner.get_all_tasks()

    def pending_tasks(self) -> list[Task]:
        return [task for task in self.retrieve_tasks() if not task.completed]

    def organize_tasks(self) -> list[Task]:
        priority_order = {
            TaskPriority.HIGH: 0,
            TaskPriority.MEDIUM: 1,
            TaskPriority.LOW: 2,
        }
        return sorted(
            self.pending_tasks(),
            key=lambda task: (priority_order[task.priority], task.duration_minutes),
        )

    def _preferred_start_minutes(self) -> int:
        return {
            DaytimePreference.DAYTIME: 7 * 60,
            DaytimePreference.AFTERNOON: 12 * 60,
            DaytimePreference.NIGHTTIME: 17 * 60,
        }[self.owner.preference]

    def _preferred_end_minutes(self) -> int:
        return {
            DaytimePreference.DAYTIME: 12 * 60,
            DaytimePreference.AFTERNOON: 17 * 60,
            DaytimePreference.NIGHTTIME: 24 * 60,
        }[self.owner.preference]

    @staticmethod
    def _format_minutes(total_minutes: int) -> str:
        total_minutes = max(0, total_minutes)
        hours = (total_minutes // 60) % 24
        minutes = total_minutes % 60

        suffix = "AM" if hours < 12 else "PM"
        display_hour = hours % 12
        if display_hour == 0:
            display_hour = 12

        return f"{display_hour}:{minutes:02d} {suffix}"

    def generate_schedule(self) -> list[ScheduledTask]:
        tasks = self.organize_tasks()
        if not tasks:
            return []

        preferred_start = self._preferred_start_minutes()
        preferred_end = self._preferred_end_minutes()

        total_duration = sum(task.duration_minutes for task in tasks)
        available_minutes = preferred_end - preferred_start

        current_time = preferred_start
        if total_duration > available_minutes:
            overflow = total_duration - available_minutes
            current_time = max(0, preferred_start - overflow)

        scheduled_tasks: list[ScheduledTask] = []

        for task in tasks:
            start_time = current_time
            end_time = start_time + task.duration_minutes

            scheduled_tasks.append(
                ScheduledTask(
                    task=task,
                    scheduled_start=self._format_minutes(start_time),
                    scheduled_end=self._format_minutes(end_time),
                )
            )

            current_time = end_time

        return scheduled_tasks
