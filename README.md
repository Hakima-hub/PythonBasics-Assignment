# Python Basics Tasks

Python exercise covering core python fundamentals: conditionals,
loops, strings, lists, functions (including lambdas), dictionaries, OOP with
encapsulation.

Each task lives in its own script so it can be run and reviewed independently.

## Requirements

- Python 3.10 (Task 1 uses `match`/`case`, added in 3.10)
- No external dependencies — standard library only

## Setup

```bash
git clone <your-repo-url>
cd python-basics-tasks
```

No virtual environment or `pip install` is needed since everything uses the
standard library.

## Usage

Run any task script directly:

```bash
python3 task1
python3 task2
python3 task3
python3 task4.py
python3 task5.py
python3 task6.py
```

Tasks 1 and 3 prompt for user input. The rest run with pre-set sample data
so they can be executed and reviewed without typing anything in.

## Task overview

| File | Description |
|---|---|
| `task1` | Takes name/age/marks; reports Minor vs Adult (`if`/`else`) and a letter grade (`match`/`case`). |
| `task2` | Prints numbers 1–30, filters multiples of 3, and counts them. |
| `task3` | Character count, vowel count, middle/first-4 characters, last 2 characters, and a palindrome check. |
| `task4.py` | A 5-integer list with a normal function for max/sum, plus a `lambda` for palindrome checking. |
| `task5.py` | Builds a `student` dictionary, updates marks, adds a grade, and loops over key–value pairs. |
| `task6.py` | `BankAccount` class with a private `__balance` (encapsulation), plus a `BankCustomer`/`Bank` simulation supporting many owners, each with multiple accounts (e.g. local plus multicurrency), and a `transfer` between accounts. |
| 

## Assumptions

- Task 3's "middle characters" returns the true middle characters for strings
  of length 5+, and falls back to the first 4 characters for shorter strings,
  per the task's "middle **or** first 4" wording.
- Task 6's `transfer` method is a simplified core transaction between two
  accounts of the *same* currency — no FX conversion, fees, or auth/security
  layers, since the task scope explicitly excludes security concerns.
- All scripts were tested manually on Python 3.10.
