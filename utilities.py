import random
from User import User
import math

selected_User = User


def int_Validator(input_amount):
    try:
        selected_int = int(input_amount)
        if selected_int < 0:
            print("Negative value detected.")
            return False, 0
        else:
            return True, selected_int
    except ValueError:
        print("Please enter number.")
        return False, 0


def float_amount_validator(input_amount):
    try:
        new_amount = float(input_amount)
        return True, new_amount
    except ValueError:
        return False, 0


def getRandomShape(count):
    shapeList = []
    for x in range(count):
        # ["Circle", "Square", "Rectangle", "Triangle"]
        shapeList.append(random.choice(["Circle", "Square", "Rectangle", "Triangle"]))
    return shapeList


def getRandomInt():
    return random.randrange(1, 100)


def compareValues(value1, value2):
    return math.isclose(value1, value2, rel_tol=0.01)


def findSquareRoot(value):
    return math.sqrt(value)
