# puzzle needs to be able to print out the word in blank form. It should be able to take a guess and process that guess if there are letters
#  in there. Puzzle should be able to tell the director if that guess was right or not. Should tell how many guess are in there.
# Handles the puzzle. does not deal with the jumper.
# Should have the word that is select. Hard code four letter words.
# shoudl have another variable that is identical that has been selected for the puzzle.
# ["ship", "star", "bell", "tree", "bird"]
import random

class Puzzle:
    def __init__(self):
        self.wordList = ["ship", "star", "bell", "tree", "bird"]
        self.wordIndex = random.randint(0, len(self.wordList))
        self.guess = 0

    def getGuess(self):
        while True:
            print('')