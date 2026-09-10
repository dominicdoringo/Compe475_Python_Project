"""
display.py — owned by: Sakshi

Concepts demonstrated in this file:
  - Python Strings (formatting, methods)
  - Python PIP (third-party package: colorama)

PIP NOTE FOR PRESENTATION:
  This project installs a third-party package called "colorama" which lets
  us print colored text in the terminal (Windows terminals don't support
  ANSI colors by default without it). Install it with:

      pip install colorama

  Show this command running during the presentation, then show the import
  below actually being used.
"""

from colorama import init, Fore, Style

init(autoreset=True)  # colorama setup


def show_title():
    title = "PYTHON TRIVIA CHALLENGE"
    # STRING METHODS: .center(), string multiplication
    print(Fore.CYAN + "=" * 44)
    print(Fore.CYAN + title.center(44))
    print(Fore.CYAN + "=" * 44 + Style.RESET_ALL)


def show_question(number, category, question, points):
    # STRING FORMATTING: f-strings
    header = f"[Q{number}] {category} — worth {points} pts"
    print(Fore.YELLOW + header)
    print(Fore.WHITE + question.strip().capitalize())


def show_result(is_correct, correct_answer):
    if is_correct:
        print(Fore.GREEN + "Correct!")
    else:
        # STRING METHOD: .title() for nicer display of the answer
        print(Fore.RED + f"Wrong. The correct answer was: {correct_answer.title()}")


def show_badges(badges, has_badge_func, speed, streak, perfect):
    print(Fore.MAGENTA + "--- Badges Earned ---")
    if has_badge_func(badges, speed):
        print(Fore.MAGENTA + " * Speed Demon (answered fast)")
    if has_badge_func(badges, streak):
        print(Fore.MAGENTA + " * Hot Streak (3+ correct in a row)")
    if has_badge_func(badges, perfect):
        print(Fore.MAGENTA + " * Perfectionist (mastered a category)")


def show_final_score(name, score, total_possible):
    # STRING FORMATTING: multiple f-strings combined
    line = f"{name}'s final score: {score} / {total_possible}"
    print(Fore.CYAN + "=" * len(line))
    print(Fore.CYAN + line)
    print(Fore.CYAN + "=" * len(line))
