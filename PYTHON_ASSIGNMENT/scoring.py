"""
scoring.py — owned by: Functions & Sets Lead

Concepts demonstrated in this file:
  - Python Sets (tracking asked questions + mastered categories)
  - Python For Loops
  - Python Lists (score history)
  - Python Functions
"""

# SET: stores (category, question_text) pairs already asked, so the same
# question never repeats in one game. Sets are ideal here because
# membership checks ("have we asked this already?") need to be fast and
# duplicates must be impossible.
asked_questions = set()

# LIST: keeps a running history of points earned per round, in order.
score_history = []

# SET: categories where the player answered every question correctly.
mastered_categories = set()


def mark_asked(category, question_text):
    asked_questions.add((category, question_text))


def already_asked(category, question_text):
    return (category, question_text) in asked_questions


def record_round(points_earned):
    score_history.append(points_earned)


def total_score():
    total = 0
    # FOR LOOP over the list
    for points in score_history:
        total += points
    return total


def check_category_mastery(category, questions_in_category, correct_in_category):
    # FOR LOOP-style comparison: if every question in this category was
    # answered correctly, the player "masters" it.
    if correct_in_category == len(questions_in_category) and len(questions_in_category) > 0:
        mastered_categories.add(category)
        return True
    return False


def summarize_history():
    print("--- Round-by-round scores ---")
    round_number = 1
    # FOR LOOP printing each entry with its round number
    for points in score_history:
        print(f"Round {round_number}: {points} points")
        round_number += 1
