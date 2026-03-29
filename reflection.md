# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

My initial UML design focused on modeling the main parts of the PawPal+ system and the relationships between them. I designed the system so that an Owner can manage one or more Pets, each Pet can have multiple care Tasks, and the Scheduler is responsible for organizing those tasks into a daily plan based on priorities and constraints.

- What classes did you include, and what responsibilities did you assign to each?

My initial UML design included four main classes: Owner, Pet, Task, and Scheduler. The Owner class is responsible for storing basic information about the pet owner and their preferences or available time. The Pet class stores information about the pet, such as its name, type, and care needs. The Task class represents individual care tasks like feeding, walks, medications, or grooming, along with details such as duration, priority, and category. The Scheduler class is responsible for organizing tasks into a daily plan based on priorities and constraints.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

I updated my design to make the scheduling system more practical. I added stronger relationships between classes, especially by connecting each Task to a specific Pet and giving the Scheduler more context about the Owner and Pets. I also realized that the Owner should have a way to gather tasks across all pets so the system can build a complete daily plan.

I also improved the Task design by noting that it needs better time-related information, such as a due date, scheduled time, or recurrence pattern. Finally, I recognized that some details should be more reliable, such as using a clearer way to identify pets and tracking task completion more carefully. These changes made the design more connected and better suited for the app’s scheduling goals.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
  My scheduler considers task time, priority, and completion status when organizing a daily plan. It also uses pet information to group and manage tasks more clearly. I decided that time and priority mattered most because the app’s main goal is to help a pet owner see what needs to be done and in what order. Completion status also matters because completed tasks should not be treated the same as pending ones.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is that conflict detection only checks whether two tasks have the exact same scheduled time. This is reasonable for this scenario because it keeps the logic simple and easy to understand, while still giving useful warnings for obvious conflicts. It does not detect partial overlaps based on task duration, but that level of detail was not necessary for this version of the project.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
