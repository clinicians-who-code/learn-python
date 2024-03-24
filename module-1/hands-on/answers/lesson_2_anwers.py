""" Lesson 1 answers"""


def statement(question, answer) -> bool:
    """Checks if question and answer match"""
    global all_correct

    question_and_answer_bank: dict[str, str] = {
        "a comment is": "used to provide helpful information for your later self and others to better understand your code at a later date",
    }

    if (question, answer) in question_and_answer_bank.items():
        print(f"* Correct, '{ question } { answer }'!")
        return True

    else:
        print(
            f"* Sorry, the following statement is not correct: '{ question } { answer }'"
        )
        return False

    return


def end(all_correct):
    if all_correct:
        print("* All passed!", "\U0001f600")
    else:
        print(
            "* Sorry, there was an some errors / incorrect answers!",
            "\U0001F641",
        )
