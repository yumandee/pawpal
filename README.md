# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
Today's Schedule:
[12:00 PM - 12:30 PM] Feed breakfast
[12:30 PM - 1:00 PM] Feed breakfast
[1:00 PM - 1:30 PM] Feed breakfast
[1:30 PM - 2:30 PM] Walk Louie
[2:30 PM - 3:15 PM] Brush cats
[3:15 PM - 4:00 PM] Brush cats
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
========================= test session starts ==========================
platform darwin -- Python 3.13.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/mandee/codepath/pawpal
configfile: pytest.ini
plugins: anyio-4.14.1
collected 2 items

tests/test_pawpal.py ..                                          [100%]

========================== 2 passed in 0.01s ===========================
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature           | Method(s)                                                                                                      | Notes |
| ----------------- | -------------------------------------------------------------------------------------------------------------- | ----- |
| Task sorting      | by priority and daytime preference                                                                             |
| Filtering         | skip tasks if time runs out                                                                                    |       |
| Conflict handling | after daytime preference fulfilled and there are remaining tasks, add tasks starting from preference and prior |       |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Enter owner name
2. Select owner daytime preference (daytime, afternoon, nighttime) from dropdown
3. Enter pet information (name, species, & age required, breed optional)
4. Add pet
5. See pet and information in table
6. Create a task and associate it to one or more pets
7. Create more tasks as needed
8. Generate schedule from tasks provided

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or link to a demo video here -->
