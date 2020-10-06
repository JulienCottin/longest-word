import string
import random


class Game :
    def __init__(self) :
        self.grid=[]
        for _ in range(9) :
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self,user_word) :
        if user_word == '' :
            return False
        for letter in user_word :
            if letter not in self.grid :
                return False
        return True
