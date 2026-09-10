"""
main.py — owned by: Project Lead

Concepts demonstrated in this file:
  - Python Syntax (structure, indentation, comments)
  - Python Variables
  - Python Modules (importing our own files + a built-in module)
  - Python For Loops
  - Python If...Else

NOTE: every line that reaches into another file is marked with
"--> <filename>" so you can see the delegation at a glance.
"""

import random  # built-in MODULE
import time     # built-in MODULE (used for the speed-badge timer)

import questions
import game_logic
import scoring
import display


def play_round(round_number, category, question_data, badges, streak):
    # unpack the TUPLE that questions.py built
    question_text, correct_answer, points = question_data

    # --> display.py : print the question header and text
    display.show_question(round_number, category, question_text, points)

    start_time = time.time()                      # --> time (built-in)
    user_answer = input("Your answer: ")
    seconds_taken = time.time() - start_time      # --> time (built-in)

    # --> game_logic.py : is the typed answer correct?
    is_correct = game_logic.check_answer(user_answer, correct_answer)

    # --> display.py : tell the player right or wrong
    display.show_result(is_correct, correct_answer)

    points_earned = points if is_correct else 0

    # --> scoring.py : add this round's points to the history list
    scoring.record_round(points_earned)

    # --> game_logic.py : update streak + badge bits
    streak, badges = game_logic.evaluate_round(is_correct, streak, seconds_taken, badges)

    return is_correct, streak, badges


def game_loop():
    # --> display.py : print the banner
    display.show_title()

    # VARIABLES
    player_name = input("Enter your name: ").strip()
    if player_name == "":
        player_name = "Player"

    badges = 0b000
    streak = 0
    round_number = 1
    rounds_to_play = 3
    total_possible = 0

    # --> questions.py : get the SET of categories, convert to LIST
    category_list = list(questions.get_categories())

    # OUTER FOR LOOP: one pass per round
    for _ in range(rounds_to_play):
        category = random.choice(category_list)          # --> random (built-in)

        # --> questions.py : all questions for that category
        category_questions = questions.get_questions(category)

        # INNER FOR LOOP: keep only questions we haven't asked yet
        available = []
        for q in category_questions:
            # --> scoring.py : have we already used this one?
            if not scoring.already_asked(category, q[0]):
                available.append(q)

        if not available:
            continue  # every question in this category already used

        question_data = random.choice(available)         # --> random (built-in)

        # --> scoring.py : remember we've now used this question
        scoring.mark_asked(category, question_data[0])

        total_possible += question_data[2]

        # call our own play_round() for one full question
        is_correct, streak, badges = play_round(
            round_number, category, question_data, badges, streak
        )

        round_number += 1
        print()  # spacer

    print("\n--- GAME OVER ---")

    # --> scoring.py : add up every round
    final_score = scoring.total_score()

    # --> display.py : final score banner
    display.show_final_score(player_name, final_score, total_possible)

    # --> scoring.py : round-by-round breakdown
    scoring.summarize_history()

    # --> display.py : badge list (has_badge + flags come from game_logic.py)
    display.show_badges(
        badges,
        game_logic.has_badge,
        game_logic.SPEED_BADGE,
        game_logic.STREAK_BADGE,
        0,  # Perfectionist badge not used in this version
    )

    # IF...ELSE final message
    if final_score >= total_possible * 0.7:
        print("Great job — you know your stuff!")
    else:
        print("Nice try — play again to improve your score!")


if __name__ == "__main__":
    game_loop()