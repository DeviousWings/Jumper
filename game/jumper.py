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
        return self.parachute.pop(0)
    
    def take_parachute(self):
        self.parachute[0]

        
        
    