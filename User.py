class User:
    def __init__(self, name):
        self.__name = name
        self.__score = 0

    @property
    def score(self):
        return self.__score

    @property
    def name(self):
        return self.__name

    def CorrectAnswer(self):
        self.__score = self.__score + 1
