import streamlit as st
from pawpal_system import (
    DaytimePreference,
    Owner,
    Pet,
    Scheduler,
    Task,
    TaskFrequency,
    TaskPriority,
)

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# st.markdown(
#     """
# Welcome to the PawPal+ starter app.

# This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
# but **it does not implement the project logic**. Your job is to design the system and build it.

# Use this app as your interactive demo once your backend classes/functions exist.
# """
# )

st.markdown(
    """
        Welcome to PawPal+, your pet care planning assistant! 
        This app helps you plan care tasks for your pet(s).
    """
)

# with st.expander("Scenario", expanded=True):
#     st.markdown(
#         """
# **PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
# for their pet(s) based on constraints like time, priority, and preferences.

# You will design and implement the scheduling logic and connect it to this Streamlit UI.
# """
#     )

# with st.expander("What you need to build", expanded=True):
#     st.markdown(
#         """
# At minimum, your system should:
# - Represent pet care tasks (what needs to happen, how long it takes, priority)
# - Represent the pet and the owner (basic info and preferences)
# - Build a plan/schedule for a day that chooses and orders tasks based on constraints
# - Explain the plan (why each task was chosen and when it happens)
# """
#     )

# st.divider()

# st.subheader("Quick Demo Inputs (UI only)")
# owner_name = st.text_input("Owner name", value="Jordan")
# pet_name = st.text_input("Pet name", value="Mochi")
# species = st.selectbox("Species", ["dog", "cat", "other"])
st.markdown("### Owner")

if "owner" not in st.session_state or st.session_state.owner is None:
    st.session_state.owner = Owner(name="", pets=[])

owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
st.session_state.owner.name = owner_name

preference_values = [preference.value for preference in DaytimePreference]
current_preference_index = preference_values.index(
    st.session_state.owner.preference.value
)
preference_value = st.selectbox(
    "Owner daytime preference",
    options=preference_values,
    index=current_preference_index,
)
st.session_state.owner.preference = DaytimePreference(preference_value)

st.markdown("### Pets")
st.caption("Add one or more pets for this owner.")

with st.form("add_pet_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        pet_name = st.text_input("Pet name")
        species = st.text_input("Species")
    with col2:
        breed = st.text_input("Breed")
        age = st.number_input("Age", min_value=0, max_value=100, value=1, step=1)

    add_pet_clicked = st.form_submit_button("Add pet")

if add_pet_clicked:
    if not pet_name.strip() or not species.strip():
        st.error("Please provide at least a pet name and species.")
    else:
        Pet(
            owner=st.session_state.owner,
            name=pet_name.strip(),
            species=species.strip(),
            breed=breed.strip(),
            age=int(age),
        )
        st.success(
            f"Added {pet_name.strip()} to {st.session_state.owner.name or 'owner'}."
        )

if st.session_state.owner.pets:
    st.write("Current pets:")
    st.table(
        [
            {
                "Name": pet.name,
                "Species": pet.species,
                "Breed": pet.breed,
                "Age": pet.age,
            }
            for pet in st.session_state.owner.pets
        ]
    )
else:
    st.info("No pets added yet.")


st.markdown("### Tasks")
st.caption("Add a task and associate it with one or more pets.")

if st.session_state.owner.pets:
    pet_options = {
        f"{pet.name} ({pet.species})": pet for pet in st.session_state.owner.pets
    }

    with st.form("add_task_form", clear_on_submit=True):
        task_description = st.text_input("Task description")
        duration_minutes = st.number_input(
            "Duration (minutes)", min_value=1, max_value=240, value=20, step=1
        )
        frequency_value = st.selectbox(
            "Frequency", [freq.value for freq in TaskFrequency], index=0
        )
        priority_value = st.selectbox(
            "Priority", [priority.value for priority in TaskPriority], index=1
        )
        selected_pet_labels = st.multiselect(
            "Assign to pets",
            options=list(pet_options.keys()),
        )

        add_task_clicked = st.form_submit_button("Add task")

    if add_task_clicked:
        if not task_description.strip():
            st.error("Please provide a task description.")
        elif not selected_pet_labels:
            st.error("Select at least one pet for this task.")
        else:
            selected_pets = [pet_options[label] for label in selected_pet_labels]
            Task(
                description=task_description.strip(),
                duration_minutes=int(duration_minutes),
                frequency=TaskFrequency(frequency_value),
                priority=TaskPriority(priority_value),
                pets=selected_pets,
            )
            st.success("Task added and assigned to selected pets.")

    all_tasks = st.session_state.owner.get_all_tasks()
    if all_tasks:
        unique_tasks = list({id(task): task for task in all_tasks}.values())
        st.write("Current tasks:")
        st.table(
            [
                {
                    "Description": task.description,
                    "Duration": task.duration_minutes,
                    "Frequency": task.frequency.value,
                    "Priority": task.priority.value,
                    "Pets": ", ".join(pet.name for pet in task.pets),
                    "Completed": task.completed,
                }
                for task in unique_tasks
            ]
        )
    else:
        st.info("No tasks added yet.")
else:
    st.info("Add at least one pet before creating tasks.")


st.markdown("### Schedule")
st.caption("Generate a schedule from the tasks currently assigned to your pets.")

all_tasks = st.session_state.owner.get_all_tasks()
unique_tasks = list({id(task): task for task in all_tasks}.values())

if "generated_schedule" not in st.session_state:
    st.session_state.generated_schedule = []

schedule_button_label = (
    "Regenerate schedule"
    if st.session_state.generated_schedule
    else "Generate schedule"
)

if st.button(schedule_button_label):
    if not unique_tasks:
        st.warning("Add at least one task before generating a schedule.")
    else:
        scheduler = Scheduler(owner=st.session_state.owner)
        st.session_state.generated_schedule = scheduler.generate_schedule()

if st.session_state.generated_schedule:
    st.write("Generated schedule:")
    st.table(
        [
            {
                "Task": scheduled_task.task.description,
                "Start": scheduled_task.scheduled_start,
                "End": scheduled_task.scheduled_end,
                "Priority": scheduled_task.task.priority.value,
                "Pets": ", ".join(pet.name for pet in scheduled_task.task.pets),
            }
            for scheduled_task in st.session_state.generated_schedule
        ]
    )
