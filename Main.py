from Circle import Circle
from User import User
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle
import utilities
from prettytable import PrettyTable

userList = []


def askQuestion(countShape):
    shapes = utilities.getRandomShape(countShape)
    for shape in shapes:
        if shape == "Circle":
            radius = utilities.getRandomInt()
            circle = Circle(radius)
            circle.CircleSelected()
        elif shape == "Square":
            width = utilities.getRandomInt()
            square = Square(width=width)
            square.SquareSelected()
        elif shape == "Rectangle":
            width = utilities.getRandomInt()
            length = utilities.getRandomInt()
            rectangle = Rectangle(width=width, length=length)
            rectangle.RectangleSelected()
        elif shape == "Triangle":
            side = utilities.getRandomInt()
            triangle = Triangle(side)
            triangle.TriangleSelected()
        else:
            print()

    print("***********************************")
    print("Hello {}!! Your score is {}.".format(utilities.selected_User.name, utilities.selected_User.score))
    print("***********************************")
    nextRound()


def RegisterUser():
    input_name = input("Please enter your name:\n")
    user = User(name=input_name)
    userList.append(user)
    utilities.selected_User = user
    print("Welcome {}, your initial score is {}".format(user.name, user.score))
    StartGame()


def StartGame():
    correct_details = False
    while not correct_details:
        input_shapeCount = input("Enter number of shapes you wants to play:\n")
        rounds = utilities.int_Validator(input_shapeCount)
        if rounds[0]:
            correct_details = True
            askQuestion(rounds[1])
        else:
            pass


def nextRound():
    correct_input = False
    while not correct_input:
        print("Do you wants to play next round?")
        strValue = input("Press 'y' for YES and 'n' for NO \n").lower()
        if strValue == 'y':
            correct_input = True
            StartGame()
        elif strValue == 'n':
            correct_input = True
            get_Menu()
        else:
            print("Please enter correct input. 'y' or 'n'\n")


def show_Score():
    if len(userList) > 0:
        print("Score board:")
        my_table = PrettyTable()
        my_table.field_names = ["User.", "Score"]
        for objUser in userList:
            my_table.add_row([objUser.name, objUser.score])
        print(my_table)
    else:
        print("No user found in system.")
    get_Menu()


def get_Menu():
    print("1. Register User")
    print("2. Show Score")
    print("3. Quit")
    correct_input = False
    while not correct_input:
        selectedOption = input("Please enter valid choice from above options:\n")
        enteredValue = utilities.int_Validator(selectedOption)
        if enteredValue[0]:
            correct_input = True
            if enteredValue[1] == 1:
                RegisterUser()
            elif enteredValue[1] == 2:
                show_Score()
            elif enteredValue[1] == 3:
                print("Hope you enjoyed. Come soon!!")
        else:
            pass


if __name__ == '__main__':
    print("********************************")
    print("*****Welcome to Shape Game******")
    print("********************************")
    get_Menu()
