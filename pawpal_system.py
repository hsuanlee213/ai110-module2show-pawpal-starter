from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Task:
    """Represents a pet care task"""
    title: str
    category: str
    duration: float
    priority: int
    preferred_time: str
    recurring: bool
    completed: bool = False
    pet: Optional['Pet'] = None
    due_date: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    recurrence_pattern: Optional[str] = None  # "daily", "weekly", etc.
    
    def update_task(self, updates: Dict) -> None:
        """Update task attributes."""
        for key, value in updates.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def mark_complete(self) -> None:
        """Mark task as completed with timestamp."""
        self.completed = True
        self.completed_at = datetime.now()
    
    def get_task_summary(self) -> str:
        """Get formatted task summary with status."""
        pet_name = self.pet.name if self.pet else "Unknown Pet"
        status = "✓ Completed" if self.completed else "⏳ Pending"
        return f"{self.title} ({pet_name}) - {self.category} - {status}"


@dataclass
class Pet:
    """Represents a pet in the PawPal+ system"""
    name: str
    species: str
    breed: str
    age: int
    care_notes: str
    pet_id: Optional[int] = None
    tasks: List[Task] = field(default_factory=list)
    
    def add_task(self, task: Task) -> None:
        """Add task with bidirectional pet link."""
        task.pet = self
        self.tasks.append(task)
    
    def get_tasks(self) -> List[Task]:
        """Get all tasks for this pet."""
        return self.tasks
    
    def update_pet_info(self, info: Dict) -> None:
        """Update pet attributes."""
        for key, value in info.items():
            if hasattr(self, key) and key != "tasks":
                setattr(self, key, value)


class Owner:
    """Represents a pet owner in the PawPal+ system"""
    
    def __init__(self, name: str, available_time: float, preferences: Dict = None):
        self.name = name
        self.available_time = available_time
        self.preferences = preferences or {}
        self.pets: List[Pet] = []
    
    def add_pet(self, pet: Pet) -> None:
        """Add pet with auto-assigned ID."""
        pet.pet_id = len(self.pets)
        self.pets.append(pet)
    
    def update_preferences(self, prefs: Dict) -> None:
        """Update owner preferences."""
        self.preferences.update(prefs)
    
    def get_pet_info(self, pet_id: int) -> Optional[Pet]:
        """Get pet by ID."""
        for pet in self.pets:
            if pet.pet_id == pet_id:
                return pet
        return None
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Scheduler for managing and organizing pet care tasks"""
    
    def __init__(self, owner: 'Owner', available_time: float, constraints: Dict = None):
        self.owner = owner
        self.tasks: List[Task] = []
        self.available_time = available_time
        self.constraints = constraints or {}
        self.daily_plan: List[Task] = []
    
    def add_tasks_from_owner(self) -> None:
        """Load owner's tasks into scheduler."""
        self.tasks = self.owner.get_all_tasks()
    
    def sort_tasks(self) -> List[Task]:
        """Sort tasks by priority and time."""
        def time_key(task):
            time_str = task.preferred_time or "23:59"
            try:
                hours, minutes = map(int, time_str.split(":"))
                return hours * 60 + minutes  # Convert to minutes for proper sorting
            except (ValueError, AttributeError):
                return 24 * 60  # Default to end of day if invalid
        
        return sorted(self.tasks, key=lambda t: (-t.priority, time_key(t)))
    
    def detect_conflicts(self) -> List[tuple]:
        """Find tasks scheduled for the same time."""
        conflicts = []
        sorted_tasks = self.sort_tasks()
        
        for i in range(len(sorted_tasks)):
            for j in range(i + 1, len(sorted_tasks)):
                task1 = sorted_tasks[i]
                task2 = sorted_tasks[j]
                
                # Simple conflict detection: same preferred_time
                if task1.preferred_time == task2.preferred_time:
                    conflicts.append((task1, task2))
        
        return conflicts
    
    def filter_by_completion_status(self, completed: bool) -> List[Task]:
        """
        Filter tasks by completion status.
        
        Args:
            completed: True for completed tasks, False for pending tasks
            
        Returns:
            List of tasks matching the completion status
        """
        return [task for task in self.tasks if task.completed == completed]
    
    def filter_by_pet_name(self, pet_name: str) -> List[Task]:
        """
        Filter tasks by pet name.
        
        Args:
            pet_name: Name of the pet to filter by
            
        Returns:
            List of tasks for the specified pet
        """
        return [task for task in self.tasks if task.pet and task.pet.name.lower() == pet_name.lower()]
    
    def generate_daily_plan(self) -> List[Task]:
        """Generate sorted daily task plan."""
        self.add_tasks_from_owner()
        self.daily_plan = self.sort_tasks()
        return self.daily_plan
    
    def explain_plan(self) -> str:
        """Get human-readable daily schedule."""
        if not self.daily_plan:
            return "No tasks scheduled for today."
        
        explanation = "📋 Daily Plan:\n"
        for idx, task in enumerate(self.daily_plan, 1):
            pet_name = task.pet.name if task.pet else "Unknown"
            status = "✓" if task.completed else "•"
            explanation += f"{idx}. {status} {task.title} ({pet_name}) at {task.preferred_time} - {task.duration}min\n"
        
        return explanation
