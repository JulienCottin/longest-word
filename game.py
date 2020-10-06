import string
import random
import requests

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
        return self.__check_dictionary(user_word)

    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
