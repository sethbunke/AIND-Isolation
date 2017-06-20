"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

import random
from random import randint

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def getActivePlayerLegalMoves(self):
        legal_moves = self.game.get_legal_moves(self.game.active_player)
        return legal_moves
    
    def test_split(self):
        """ Test split """        
        legal_moves = self.getActivePlayerLegalMoves();
        self.assertTrue(len(legal_moves) == 49)
        print(legal_moves)

        ret_score = float('-inf') if True else float('inf')
        print(ret_score)

        legal_moves_length = len(legal_moves)
        move_index = randint(0, legal_moves_length)
        print(move_index)


        x = (-1, -1) 
        y = (3, 2)
        result = x == y

        print(result)

        game = self.game

        # w, h = game.width / 2., game.height / 2.        
        # y, x = game.get_player_location(game.active_player)
        # print(float((h - y)**2 + (w - x)**2))


        center = int((game.width / 2) + 0.5)

        positions = [[1, 2], [3, 3], [4, 4], [8, 1]]

        #result = (center, center) in yy
        center_tuple = (center, center)
        result = [pos for pos in positions if pos[0] == center_tuple[0] and pos[1] == center_tuple[1]]
        # found = []
        # for item in yy:
        #     if item[0] == center_tuple[0] and item[1] == center_tuple[1]:
        #         found.append(item)
        print(center_tuple[0])
        #print(result[1])
        print(result)

        col_row_indexes = [0, game.width - 1]

        no_reflect = []

        index = 1
        while index < game.width:
            print(index)
            for inner_index in col_row_indexes:
                no_reflect.append((index, inner_index))
                no_reflect.append((inner_index, index))
            index += 2
        

        print(no_reflect)

        intersect = list(set(no_reflect) & set(self.getActivePlayerLegalMoves()))
        print(intersect)




    
    # def minimax(self, game, depth):
    #     """Test minimax implementation"""
    #     utility = game.utility(game.active_player)
    #     if utility == 0: #need to keep playing
            
            



if __name__ == '__main__':
    unittest.main()
