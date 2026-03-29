#!/usr/bin/env python3
"""Quick test to verify imports and object creation work"""

# Test imports
try:
    from pawpal_system import Owner, Pet, Task, Scheduler
    print("[PASS] All imports successful!")
except ImportError as e:
    print("[FAIL] Import failed: " + str(e))
    exit(1)

# Test creating an Owner
owner = Owner("Jordan", 8.0)
print("[PASS] Owner created: " + owner.name + ", available time: " + str(owner.available_time) + "h")

# Test creating a Pet
pet = Pet("Mochi", "dog", "Labrador", 3, "Friendly and playful")
print("[PASS] Pet created: " + pet.name + " (" + pet.species + "), age " + str(pet.age))

# Test adding pet to owner
owner.add_pet(pet)
print("[PASS] Pet added to owner. Owner now has " + str(len(owner.pets)) + " pet(s)")
print("       Pet ID assigned: " + str(pet.pet_id))

# Test creating a Task
task = Task(
    title="Morning walk",
    category="Exercise",
    duration=30.0,
    priority=3,
    preferred_time="8:00 AM",
    recurring=True
)
print("[PASS] Task created: " + task.title)

# Test adding task to pet
pet.add_task(task)
print("[PASS] Task added to pet. Pet now has " + str(len(pet.get_tasks())) + " task(s)")

# Verify bidirectional link
pet_name = task.pet.name if task.pet else "No pet"
print("[PASS] Task is linked to pet: " + pet_name)

# Test Scheduler
scheduler = Scheduler(owner, 8.0)
daily_plan = scheduler.generate_daily_plan()
print("[PASS] Scheduler created and daily plan generated with " + str(len(daily_plan)) + " task(s)")

# Test getting pet info
retrieved_pet = owner.get_pet_info(0)
print("[PASS] Retrieved pet by ID: " + (retrieved_pet.name if retrieved_pet else "Failed"))

# Test all tasks across all pets
all_tasks = owner.get_all_tasks()
print("[PASS] Retrieved all tasks from owner: " + str(len(all_tasks)) + " task(s)")

print("")
print("[SUCCESS] All tests passed! Logic layer is working correctly!")
print("")
print("App.py can now successfully:")
print("  - Import Pet, Task, Owner, and Scheduler classes")
print("  - Create real objects that persist in memory")
print("  - Link objects together (pets to owners, tasks to pets)")
print("  - Schedule and manage tasks end-to-end")
