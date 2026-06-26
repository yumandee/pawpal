from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Owner:
    name: str
    preferences: list[str] = field(default_factory=list)


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
    priority: str
    title: str
    pet: Pet
    completed: bool = False

    def complete_task(self) -> None:
        raise NotImplementedError


@dataclass
class DailySchedule:
    tasks: list[Task] = field(default_factory=list)

    def generate_schedule(self) -> list[Task]:
        raise NotImplementedError
