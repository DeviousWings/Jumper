# puzzle needs to be able to print out the word in blank form. It should be able to take a guess and process that guess if there are letters
#  in there. Puzzle should be able to tell the director if that guess was right or not. Should tell how many guess are in there.
# Handles the puzzle. does not deal with the jumper.
# Should have the word that is select. Hard code four letter words.
# shoudl have another variable that is identical that has been selected for the puzzle.
# ["ship", "star", "bell", "tree", "bird"]
import random

class Puzzle:
    def __init__(self):
        wordsList = ["ship", "star", "bell", "tree", "bird"]
        self.wordList = random.randint(0, len(wordsList))
        self.guess = 0
        
    def create_word(self):
        self.wordList = ["ship", "star", "bell", "tree", "bird"]

    def checkWord(self, guess):
        self.correctLetters = []
        for x in self.wordList:
            if guess == x:
                self.correctLetters.append(x)
                
        if guess in self.correctLetters:
            return True
        else:
            return False
        
        
    def completedWord(self):
        self.correctLetters = []
        correctWord = []
        
         #convert word into list
        for x in self.wordList:
            correctWord.append(x)
        
        #sort lists so we can check
        _checker = self.correctLetters.sort()
        _correct_check = correctWord.sort()

        #checks the word
        if _checker != _correct_check:
            return False
        elif _checker == _correct_check:
            return self.wordList
