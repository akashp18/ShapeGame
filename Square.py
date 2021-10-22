from Shape import Shape
import utilities


class Square(Shape):
    def __init__(self, width):
        super().__init__()
        self.__width = width

    def __perimeter(self):
        return 4 * self.__width

    def __area(self):
        return self.__width * self.__width

    def check_area(self, user_input):
        return utilities.compareValues(self.__area(), user_input)

    def check_perimeter(self, user_input):
        return utilities.compareValues(self.__perimeter(), user_input)

    def SquareSelected(self):
        print("-------------------------------")
        print("Square: length = ", self.__width)
        print("-------------------------------")
        correctInputPerimeter = False
        correctInputArea = False
        while not correctInputPerimeter:
            userInputPerimeter = input("Enter Perimeter for Square:\n")
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
            userInputPerimeter = input("Enter Area for Square: \n")
            enteredValue = utilities.float_amount_validator(userInputPerimeter)
            if enteredValue[0]:
                correctInputArea = True
                if self.check_area(enteredValue[1]):
                    utilities.selected_User.CorrectAnswer()
                else:
                    print("Sorry, Wrong Answer!\nCorrect answer is {}".format(self.__area()))
            else:
                print("Enter proper value.")
