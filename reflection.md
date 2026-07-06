# PawPal+ Project Reflection

## 1. System Design

### Core actions

In this PawPal application, a user should be able to perform at least the following actions:

- enter owner and pet info
- schedule tasks
- track daily pet tasks

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The initial UML design should have the following classes and their respective attributes and methods:

- Owner
  - attributes: name (str), preferences (str[])
  - relationships: an owner can have one or more pets,
- Pet
  - attributes: owner (Owner), name (str), species (cat/dog/lizard/etc -- str), breed (tabby/retriever/etc -- str), age (int)
  - relationships: a pet belongs to an owner , a pet can be associated to one or more tasks
- Task
  - attributes: duration in minutse(int), priority (high/med/low -- str), description/type (walk/grooming/meds -- str), pet (Pet), completed (boolean)
  - methods: complete_task()
- Daily Schedule ? - should be auto generated/calculated not rly stored
  - attributes: tasks (Task[])
  - relationships: a schedule can have zero or more tasks
  - methods: generate_schedule()

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

In asking the agent to identify any missing relationships or bottlenecks, it pointed out several things.

1. Pets belong to an owner, but there is no reverse where Owners have a list of Pets. This was added during implementation.
2. The DailySchedule was further improved by associating it to an owner, a date, and the possible amount of available minutes.
3. The priority for a task was suggested to be changed from a generic string to a Enum with "High", "Medium", "Low" priorities.
4. This then inspired me to adjust the Owner preferences from a list of a strings to a more specific daytime preference enum.
5. Added a list of a pets to a Task so that Tasks can be completed for one or more pets (feeding all pets at the same time)

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler implemented considered the user's daytime preferences and adding the tasks in order of priority.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

The scheduler does not account for a specific start time for certain tasks like feeding breakfast. This tradeoff is reasonable to support the user's daytime preferences and trying to accommodate all tasks in order of priority. If a task is unable to be completed due to time constraints, it becomes user error.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

AI helped in designing the UML and ideating how the scheduler should be implemented given the provided classes and their purposes in the application. The most useful prompts were ones that were very specific in how the AI should implement the scheduler with the constraints.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

The AI was quick to implement everything after one prompt and got ahead of my development process. Rather than accepting this response, I rejected it and had it go through the process piece by piece and function by function.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested that the outputs of creating each class was as expected. These tests are important to ensure that no unexpected outputs happen, causing different behaviors in the end scheduler output.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I'm confident that the scheduler works in scheduling tasks based on daytime preference and priority. There are additional edge cases such as tasks that could not be fit in if there are too many tasks. If there was more time, I would test for edge cases such as scheduling for weekly items.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
