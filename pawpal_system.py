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
        """Update task attributes"""
        pass
    
    def mark_complete(self) -> None:
        """Mark the task as completed"""
        pass
    
    def get_task_summary(self) -> str:
        """Get a summary of the task"""
        pass


@dataclass
class Pet:
    """Represents a pet in the PawPal+ system"""
    name: str
    species: str
    breed: str
    age: int
    care_notes: str
    pet_id: int = field(default_factory=lambda: None)
    tasks: List[Task] = field(default_factory=list)
    
    def add_task(self, task: Task) -> None:
        """Add a task for this pet"""
        pass
    
    def get_tasks(self) -> List[Task]:
        """Get all tasks for this pet"""
        pass
    
    def update_pet_info(self, info: Dict) -> None:
        """Update pet information"""
        pass


class Owner:
    """Represents a pet owner in the PawPal+ system"""
    
    def __init__(self, name: str, available_time: float, preferences: Dict = None):
        self.name = name
        self.available_time = available_time
        self.preferences = preferences or {}
        self.pets: List[Pet] = []
    
    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's collection"""
        pass
    
    def update_preferences(self, prefs: Dict) -> None:
        """Update owner preferences"""
        pass
    
    def get_pet_info(self, pet_id: int) -> Optional[Pet]:
        """Get information about a specific pet by ID"""
        pass
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks across all of the owner's pets"""
        pass


class Scheduler:
    """Scheduler for managing and organizing pet care tasks"""
    
    def __init__(self, owner: 'Owner', available_time: float, constraints: Dict = None):
        self.owner = owner
        self.tasks: List[Task] = []
        self.available_time = available_time
        self.constraints = constraints or {}
        self.daily_plan: List[Task] = []
    
    def add_tasks_from_owner(self, owner: 'Owner') -> None:
        """Load all tasks from the owner's pets into the scheduler"""
        pass
    
    def sort_tasks(self) -> List[Task]:
        """Sort tasks by priority and other criteria"""
        pass
    
    def detect_conflicts(self) -> List[tuple]:
        """Detect scheduling conflicts"""
        pass
    
    def generate_daily_plan(self) -> List[Task]:
        """Generate a daily plan for all tasks"""
        pass
    
    def explain_plan(self) -> str:
        """Explain the generated daily plan"""
        pass
