# Write a script in main.py that performs the following:
# Imports your classes from pawpal_system.py.
# Creates an Owner and at least two Pets .
# Adds at least three Tasks with different times to those pets.
# Prints a "Today's Schedule" to the terminal.


from pawpal_system import (
    Owner,
    Pet,
    Scheduler,
    Task,
    TaskPriority,
    TaskFrequency,
    DaytimePreference,
)

owner = Owner("Mandy", preference=DaytimePreference.AFTERNOON)

damien = Pet(owner=owner, name="Damien", species="Cat", breed="Tuxedo", age=2)
kino = Pet(owner=owner, name="Kino", species="Cat", breed="Orange", age=2)
louie = Pet(owner=owner, name="Louie", species="Dog", breed="Havanese", age=5)

breakfast = Task(
    description="Feed breakfast",
    duration_minutes=30,
    priority=TaskPriority.HIGH,
    frequency=TaskFrequency.DAILY,
    pets=[damien, kino, louie],
)

brushing = Task(
    description="Brush cats",
    duration_minutes=45,
    priority=TaskPriority.MEDIUM,
    frequency=TaskFrequency.WEEKLY,
    pets=[damien, kino],
)

walk = Task(
    description="Walk Louie",
    duration_minutes=60,
    priority=TaskPriority.HIGH,
    frequency=TaskFrequency.DAILY,
    pets=[louie],
)

schedule = Scheduler(owner=owner).generate_schedule()
print("my tasks:", owner.get_all_tasks())
print("Today's Schedule:")
for scheduled_task in schedule:
    print(
        f"[{scheduled_task.scheduled_start} - {scheduled_task.scheduled_end}] {scheduled_task.task.description}"
    )
