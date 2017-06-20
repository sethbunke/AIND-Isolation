"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
from random import randint


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """    
    # if game.is_loser(player):
    #     return float("-inf")

    # if game.is_winner(player):
    #     return float("inf")

    # return float(len(game.get_legal_moves(player)))

    #Compare number of "no reflect positions" of agent and opponent
    col_row_indexes = [0, game.width - 1]
    no_reflect = []

    index = 1
    while index < game.width:
        #print(index)
        for inner_index in col_row_indexes:
            no_reflect.append((index, inner_index))
            no_reflect.append((inner_index, index))
        index += 2

    player_intersect = list(set(no_reflect) & set(game.get_legal_moves(player)))
    opponent_intersect = list(set(no_reflect) & set(game.get_legal_moves(game.get_opponent(player))))
    return float(len(player_intersect) - len(opponent_intersect))

    # #RATIO
    # open_spaces = len(game.get_blank_spaces())

    # player_moves = len(game.get_legal_moves(player))
    # opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    # player_ratio = float(player_moves/open_spaces)
    # opponent_ratio = float(opponent_moves/open_spaces)

    # return player_ratio - opponent_ratio


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # player_moves = len(game.get_legal_moves(player))
    # opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    # return float(player_moves - opponent_moves)
    # if game.is_winner(player) or game.is_loser(player):
    #     return game.utility(player)

    # player_moves = game.get_legal_moves()
    # #opponent_moves = game.get_legal_moves(game.inactive_player)
    # open_spaces = game.get_blank_spaces()
    # return float (len(player_moves) - (len (open_spaces)/2))

    #Determine if agent or opponent has the center position in their list of legam moves
    center = int((game.width / 2) + 0.5)
    center_tuple = (center, center)

    #Calculate for player
    player_legal_moves = game.get_legal_moves(player)
    player_result = [pos for pos in player_legal_moves if pos[0] == center_tuple[0] and pos[1] == center_tuple[1]]
    player_weight = 1

    if len(player_result) > 0:
        player_weight = 10

    #Calculate for opponent
    opponent_legal_moves = game.get_legal_moves(game.get_opponent(player))
    opponent_result = [pos for pos in opponent_legal_moves if pos[0] == center_tuple[0] and pos[1] == center_tuple[1]]
    opponent_weight = 1

    if len(opponent_result) > 0:
        opponent_weight = -10

    player_value = len(player_legal_moves) * player_weight
    opponent_value = len(opponent_legal_moves) * opponent_weight

    return float(player_value - opponent_value)

def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # player_moves = len(game.get_legal_moves(player))
    # opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    # return float(player_moves - (2 * opponent_moves))

    # player_moves = len(game.get_legal_moves(player))
    # opponent_moves = len(game.get_legal_moves(game.get_opponent(player)))

    # if player_moves == opponent_moves:
    #     return float("inf")

    # return float(player_moves - (2 * opponent_moves))

    #Look at the intersection of legal moves for the players and "no reflect" positions
    #Additionally, add additional weight if that player's moves contains the center
    center = int((game.width / 2) + 0.5)
    center_tuple = (center, center)

    #Calculate for player
    player_legal_moves = game.get_legal_moves(player)
    player_result = [pos for pos in player_legal_moves if pos[0] == center_tuple[0] and pos[1] == center_tuple[1]]
    player_weight = 1

    if len(player_result) > 0:
        player_weight = 10

    #Calculate for opponent
    opponent_legal_moves = game.get_legal_moves(game.get_opponent(player))
    opponent_result = [pos for pos in opponent_legal_moves if pos[0] == center_tuple[0] and pos[1] == center_tuple[1]]
    opponent_weight = 1

    if len(opponent_result) > 0:
        opponent_weight = -10

    col_row_indexes = [0, game.width - 1]

    no_reflect = []

    index = 1
    while index < game.width:
        for inner_index in col_row_indexes:
            no_reflect.append((index, inner_index))
            no_reflect.append((inner_index, index))
        index += 2

    player_intersect = list(set(no_reflect) & set(player_legal_moves))
    opponent_intersect = list(set(no_reflect) & set(opponent_legal_moves))

    player_value = len(player_intersect) * player_weight
    opponent_value = len(opponent_intersect) * opponent_weight

    return float(player_value - opponent_value)

class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        move = (-1, -1)
        legal_moves = game.get_legal_moves()
        if len(legal_moves) == 0:
            return move
        #because move by first player is a maximizing
        score_i, move = max((self.min_value(game, p, depth-1), p) for p in legal_moves)
        return move
        #raise NotImplementedError

    def min_value(self, game, move, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        game_tmp = game.forecast_move(move)

        legal_moves = game_tmp.get_legal_moves()
        score_i = float("inf")

        if depth == 0:
            return self.score(game_tmp, self) #PA passed

        for p in legal_moves:
            score_i = min(score_i, self.max_value(game_tmp, p, depth-1))
        return score_i

    def max_value(self, game, move, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        game_tmp = game.forecast_move(move)

        legal_moves = game_tmp.get_legal_moves()
        score_i = float("-inf")

        if depth == 0:
            return self.score(game_tmp, self) #PA passed

        for p in legal_moves:
            score_i = max(score_i, self.min_value(game_tmp, p, depth-1))
        return score_i


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.

            search_depth = 1
            while True:
                result = self.alphabeta(game, search_depth)
                best_move = result
                search_depth += 1

        except SearchTimeout:
            pass
            # Handle any actions required after timeout as needed

        legal_moves = game.get_legal_moves()
        legal_moves_length = len(legal_moves)

        #See if there is at least some move that we can make
        if (best_move == (-1, -1)) and (legal_moves_length > 0):
            best_move = legal_moves[randint(0, legal_moves_length - 1)]

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        move = (-1, -1)
        legal_moves = game.get_legal_moves()

        if len(legal_moves) == 0:
            return move

        best_value = float("-inf")
        for p in legal_moves:
            score = self.min_value(game, p, depth-1, alpha, beta)
            if score > best_value:
                best_value = score
                move = p
            #also you need to update alpha
            alpha = max(alpha, score)

        return move        

    def min_value(self, game, move, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        game_tmp = game.forecast_move(move)

        legal_moves = game_tmp.get_legal_moves()
        value = float("inf")

        if depth == 0:
            return self.score(game_tmp, self) #PA passed

        for move in legal_moves:
            value = min(value, self.max_value(game_tmp, move, depth-1, alpha, beta))
            if value <= alpha:
                return value

            beta = min(beta, value)
        return value

    def max_value(self, game, move, depth, alpha, beta):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        game_tmp = game.forecast_move(move)

        legal_moves = game_tmp.get_legal_moves()
        value = float("-inf")

        if depth == 0:
            return self.score(game_tmp, self) #PA passed

        for move in legal_moves:
            value = max(value, self.min_value(game_tmp, move, depth-1, alpha, beta))
            if value >= beta:
                return value

            alpha = max(alpha, value)
        return value
