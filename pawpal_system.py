from __future__ import annotations

from datetime import date
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


@dataclass
class Owner:
    name: str
    preference: DaytimePreference = DaytimePreference.DAYTIME
    pets: list[Pet] = field(default_factory=list)


@dataclass
class Pet:
    owner: Owner
    name: str
    species: str
    breed: str
    age: int


@dataclass
class Task:
    duration_minutes: int
    priority: TaskPriority
    title: str
    pet: Pet
    completed: bool = False

    def validate_task(self) -> bool:
        raise NotImplementedError

    def complete_task(self) -> None:
        raise NotImplementedError


@dataclass
class DailySchedule:
    owner: Owner
    schedule_date: date
    available_minutes: int
    tasks: list[Task] = field(default_factory=list)

    def generate_schedule(self) -> list[Task]:
        raise NotImplementedError
