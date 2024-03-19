"""Lesson one code"""

import answers.lesson_1_anwers as answers

all_correct = True


def statement(question, answer):
    global all_correct

    if not answers.statement(question, answer):
        all_correct = False

    return


""" Lesson 1.1
    What is a comment? Uncomment the correct answer below
"""

# statement("a comment is", "a fish")
# statement("a comment is", "annoying")
# statement("a comment is", "helpful")
# statement("a comment is", "used to provide helpful information for your later self and others to better understand your code at a later date")
# statement("a comment is", "a fish")


# End print
answers.end(all_correct)
