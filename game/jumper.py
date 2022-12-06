from game.terminal_service import TerminalService
# Does jumper have parachute true or false
class Jumper:
    def __init__(self):
        self.parachute = ['____',
                        '/  \ ',
                        '|  |',
                        '\  /',
                        '\ /',
                        ' O',
                        '/|\ ',
                        '/ \ ',
                        '',
                     '^^^^^^']
        self.terminal_service = TerminalService()
        
    def draw_jumper(self):
        for line in self.parachute:
            self.terminal_service.write_text(line)
                    
    def remove_parachute_piece(self):
        return self.parachute.pop(0)
    
    def has_parachute(self):
        return len(self.parachute) >= 6
    
    def parachute_gone(self):
       self.parachute[0].replac(' O', ' X')
       