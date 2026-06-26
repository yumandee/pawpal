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

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

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
