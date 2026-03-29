import pytest
from pawpal_system import Task, Pet, Owner


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
