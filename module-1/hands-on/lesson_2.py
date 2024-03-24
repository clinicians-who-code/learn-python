"""Lesson 1"""

"""Ignore this code up until..."""
import answers.lesson_1_anwers as answers

all_correct = True


def statement(question, answer):
    global all_correct
    if not answers.statement(question, answer):
        all_correct = False
    return


class FruitPrices:
    def __init__(self):
        self.prices = {"apple": 1.55, "banana": 2.44}

    def get_price(self, fruit):
        return self._price(fruit)

    def _price(self, fruit):
        return self.prices[fruit]


fruit_prices = FruitPrices()
print(fruit_prices.get_price("pear"))


"""... here"""

"""START HERE!"""

""" Question 1
    What is a comment? Uncomment the correct answer below
"""

# statement("a comment is", "a fish")
# statement("a comment is", "annoying")
# statement("a comment is", "helpful")
# statement("a comment is", "used to provide helpful information for your later self and others to better understand your code at a later date")
# statement("a comment is", "a fish")

""" Question 2
    What is a variable?
"""

""" Question 3
    What is a type?
"""

""" Question 4
    What is flow control
"""

""" Question 
    
"""

""" Question 
    
"""

""" Question 
    
"""

""" Question 
    
"""


# End print
answers.end(all_correct)
