# AI Learning Journal

## Day 1

- Installed Python, VS Code, Git
- Learned basic Python input/output
- Used GitHub Copilot for the first time

## Day 2

- Learned VS Code shortcuts (Command Palette, formatting)
- Improved Python code structure
- Used GitHub Copilot to generate a function
- Built a small logic (birth year calculator)

## Day 3

- Learned proper function structure
- Broke code into reusable components
- Used Copilot to build logic (is_adult)
- Practiced refactoring using VS Code rename

## Day 4

- Learned about Dictionaries and Lists
- Used Copilot to generate code for handling user input and storing data
- for loop to iterate through lists
- alt click for multi cursor editing

## Day 5

- **JSON Library:** Learned to use Python's built-in `json` module for data serialization and deserialization.
- **File Handling:** Used `with open()` context manager for safe file operations.
- **Writing JSON:** Used `json.dump()` to save Python dictionaries to a `.json` file.
- **Reading JSON:** Used `json.load()` to parse JSON data from a file back into Python objects.
- **Pretty Printing:** Added `indent=4` parameter for human-readable JSON output.
- **Read/Write Modes:** Understood `"w"` (write/overwrite) vs `"r"` (read) file modes.
- **Error Handling:** Implemented `try...except` blocks to handle `FileNotFoundError` when loading data.

## Day 6

- **While Loops:** Practiced `while` loops for continuous execution and control flow.
- **Input Validation:** Used `.isdigit()` to verify numeric user input before processing.
- **Type Conversion:** Used `int()` and `float()` functions to convert strings to appropriate data types.
- **Error Handling:** Implemented `try...except` blocks to gracefully catch `ValueError` and prevent crashes.
- **Robust Scripts:** Combined loops, validation, and exception handling to build resilient input prompts.

## Day 7

- Refactored project into multiple files
- Learned modular programming
- Separated logic and file handling
- Improved project structure

## Day 8

- Integrated AI API (OpenRouter)
- Built ai_service module
- Sent prompts and received responses
- Connected AI with user data
- Used api key in .env file for secure access

## 📅 Day 9 – AI Prompt System (Foundation)

### 🔍 What we did

- Introduced a **structured way to use AI** instead of random prompts
- Created reusable components:
  - **Persona** → defines how AI should behave
  - **Rules** → controls AI output quality
  - **Prompt templates** → reusable task definitions
- Built a simple workflow:
  > Persona + Rules + Task + Data → AI Output

---

### 🎯 Why we did this

- Raw AI usage gives **generic, inconsistent results**
- Structured prompts ensure:
  - **Consistent output**
  - **Better quality responses**
  - **Reusability across use cases**

---

### 🧠 Key Learning

> AI is not plug-and-play — it must be **guided with structure, context, and constraints** to produce useful results.
