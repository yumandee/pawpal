from pawpal_system import DaytimePreference, Owner, Pet, Task, TaskFrequency


def test_task_marks_complete() -> None:
    task = Task(
        description="Walk the dog",
        duration_minutes=30,
        frequency=TaskFrequency.DAILY,
    )

    assert task.completed is False

    task.complete_task()

    assert task.completed is True


def test_adding_task_to_pet_increases_task_count() -> None:
    owner = Owner(name="Sam", preference=DaytimePreference.DAYTIME)
    pet = Pet(
        owner=owner,
        name="Buddy",
        species="Dog",
        breed="Golden Retriever",
        age=4,
    )
    task = Task(
        description="Brush coat",
        duration_minutes=15,
        frequency=TaskFrequency.WEEKLY,
    )

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0] is task
