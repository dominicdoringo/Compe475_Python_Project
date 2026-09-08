"""
questions.py — owned by: Data Lead

Concepts demonstrated in this file:
  - Python Dictionaries (question bank organized by category)
  - Python Tuples (each question is a fixed (question, answer, difficulty) tuple)
  - Python Sets (unique category names)
  - Python Data Types (int, str)
"""

# DICTIONARY: keys are category names (str), values are LISTS of TUPLES.
# Each TUPLE is (question_text, correct_answer, difficulty_points) — fixed,
# ordered data that should never change shape, which is exactly what a
# tuple is for.
QUESTION_BANK = {
    "Science": [
        ("What planet is known as the Red Planet?", "mars", 10),
        ("What gas do plants absorb from the air?", "carbon dioxide", 10),
        ("What is the chemical symbol for gold?", "au", 15),
        ("How many bones are in the adult human body?", "206", 15),
    ],
    "History": [
        ("In what year did World War II end?", "1945", 10),
        ("Who was the first President of the United States?", "george washington", 10),
        ("Which ancient wonder was located in Giza?", "the great pyramid", 15),
        ("What wall fell in 1989?", "berlin wall", 15),
    ],
    "Geography": [
        ("What is the longest river in the world?", "nile", 10),
        ("What is the smallest country in the world?", "vatican city", 15),
        ("Which continent is the Sahara Desert on?", "africa", 10),
        ("What is the capital of Japan?", "tokyo", 10),
    ],
}

# SET: built from the dictionary's keys. Sets automatically enforce
# uniqueness, which matches what a list of categories should be.
CATEGORIES = set(QUESTION_BANK.keys())


def get_categories():
    return CATEGORIES


def get_questions(category):
    # returns the LIST of TUPLES for a given category
    return QUESTION_BANK.get(category, [])


def total_question_count():
    total = 0
    for category in QUESTION_BANK:
        total += len(QUESTION_BANK[category])
    return total
