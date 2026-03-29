from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime


def main():
    """Test script to verify PawPal+ system logic"""
    
    # Create an owner
    owner = Owner(
        name="Alice",
        available_time=8.0,
        preferences={"feeding_time": "8:00 AM", "play_time": "evening"}
    )
    
    # Create pets
    fluffy = Pet(
        name="Fluffy",
        species="cat",
        breed="Persian",
        age=3,
        care_notes="Needs daily brushing"
    )
    
    buddy = Pet(
        name="Buddy",
        species="dog",
        breed="Golden Retriever",
        age=5,
        care_notes="Needs 1-hour walks daily"
    )
    
    # Add pets to owner
    owner.add_pet(fluffy)
    owner.add_pet(buddy)
    
    # Create tasks for Fluffy
    task1 = Task(
        title="Feed Fluffy",
        category="Feeding",
        duration=15.0,
        priority=3,
        preferred_time="8:00 AM",
        recurring=True,
        recurrence_pattern="daily"
    )
    
    task2 = Task(
        title="Brush Fluffy",
        category="Grooming",
        duration=30.0,
        priority=2,
        preferred_time="10:00 AM",
        recurring=True,
        recurrence_pattern="daily"
    )
    
    # Create tasks for Buddy
    task3 = Task(
        title="Walk Buddy",
        category="Exercise",
        duration=60.0,
        priority=3,
        preferred_time="9:00 AM",
        recurring=True,
        recurrence_pattern="daily"
    )
    
    task4 = Task(
        title="Feed Buddy",
        category="Feeding",
        duration=20.0,
        priority=3,
        preferred_time="6:00 PM",
        recurring=True,
        recurrence_pattern="daily"
    )
    
    # Add tasks to pets
    fluffy.add_task(task1)
    fluffy.add_task(task2)
    buddy.add_task(task3)
    buddy.add_task(task4)
    
    # Create and use scheduler
    scheduler = Scheduler(owner=owner, available_time=8.0)
    
    # Generate the daily plan
    daily_plan = scheduler.generate_daily_plan()
    
    # Print today's schedule
    print("=" * 50)
    print("🐾 PawPal+ - Today's Schedule 🐾")
    print("=" * 50)
    print(f"Owner: {owner.name}")
    print(f"Available Time: {owner.available_time} hours")
    print()
    
    # Print the daily plan explanation
    print(scheduler.explain_plan())
    
    # Check for conflicts
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        print("⚠️  Scheduling Conflicts Detected:")
        for task1, task2 in conflicts:
            print(f"   - '{task1.title}' and '{task2.title}' at {task1.preferred_time}")
    else:
        print("✓ No scheduling conflicts detected!")
    
    print("=" * 50)
    
    # Test individual pet info
    print("\nPet Details:")
    pet = owner.get_pet_info(0)
    if pet:
        print(f"  {pet.name} ({pet.species}) - {len(pet.get_tasks())} tasks")
    
    pet = owner.get_pet_info(1)
    if pet:
        print(f"  {pet.name} ({pet.species}) - {len(pet.get_tasks())} tasks")
    
    # Mark a task as complete
    print("\nMarking 'Feed Fluffy' as complete...")
    task1.mark_complete()
    print(f"  {task1.get_task_summary()}")


if __name__ == "__main__":
    main()
