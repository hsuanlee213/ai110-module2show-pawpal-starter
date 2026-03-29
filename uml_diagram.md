# PawPal+ Class Diagram

```mermaid
classDiagram
    class Owner {
        -string name
        -float available_time
        -dict preferences
        -list pets
        +add_pet(pet)
        +update_preferences(prefs)
        +get_pet_info(pet_id)
        +get_all_tasks()
    }

    class Pet {
        -int pet_id
        -string name
        -string species
        -string breed
        -int age
        -string care_notes
        -list tasks
        +add_task(task)
        +get_tasks()
        +update_pet_info(info)
    }

    class Task {
        -string title
        -string category
        -float duration
        -int priority
        -string preferred_time
        -bool recurring
        -bool completed
        -Pet pet
        -datetime due_date
        -datetime completed_at
        -string recurrence_pattern
        +update_task(updates)
        +mark_complete()
        +get_task_summary()
    }

    class Scheduler {
        -Owner owner
        -list tasks
        -float available_time
        -dict constraints
        -list daily_plan
        +add_tasks_from_owner(owner)
        +sort_tasks()
        +detect_conflicts()
        +generate_daily_plan()
        +explain_plan()
        +handle_recurring_task(task): Task
        +filter_by_completion_status(completed): List[Task]
        +filter_by_pet_name(pet_name): List[Task]
    }

    Owner "1" --> "*" Pet : owns
    Pet "1" --> "*" Task : contains
    Scheduler "1" --> "1" Owner : schedules for
```
