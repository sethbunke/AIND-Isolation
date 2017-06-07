"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

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
    
    # def minimax(self, game, depth):
    #     """Test minimax implementation"""
    #     utility = game.utility(game.active_player)
    #     if utility == 0: #need to keep playing
            
            



if __name__ == '__main__':
    unittest.main()
