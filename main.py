from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import datetime, timedelta


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
    
    # Create tasks OUT OF ORDER to test sorting
    # Task 4: Evening (added first)
    task4 = Task(
        title="Feed Buddy",
        category="Feeding",
        duration=20.0,
        priority=3,
        preferred_time="6:00 PM",
        recurring=True,
        recurrence_pattern="daily",
        due_date=datetime(2026, 3, 29)  # Today's date
    )
    
    # Task 1: Morning (added second)
    task1 = Task(
        title="Feed Fluffy",
        category="Feeding",
        duration=15.0,
        priority=3,
        preferred_time="8:00 AM",
        recurring=True,
        recurrence_pattern="daily",
        due_date=datetime(2026, 3, 29)
    )
    
    # Task 3: Mid-morning (added third)
    task3 = Task(
        title="Walk Buddy",
        category="Exercise",
        duration=60.0,
        priority=4,  # Higher priority
        preferred_time="9:00 AM",
        recurring=True,
        recurrence_pattern="weekly",
        due_date=datetime(2026, 3, 29)
    )
    
    # Task 2: Late morning (added last)
    task2 = Task(
        title="Brush Fluffy",
        category="Grooming",
        duration=30.0,
        priority=2,
        preferred_time="10:00 AM",
        recurring=False,  # Non-recurring
        due_date=datetime(2026, 3, 29)
    )
    
    # Add tasks to pets in mixed order
    fluffy.add_task(task4)  # This belongs to Buddy, will be re-assigned
    buddy.add_task(task4)
    fluffy.add_task(task1)
    buddy.add_task(task3)
    fluffy.add_task(task2)
    
    # Mark some tasks as completed to test filtering
    task1.mark_complete()  # Feed Fluffy - completed
    task3.mark_complete()  # Walk Buddy - completed
    
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
    
    print("\n" + "=" * 50)
    print("🔍 TESTING SORTING & FILTERING METHODS")
    print("=" * 50)
    
    # Test 1: Display tasks in order added (unsorted)
    print("\n📌 Tasks in Order Added (UNSORTED):")
    for i, task in enumerate(scheduler.tasks, 1):
        pet_name = task.pet.name if task.pet else "Unknown"
        status = "✓" if task.completed else "⏳"
        print(f"  {i}. {status} {task.title} ({pet_name}) at {task.preferred_time} | Priority: {task.priority}")
    
    # Test 2: Display sorted tasks
    print("\n⏰ Tasks SORTED by Priority & Time:")
    sorted_tasks = scheduler.sort_tasks()
    for i, task in enumerate(sorted_tasks, 1):
        pet_name = task.pet.name if task.pet else "Unknown"
        status = "✓" if task.completed else "⏳"
        print(f"  {i}. {status} {task.title} ({pet_name}) at {task.preferred_time} | Priority: {task.priority}")
    
    # Test 3: Filter by completion status - Pending tasks
    print("\n⏳ PENDING Tasks Only:")
    pending_tasks = scheduler.filter_by_completion_status(False)
    if pending_tasks:
        for i, task in enumerate(pending_tasks, 1):
            pet_name = task.pet.name if task.pet else "Unknown"
            print(f"  {i}. {task.title} ({pet_name}) at {task.preferred_time}")
    else:
        print("  No pending tasks!")
    
    # Test 4: Filter by completion status - Completed tasks
    print("\n✓ COMPLETED Tasks Only:")
    completed_tasks = scheduler.filter_by_completion_status(True)
    if completed_tasks:
        for i, task in enumerate(completed_tasks, 1):
            pet_name = task.pet.name if task.pet else "Unknown"
            print(f"  {i}. {task.title} ({pet_name}) at {task.preferred_time}")
    else:
        print("  No completed tasks!")
    
    # Test 5: Filter by pet name - Fluffy
    print("\n🐱 Tasks for FLUFFY:")
    fluffy_tasks = scheduler.filter_by_pet_name("Fluffy")
    if fluffy_tasks:
        for i, task in enumerate(fluffy_tasks, 1):
            status = "✓" if task.completed else "⏳"
            print(f"  {i}. {status} {task.title} at {task.preferred_time}")
    else:
        print("  No tasks for Fluffy!")
    
    # Test 6: Filter by pet name - Buddy
    print("\n🐕 Tasks for BUDDY:")
    buddy_tasks = scheduler.filter_by_pet_name("Buddy")
    if buddy_tasks:
        for i, task in enumerate(buddy_tasks, 1):
            status = "✓" if task.completed else "⏳"
            print(f"  {i}. {status} {task.title} at {task.preferred_time}")
    else:
        print("  No tasks for Buddy!")
    
    print("\n" + "=" * 50)
    
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
    
    print("\n" + "=" * 50)
    print("🔄 TESTING RECURRING TASK LOGIC")
    print("=" * 50)
    
    # Test recurring task creation - daily recurrence
    print("\n📋 Before creating recurring tasks:")
    print(f"  Fluffy's tasks: {len(fluffy.get_tasks())}")
    print(f"  Buddy's tasks: {len(buddy.get_tasks())}")
    
    # Create recurring task for "Feed Fluffy" (daily)
    print("\n✅ Marking 'Feed Fluffy' as complete and creating next occurrence...")
    new_task1 = scheduler.handle_recurring_task(task1)
    if new_task1:
        print(f"  ✓ Created: {new_task1.title}")
        print(f"    Due: {new_task1.due_date.strftime('%Y-%m-%d')}")
        print(f"    Completed: {new_task1.completed}")
        print(f"    Recurrence: {new_task1.recurrence_pattern}")
    else:
        print("  ✗ Failed to create recurring task")
    
    # Create recurring task for "Walk Buddy" (weekly)
    print("\n✅ Marking 'Walk Buddy' as complete and creating next occurrence...")
    new_task3 = scheduler.handle_recurring_task(task3)
    if new_task3:
        print(f"  ✓ Created: {new_task3.title}")
        print(f"    Due: {new_task3.due_date.strftime('%Y-%m-%d')}")
        print(f"    Completed: {new_task3.completed}")
        print(f"    Recurrence: {new_task3.recurrence_pattern}")
        days_until = (new_task3.due_date - task3.due_date).days
        print(f"    Days until next: {days_until}")
    else:
        print("  ✗ Failed to create recurring task")
    
    # Try to create recurring task for non-recurring task (should fail)
    print("\n⚠️  Trying to create recurring task for non-recurring task...")
    result = scheduler.handle_recurring_task(task2)
    if result is None:
        print("  ✓ Correctly skipped (task is not recurring)")
    else:
        print("  ✗ Unexpected result")
    
    # Reload scheduler to see all updated tasks
    scheduler.add_tasks_from_owner()
    print(f"\n📊 After creating recurring tasks:")
    print(f"  Fluffy's tasks: {len(fluffy.get_tasks())}")
    print(f"  Buddy's tasks: {len(buddy.get_tasks())}")
    
    print("\n🐱 All Fluffy's tasks (including new recurring ones):")
    for i, t in enumerate(fluffy.get_tasks(), 1):
        status = "✓" if t.completed else "⏳"
        due = t.due_date.strftime('%Y-%m-%d') if t.due_date else "None"
        recur = f" [{t.recurrence_pattern}]" if t.recurring else ""
        print(f"  {i}. {status} {t.title} (due: {due}){recur}")


if __name__ == "__main__":
    main()
