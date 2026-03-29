import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Owner & Pet Setup")

# Initialize Owner in session state
if "owner" not in st.session_state:
    st.session_state.owner = None
if "pet" not in st.session_state:
    st.session_state.pet = None

col1, col2 = st.columns(2)
with col1:
    owner_name = st.text_input("Owner name", value="Jordan")
with col2:
    available_hours = st.number_input("Available hours per day", min_value=1.0, max_value=24.0, value=8.0)

col1, col2, col3 = st.columns(3)
with col1:
    pet_name = st.text_input("Pet name", value="Mochi")
with col2:
    species = st.selectbox("Species", ["dog", "cat", "other"])
with col3:
    pet_age = st.number_input("Pet age (years)", min_value=0, max_value=50, value=1)

if st.button("Create Owner & Pet"):
    # Create Owner
    st.session_state.owner = Owner(
        name=owner_name,
        available_time=available_hours,
        preferences={}
    )
    
    # Create Pet and add to Owner
    st.session_state.pet = Pet(
        name=pet_name,
        species=species,
        breed="Mixed",
        age=pet_age,
        care_notes=""
    )
    st.session_state.owner.add_pet(st.session_state.pet)
    st.success(f"✓ Owner '{owner_name}' and pet '{pet_name}' created!")

# Display current owner and pet
if st.session_state.owner:
    st.info(f"📋 Owner: **{st.session_state.owner.name}** | Pet: **{st.session_state.pet.name}** ({st.session_state.pet.species})")

st.markdown("### Tasks")
st.caption("Add tasks to your pet. These will be scheduled when you generate the daily plan.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3, col4 = st.columns(4)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.number_input("Priority (1-5)", min_value=1, max_value=5, value=3)
with col4:
    preferred_time = st.text_input("Time", value="8:00 AM", placeholder="e.g., 8:00 AM")

if st.button("Add task"):
    if st.session_state.owner and st.session_state.pet:
        # Create Task object
        new_task = Task(
            title=task_title,
            category="Care",
            duration=float(duration),
            priority=priority,
            preferred_time=preferred_time,
            recurring=False
        )
        # Add task to pet
        st.session_state.pet.add_task(new_task)
        st.success(f"✓ Task '{task_title}' added to {st.session_state.pet.name}!")
    else:
        st.warning("⚠️ Please create an Owner and Pet first!")

if st.session_state.pet and len(st.session_state.pet.get_tasks()) > 0:
    st.write("**Current tasks:**")
    task_data = []
    for task in st.session_state.pet.get_tasks():
        task_data.append({
            "Title": task.title,
            "Duration (min)": task.duration,
            "Priority": task.priority,
            "Time": task.preferred_time,
            "Status": "✓" if task.completed else "•"
        })
    st.table(task_data)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Generate Daily Schedule")
st.caption("Create an optimized daily plan based on your pet's tasks and your availability.")

if st.button("Generate schedule"):
    if st.session_state.owner and len(st.session_state.pet.get_tasks()) > 0:
        # Create Scheduler and generate daily plan
        scheduler = Scheduler(
            owner=st.session_state.owner,
            available_time=st.session_state.owner.available_time
        )
        
        # Generate the daily plan
        daily_plan = scheduler.generate_daily_plan()
        
        # Display the plan
        st.success("✨ Daily Schedule Generated!")
        
        # Check for conflicts first
        st.subheader("⚠️ Conflict Status")
        conflicts = scheduler.detect_conflicts()
        if conflicts:
            st.warning("**Scheduling Conflicts Detected:**")
            for conflict_warning in conflicts:
                st.write(conflict_warning)
        else:
            st.success("✓ No scheduling conflicts!")
        
        # Display sorted task schedule as a clean table
        st.subheader("📋 Today's Schedule (Sorted by Priority & Time)")
        sorted_tasks = scheduler.sort_tasks()
        
        # Build table data
        schedule_data = []
        for idx, task in enumerate(sorted_tasks, 1):
            schedule_data.append({
                "Order": idx,
                "Pet": task.pet.name if task.pet else "Unknown",
                "Task": task.title,
                "Time": task.preferred_time,
                "Duration": f"{task.duration}min",
                "Priority": task.priority,
                "Status": "✓ Done" if task.completed else "⏳ Pending"
            })
        
        st.dataframe(schedule_data, use_container_width=True)
    else:
        st.warning("⚠️ Please finish setup:")
        if not st.session_state.owner:
            st.write("1. Create an Owner and Pet")
        if not st.session_state.pet or len(st.session_state.pet.get_tasks()) == 0:
            st.write("2. Add at least one task")
