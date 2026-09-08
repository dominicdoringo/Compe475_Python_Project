# Python Trivia Challenge — Concept Map for Presentation

Run with: `pip install colorama` then `python3 main.py`

| # | Concept | File | Where |
|---|---------|------|-------|
| 1 | Python Syntax | main.py | whole file: indentation, comments, structure |
| 2 | Python Variables | main.py | `player_name`, `round_number`, `rounds_to_play` |
| 3 | Python Data Types | questions.py | int (points), str (questions), bool (used elsewhere) |
| 4 | Python Strings | display.py | `show_question()`, `.center()`, `.title()`, f-strings |
| 5 | Python Operators (logical) | game_logic.py | `check_answer()`, `can_earn_speed_badge()` — `and`/`or`/`not` |
| 5b| Python Operators (bitwise) | game_logic.py | `award_badge/remove_badge/has_badge/toggle_streak_badge` — `&` `|` `^` `~` |
| 6 | Python Lists | scoring.py / main.py | `score_history`, `category_list` |
| 7 | Python Tuples | questions.py | each question is `(question, answer, points)` |
| 8 | Python Sets | questions.py / scoring.py | `CATEGORIES`, `asked_questions`, `mastered_categories` |
| 9 | Python Dictionaries | questions.py | `QUESTION_BANK` |
| 10| Python If...Else | main.py / game_logic.py | round handling, `evaluate_round()`, final message |
| 11| Python Functions | all files | every `def` |
| 12| Python For Loops | main.py / scoring.py | round loop, `total_question_count()`, `summarize_history()` |
| 13| Python Modules | main.py | `import random`, `import time`, `import questions`, etc. |
| 14| Python PIP | display.py | `pip install colorama`, `from colorama import ...` |

## Suggested 5-way split (already reflected in file headers)
1. **Project Lead** — main.py (syntax, variables, modules, for loops, if/else)
2. **Data Lead** — questions.py (dicts, tuples, sets, data types)
3. **Logic Lead** — game_logic.py (logical + bitwise operators, if/else)
4. **Functions & Sets Lead** — scoring.py (sets, for loops, lists, functions)
5. **Strings/PIP/Polish Lead** — display.py (strings, PIP) + assemble the slide above

## How the game works
- 6 rounds are played, each pulling a random question from a random category.
- Questions already asked are tracked in a set so they never repeat.
- Answering correctly builds a streak; 3+ in a row earns a "Hot Streak" badge.
- Answering within 8 seconds earns a "Speed Demon" badge.
- Badges are stored as bits in a single integer (see game_logic.py) — a
  clean, real example of bitwise operators.
  - This code uses

## For the presentation
For each concept, open the file, point at the line, and say what it does.
Don't just name it on a slide — the assignment requires showing it in
running code.
