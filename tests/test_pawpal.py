import pytest
from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


class TestTask:
    """Tests for the Task class"""
    
    def test_mark_complete(self):
        """Test that mark_complete() changes the task's status"""
        # Arrange: Create a task
        task = Task(
            title="Feed Pet",
            category="Feeding",
            duration=15.0,
            priority=3,
            preferred_time="8:00 AM",
            recurring=False
        )
        
        # Assert initial state
        assert task.completed is False
        assert task.completed_at is None
        
        # Act: Mark the task as complete
        task.mark_complete()
        
        # Assert final state
        assert task.completed is True
        assert task.completed_at is not None


class TestPet:
    """Tests for the Pet class"""
    
    def test_add_task_increases_count(self):
        """Test that adding a task to a Pet increases that pet's task count"""
        # Arrange: Create a pet and a task
        pet = Pet(
            name="Fluffy",
            species="cat",
            breed="Persian",
            age=3,
            care_notes="Needs brushing"
        )
        
        task = Task(
            title="Brush Fluffy",
            category="Grooming",
            duration=30.0,
            priority=2,
            preferred_time="10:00 AM",
            recurring=True
        )
        
        # Assert initial count
        assert len(pet.get_tasks()) == 0
        
        # Act: Add the task to the pet
        pet.add_task(task)
        
        # Assert final count
        assert len(pet.get_tasks()) == 1
        
        # Assert that the task is linked to the pet
        assert task.pet == pet


class TestSchedulerSorting:
    """Tests for Scheduler sorting logic"""
    
    def test_sort_tasks_chronological_order(self):
        """Test that sort_tasks() returns tasks in chronological order by preferred_time."""
        # Arrange: Create an owner, pets, and scheduler with tasks at different times
        owner = Owner(name="Alice", available_time=120)
        pet = Pet(name="Buddy", species="dog", breed="Golden", age=5, care_notes="Friendly")
        owner.add_pet(pet)
        
        scheduler = Scheduler(owner=owner, available_time=120)
        
        # Create tasks with different preferred times (all same priority for simple test)
        task_morning = Task(title="Breakfast Feed", category="Feeding", duration=15, priority=2, preferred_time="08:00", recurring=False)
        task_afternoon = Task(title="Lunch Walk", category="Exercise", duration=30, priority=2, preferred_time="14:00", recurring=False)
        task_evening = Task(title="Evening Playtime", category="Enrichment", duration=20, priority=2, preferred_time="18:00", recurring=False)
        
        pet.add_task(task_morning)
        pet.add_task(task_afternoon)
        pet.add_task(task_evening)
        
        # Act: Add tasks from owner and sort
        scheduler.add_tasks_from_owner()
        sorted_tasks = scheduler.sort_tasks()
        
        # Assert: Tasks should be sorted chronologically by time (08:00 → 14:00 → 18:00)
        assert sorted_tasks[0].preferred_time == "08:00"
        assert sorted_tasks[1].preferred_time == "14:00"
        assert sorted_tasks[2].preferred_time == "18:00"


class TestSchedulerRecurrence:
    """Tests for Scheduler recurring task logic"""
    
    def test_handle_recurring_task_creates_next_occurrence(self):
        """Test that handle_recurring_task() creates a new task for the following day."""
        # Arrange: Create a pet with a daily recurring task
        pet = Pet(name="Luna", species="cat", breed="Siamese", age=2, care_notes="Playful")
        today = datetime(2026, 3, 29)
        
        task = Task(
            title="Feed Luna",
            category="Feeding",
            duration=15,
            priority=3,
            preferred_time="09:00",
            recurring=True,
            recurrence_pattern="daily",
            due_date=today
        )
        pet.add_task(task)
        
        # Create owner and scheduler
        owner = Owner(name="Bob", available_time=100)
        owner.add_pet(pet)
        scheduler = Scheduler(owner=owner, available_time=100)
        
        # Act: Handle recurrence
        new_task = scheduler.handle_recurring_task(task)
        
        # Assert: New task should be created with due_date one day later
        assert new_task is not None
        assert new_task.due_date == today + timedelta(days=1)
        assert new_task.title == "Feed Luna"
        assert new_task.recurring is True
        assert new_task.completed is False
        # Verify new task was added to pet's task list
        assert new_task in pet.get_tasks()


class TestSchedulerConflictDetection:
    """Tests for Scheduler conflict detection logic"""
    
    def test_detect_conflicts_finds_same_time_tasks(self):
        """Test that detect_conflicts() identifies two tasks scheduled at the same time."""
        # Arrange: Create an owner with two pets and tasks at the same time
        owner = Owner(name="Charlie", available_time=120)
        pet1 = Pet(name="Max", species="dog", breed="Lab", age=4, care_notes="Energetic")
        pet2 = Pet(name="Bella", species="dog", breed="Poodle", age=3, care_notes="Calm")
        owner.add_pet(pet1)
        owner.add_pet(pet2)
        
        # Create tasks scheduled at the same time
        task1 = Task(title="Walk Max", category="Exercise", duration=30, priority=2, preferred_time="10:00", recurring=False)
        task2 = Task(title="Walk Bella", category="Exercise", duration=30, priority=2, preferred_time="10:00", recurring=False)
        
        pet1.add_task(task1)
        pet2.add_task(task2)
        
        # Create scheduler with tasks and detect conflicts
        scheduler = Scheduler(owner=owner, available_time=120)
        scheduler.add_tasks_from_owner()
        
        # Act: Detect conflicts
        conflicts = scheduler.detect_conflicts()
        
        # Assert: Should detect exactly one conflict at the matching time
        assert len(conflicts) == 1
        assert "10:00" in conflicts[0]
        assert "Walk Max" in conflicts[0]
        assert "Walk Bella" in conflicts[0]
