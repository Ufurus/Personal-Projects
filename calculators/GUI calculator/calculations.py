""""
This is the main logic of the application. It is the place where
it will be calculated and then return a result.
"""

import buttons

numbers = []
counter = 1

def render_result(button):

    if button not in "+-*X/%" or "//":
        if counter % 2 == 1:
            if button not in numbers:
                numbers.append(button)
            numbers[0] += button

    elif button == "=":
        pass

    else:
        pass
