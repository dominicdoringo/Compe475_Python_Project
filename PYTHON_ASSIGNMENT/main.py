"""
main.py — owned by: Project Lead

Concepts demonstrated in this file:
  - Python Syntax (structure, indentation, comments)
  - Python Variables
  - Python Modules (importing our own files + a built-in module)
  - Python For Loops
  - Python If...Else
"""

import random  # built-in MODULE
import time     # built-in MODULE (used for the speed-badge timer)

import questions
import game_logic
import scoring
import display


def play_round(round_number, category, question_data, badges, streak):
    question_text, correct_answer, points = question_data

    display.show_question(round_number, category, question_text, points)

    start_time = time.time()
    user_answer = input("Your answer: ")
    seconds_taken = time.time() - start_time

    # IF...ELSE via check_answer's boolean result
    is_correct = game_logic.check_answer(user_answer, correct_answer)
    display.show_result(is_correct, correct_answer)

    points_earned = points if is_correct else 0
    scoring.record_round(points_earned)

    streak, badges = game_logic.evaluate_round(is_correct, streak, seconds_taken, badges)

    return is_correct, streak, badges


def game_loop():
    display.show_title()

    # VARIABLES
    player_name = input("Enter your name: ").strip()
    if player_name == "":
        player_name = "Player"

    badges = 0b000
    streak = 0
    round_number = 1
    rounds_to_play = 6
    total_possible = 0

    category_list = list(questions.get_categories())  # SET -> LIST conversion

    # FOR LOOP driving the trivia rounds
    for _ in range(rounds_to_play):
        category = random.choice(category_list)
        category_questions = questions.get_questions(category)

        # find a question in this category not yet asked
        available = []
        for q in category_questions:
            if not scoring.already_asked(category, q[0]):
                available.append(q)

        if not available:
            continue  # every question in this category already used

        question_data = random.choice(available)
        scoring.mark_asked(category, question_data[0])
        total_possible += question_data[2]

        is_correct, streak, badges = play_round(
            round_number, category, question_data, badges, streak
        )

        round_number += 1
        print()  # spacer

    print("\n--- GAME OVER ---")
    final_score = scoring.total_score()
    display.show_final_score(player_name, final_score, total_possible)
    scoring.summarize_history()
    display.show_badges(
        badges,
        game_logic.has_badge,
        game_logic.SPEED_BADGE,
        game_logic.STREAK_BADGE,
        game_logic.PERFECT_BADGE,
    )

    # IF...ELSE final message
    if final_score >= total_possible * 0.7:
        print("Great job — you know your stuff!")
    else:
        print("Nice try — play again to improve your score!")


if __name__ == "__main__":
    game_loop()
