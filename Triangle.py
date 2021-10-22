from Shape import Shape
import utilities


class Triangle(Shape):
    def __init__(self, side):
        super().__init__()
        self.__side = side

    def __perimeter(self):
        return self.__side * 3

    def __area(self):
        return round((utilities.findSquareRoot(3) * (self.__side ** 2)) / 4, 2)

    def check_area(self, user_input):
        return utilities.compareValues(self.__area(), user_input)

    def check_perimeter(self, user_input):
        return utilities.compareValues(self.__perimeter(), user_input)

    def TriangleSelected(self):
        print("---------------------------------")
        print("Equilateral Triangle: side = {}".format(self.__side))
        print("---------------------------------")
        correctInputPerimeter = False
        correctInputArea = False
        while not correctInputPerimeter:
            userInputPerimeter = input("Enter Perimeter for Equilateral Triangle: \n")
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
            userInputPerimeter = input("Enter Area for Equilateral Triangle: \n")
            enteredValue = utilities.float_amount_validator(userInputPerimeter)
            if enteredValue[0]:
                correctInputArea = True
                if self.check_area(enteredValue[1]):
                    utilities.selected_User.CorrectAnswer()
                else:
                    print("Sorry, Wrong Answer!\nCorrect answer is {}".format(self.__area()))
            else:
                print("Enter proper value.")
