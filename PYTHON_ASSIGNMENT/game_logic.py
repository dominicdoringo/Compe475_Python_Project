"""
game_logic.py — owned by: Logic Lead

Concepts demonstrated in this file:
  - Python Operators: logical (and, or, not) AND bitwise (&, |, ^, ~)
  - Python If...Else
  - Python Functions
  - Python Data Types (bool)
"""

# Badges are stored as bits inside a single integer, the same idea as
# "achievements" flags. Packing multiple true/false badges into one int
# is a classic real-world use of bitwise operators.
SPEED_BADGE   = 0b001   # answered fast
STREAK_BADGE  = 0b010   # 3+ correct in a row
PERFECT_BADGE = 0b100   # got every question in a category right


def award_badge(badges, flag):
    # Bitwise OR (|) turns a badge ON without disturbing other bits.
    return badges | flag


def remove_badge(badges, flag):
    # Bitwise AND (&) with inverted flag (~) turns a badge OFF.
    return badges & ~flag


def has_badge(badges, flag):
    # Bitwise AND (&) checks whether a specific bit is set.
    return (badges & flag) != 0


def toggle_streak_badge(badges):
    # Bitwise XOR (^) flips a bit: on -> off, off -> on.
    return badges ^ STREAK_BADGE


def check_answer(user_answer, correct_answer):
    # STRING cleanup + LOGICAL OPERATORS
    cleaned = user_answer.strip().lower()
    target = correct_answer.strip().lower()
    is_correct = (cleaned == target) or (cleaned in target and len(cleaned) > 3)
    return is_correct


def can_earn_speed_badge(seconds_taken, answered_correctly):
    # LOGICAL OPERATORS: and / not
    fast_enough = seconds_taken <= 8
    return answered_correctly and fast_enough


def evaluate_round(is_correct, streak, seconds_taken, badges):
    # IF...ELSE: decision-making logic for scoring and badges
    if is_correct:
        streak += 1
        if can_earn_speed_badge(seconds_taken, is_correct):
            badges = award_badge(badges, SPEED_BADGE)
        if streak >= 3 and not has_badge(badges, STREAK_BADGE):
            badges = award_badge(badges, STREAK_BADGE)
    else:
        streak = 0
        if has_badge(badges, STREAK_BADGE):
            badges = remove_badge(badges, STREAK_BADGE)

    return streak, badges
