from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    
    def __init__(self):
        self._jumper = Jumper()
        self.is_playing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
    def _get_inputs(self):
        
        guess = self._terminal_service.read_text("\nGiess a letter [a-z]: ")
        self._puzzle.process_guess(guess)
        
    def _do_updates(self):
        if self._puzzle.process_guess is False:
            self._jumper.remove_parachute_piece
        
    def _do_outputs(self):
        if self._puzzle is True:
            self._terminal_service.write_text('That letter is correct')
        else:
            self._terminal_service.write_text('Sorry that letter is not part of this word.')
        
        self._terminal_service.write_text(self._jumper.remove_parachute_piece())


        if self._puzzle.can_keep_guessing():
            self._terminal_service.write_text('You got it!')
            self._terminal_service.write_text(self._puzzle.can_keep_guessing())
            self._is_playing = False