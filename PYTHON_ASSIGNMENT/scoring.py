# scoring.py - Ethan Garcia
# Concepts demonstrated in this file:
# Python Sets (tracking asked questions + mastered categories)
# Python For Loops
# Python Lists (score history)
# Python Functions

# Set for questions that were already asked
# main.py uses this so questions do not repeat
asked_questions = set()

# List for saving the points from each round
# main.py adds each round's score here
score_history = []

# Set for categories the player answered completely correctly
mastered_categories = set()

# Mark a question as already asked
# main.py calls this after choosing a question
def mark_asked(category, question_text):
    # Store the category and question together as a tuple
    question_key = (category, question_text)
    # Add the tuple to the set
    asked_questions.add(question_key)


# Check if a question was already asked
# main.py uses this before choosing a question
def already_asked(category, question_text):
    # Create the same tuple used in mark_asked
    question_key = (category, question_text)
    # Return True if the question is already in the set
    return question_key in asked_questions

# Save the points earned in the current round
# main.py calls this AFTER the player answers
def record_round(points_earned):
    # Adds the points to the score history list
    score_history.append(points_earned)

# Add up the player's total score
# main.py sends this score to display.py
def total_score():
    # Start the total score at 0
    total = 0
    # Go through each score in the list
    for points in score_history:
        # For loop to add the current score to the total
        total += points
    # Send the total score back to main.py
    return total

# Check if every question in a category was correct
def check_category_mastery(category, questions_in_category, correct_in_category):
    # Count the questions in the category
    total_questions = len(questions_in_category)
  
    # Check that the category is not empty
    # Also check that every question was correct
    if total_questions > 0 and correct_in_category == total_questions:
        # Add the category to the mastered categories set if all questions correct and > 0
        mastered_categories.add(category)
        # Return True for a mastered category
        return True
    # Return False if the category was not mastered
    return False

# Show the score from each round
# main.py calls this near the end of the game
def summarize_history():
    # Print a heading for the score history
    print("    Round-by-round scores    ")

    # Start the round count at one onwards
    round_number = 1

    # Go through every score in the list
    for points in score_history:
        # Print the round number and score
        print(f"Round {round_number}: {points} points")
        # Move to the next round
        round_number += 1
