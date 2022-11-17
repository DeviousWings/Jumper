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
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
    def _get_inputs(self):
        
        letter = self._terminal_service.read_word("\nGiess a letter [a-z]: ")
        self._puzzle.guess_letter(letter)
        
    def _do_updates(self):
        self._jumper.puzzle_guess(self._puzzle)
        
    def _do_outputs(self):
        hint = self._jumper.get_hint()
        self._terminal_service.write_text(hint)
        if self._jumper.is_found():
            self.is_playing = False