from game.terminal_service import TerminalService
# Does jumper have parachute true or false
class Jumper:
    def __init__(self):
        self.terminal_service = TerminalService()
        self._parachute = ['____',
                        '/  \ ',
                        '|  |',
                        '\  /',
                        '\ /',
                        ' O',
                        '/|\ ',
                        '/ \ ',
                        '',
                     '^^^^^^']
        
    def draw_jumper(self):
        for line in self._parachute:
            self.terminal_service.write_text(line)
                    
    def remove_parachute_piece(self):
        return self._parachute.pop(0)
    
    def has_parachute(self):
        return len(self._parachute) >= 6
    
    def parachute_gone(self):
       self._parachute[0].replace(' O', ' X')
       