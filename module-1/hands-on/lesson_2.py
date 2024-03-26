"""Lesson 2"""

"""Ignore this code up until..."""
import answers.lesson_1_anwers as answers

all_correct = True


def statement(Exercise, answer):
    global all_correct
    if not answers.statement(Exercise, answer):
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

""" Exercise 1
    What is a comment? Uncomment the correct answer below
"""

# statement("a comment is", "a fish")
# statement("a comment is", "annoying")
# statement("a comment is", "helpful")
# statement("a comment is", "used to provide helpful information for your later self and others to better understand your code at a later date")
# statement("a comment is", "a fish")

""" Exercise 2
    What is a variable?
"""

""" Exercise 3
    What is a type?
"""

""" Exercise 4
    What is flow control
"""

""" Exercise 
    
"""

""" Exercise 
    
"""

""" Exercise 
    
"""

""" Exercise 
    
"""


# End print
answers.end(all_correct)
