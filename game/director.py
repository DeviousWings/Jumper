from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    
    def __init__(self):
        self._jumper = Jumper()
        self._is_playing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        self._correct_guess = False

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing == True:
            self._draw_board()
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
    def _draw_board(self):
        self._puzzle.draw_word_guess()
        self._jumper.draw_jumper()
    
    def _get_inputs(self):
        
        guess = self._terminal_service.read_text("\nGiess a letter [a-z]: ")
        self._correct_guess = self._puzzle.process_guess(guess)
        
    def _do_updates(self):
        if self._correct_guess == False:
            self._jumper.remove_parachute_piece()
            
        
        
    def _do_outputs(self):
        if self._correct_guess == True:
            self._terminal_service.write_text('That letter is correct')
        else:
            self._terminal_service.write_text('Sorry that letter is not part of this word.')

        if self._puzzle.can_keep_guessing() == False:
            self._terminal_service.write_text('You got the word!')
            self._puzzle.draw_word_guess()
            self._is_playing = False
            
        if self._jumper.has_parachute() == False:
            self.is_playing = False
            self._terminal_service.write_text('You suck and you lost.')
            
        