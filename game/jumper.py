import random
# Does jumper have parachute true or false
class Jumper:
    def __init__(self):
        self.parachute = ['''
                        ____
                        /  \
                        |  |
                        \  /
                        \ /
                         O
                        /|\
                        / \
                        ^^^^^^''', 
                        ''' ____
                        /  \
                        |  |
                        \  /
                        \ /
                         O
                        /|\
                        / \
                        ^^^^^^''',
                        '''/  \
                        |  |
                        \  /
                        \ /
                         O
                        /|\
                        / \
                        ^^^^^^''', 
                        '''|  |
                        \  /
                        \ /
                         O
                        /|\
                        / \
                        ^^^^^^''',
                        '''\  /
                        \ /
                         O
                        /|\
                        / \
                        ^^^^^^''',
                        '''\ /
                         O
                        /|\
                        / \
                        ^^^^^^''',
                        '''X
                        /|\
                        / \
                        ^^^^^^'''
        ]
    def get_parachute(self):
        return self.parachute
    
    def take_parachute(self, parachute):
        self.parachute.pop

        
        
    