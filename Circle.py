from Shape import Shape
import utilities
import math


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__pi = 22 / 7
        self.__radius = radius

    def __perimeter(self):
        return round(self.__pi * 2 * self.__radius, 2)

    def __area(self):
        return round(self.__pi * self.__radius * self.__radius, 2)

    def check_area(self, user_input):
        return utilities.compareValues(self.__area(), user_input)

    def check_perimeter(self, user_input):
        return utilities.compareValues(self.__perimeter(), user_input)

    def CircleSelected(self):
        print("--------------------------------")
        print("Circle: Radius = ", self.__radius)
        print("--------------------------------")
        correctInputPerimeter = False
        correctInputArea = False
        while not correctInputPerimeter:
            userInputPerimeter = input("Enter Perimeter for Circle: \n")
            enteredValue = utilities.float_amount_validator(userInputPerimeter)
            if enteredValue[0]:
                correctInputPerimeter = True
                if self.check_perimeter(enteredValue[1]):
                    utilities.selected_User.CorrectAnswer()
                else:
                    print("Sorry, Wrong Answer!\nCorrect answer is {}".format(self.__perimeter()))
            else:
                print("Enter proper value.")

        while not correctInputArea:
            userInputPerimeter = input("Enter Area for Circle:\n")
            enteredValue = utilities.float_amount_validator(userInputPerimeter)
            if enteredValue[0]:
                correctInputArea = True
                if self.check_area(enteredValue[1]):
                    utilities.selected_User.CorrectAnswer()
                else:
                    print("Sorry, Wrong Answer!\nCorrect answer is {}".format(self.__area()))
            else:
                print("Enter proper value.")
