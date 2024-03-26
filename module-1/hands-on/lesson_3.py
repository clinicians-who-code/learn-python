"""Lesson 3

Let's build an app. Some useful link

https://pathlabs.rlbuht.nhs.uk/eGFRcalculator.htm
https://www.nhs.uk/conditions/kidney-disease/diagnosis/
"""

import streamlit as st

"""Exercise 1 - 'Hello world!' web app style!
Run the app using the command:
$ streamlit run lesson_3.py
"""


"""def main():
    st.write(f"Hello world!")
    return


if __name__ == "__main__":
    main()"""

"""Exercise 2 
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below
"""

"""
# Write a function named 'calculate_egfr'.
# Define a variable in this function called egfr and set it to '45'.
# Have this function return egfr.


def main():
    # Call the 'calculate_egfr' function above
    # Print the returned value to the browser
    return


if __name__ == "__main__":
    main()

# Run the above code and see if you have the nubmer 45 in the browser window
"""

"""Exercise 3
1. Comment out the above code.
2. Uncomment the code below
3. Follow the steps below
"""


# Add arguements 'creatinine, age, gender, race' to function below
def calculate_egf():
    egfr = 45
    return egfr


def main():
    egfr = calculate_egf()
    st.write(f"{egfr}")
    return


if __name__ == "__main__":
    main()
