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

I used AI tools throughout the project in several ways. I mainly used VS Code Copilot to help generate and revise code inside my project files, especially when implementing class methods, adding scheduling features, and drafting tests. I also used ChatGPT to discuss the project requirements, break complex steps into smaller tasks, and help me think through design decisions before making changes.

The most helpful prompts were the ones that were specific and tied to my actual files or current phase. For example, it was useful to ask AI to implement a method in `pawpal_system.py` with minimal changes, compare my test code against my current implementation, or explain how to connect Streamlit UI actions to my backend logic. Prompts that clearly stated the goal, the file, and the constraints gave the best results.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One moment where I did not accept an AI suggestion as-is was during the conflict detection part of the scheduler. AI suggested a more Pythonic version, but I decided not to fully adopt the more advanced approach because it was less readable for me and would have made the project harder to explain. Instead, I kept a simpler version, or only accepted small improvements that made the code cleaner without adding too much complexity.

I evaluated AI suggestions by comparing them against my current code structure, checking whether the method names and return values actually matched my implementation, and then testing the results in the terminal or with pytest. If a suggestion was harder to understand or introduced unnecessary complexity, I changed it or rejected it. This helped me use AI as a support tool rather than blindly copying its output.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested several core behaviors of the PawPal+ system, including task sorting, recurring task creation, conflict detection, and basic task and pet interactions. For example, I verified that tasks could be returned in the correct order, that completing a daily recurring task created a new task for the following day, and that the scheduler could flag tasks scheduled at the same time.

These tests were important because they covered the main logic of the scheduler rather than just basic data storage. Since the project depends on the scheduler to organize tasks correctly and handle recurring events, I wanted to make sure the most important planning behaviors worked as expected.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident that my scheduler works correctly for the main scenarios I implemented, especially because my automated tests passed and my terminal and Streamlit demos matched the expected behavior. I feel most confident about the core workflows, such as adding pets and tasks, sorting tasks, generating a daily plan, and detecting simple conflicts.

If I had more time, I would test more edge cases. For example, I would test invalid or missing time formats, pets with no tasks, multiple recurring tasks at once, and more advanced conflict cases such as overlapping task durations rather than only exact time matches.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied with how much my development speed and organization have improved. Earlier in my learning, a project of similar scope might have taken me one or two weeks, but this time I was able to complete it in less than half a day. This made me feel that I have grown in coding, planning, debugging, and using AI tools more effectively.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
  If I had another iteration, I would improve the user interface and make it more polished. The current version works, but I would like to design a more visually appealing and user-friendly layout so the schedule and warnings are easier to read.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

One important thing I learned from this project is that even though AI can help me finish work much faster, I still need to follow the project guide step by step and build the system carefully. Otherwise, it is easy to make too many changes at once or move the design in the wrong direction. AI was most helpful when I used it as support, not as a replacement for my own judgment.
