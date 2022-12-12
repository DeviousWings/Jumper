# puzzle needs to be able to print out the word in blank form. It should be able to take a guess and process that guess if there are letters
#  in there. Puzzle should be able to tell the director if that guess was right or not. Should tell how many guess are in there.
# Handles the puzzle. does not deal with the jumper.
# Should have the word that is select. Hard code four letter words.
# shoudl have another variable that is identical that has been selected for the puzzle.
# ["ship", "star", "bell", "tree", "bird"]
import random
from game.terminal_service import TerminalService


class Puzzle:
    def __init__(self):
        self.terminal_service = TerminalService()
        self._words = ["ship", "star", "Gas Planet", "Nebula"]
        self._word_selected = random.choice(self._words)
        self._word_guess = ['_']* len(self._word_selected)
        
        
    def draw_word_guess(self):
        for letter in self._word_guess:
            self.terminal_service.write_text(letter)
        
    def process_guess(self, guess_letter):
        correct_guess = False
        # Loop throug _word_seleected by index
        if self._word_selected == guess_letter:
            # Check if guess_letter = _word_select[index]
            guess_letter = self._word_guess[self._words]
            # Set _word_guess[index] = guess_letter
            self._word_guess[self._words] = guess_letter
        
        
        
        return correct_guess
        
    def can_keep_guessing(self):
        return "_" in self._word_guess