import random


X = "x"
O = "o"
EMPTY = " "
NUM_OF_POSITIONS = 9
WINNING_ROW_POSITIONS = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
)


def create_board(board_str):
    """create board representation of board string
    returns a list of string representing board characters
    of 'x', 'o' and space ' '.
    An empty space list is added so that board index starts at 1.
    >>> create_board(" xxo  o  ")
    >>> [" ", " ", "x", "x", "o", " ", " ", "o", " "]
    """
    board = [" "]
    board.extend(list(board_str))
    return board


def player_has_a_win(board):
    """check if a player already has three marks
    in a row(horizontally, vertically, diagonally).
    If yes, then there is no need to proceed with the
    game.
    >>> player_has_a_win("xxxoo   ")
    >>> True
    >>> player_has_a_win("xxo o o  ")
    >>> True
    >>> player_has_a_win(" xxo  o  ")
    >>> False
    """
    for row in WINNING_ROW_POSITIONS:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            return True
    return False


def select_random_move(available_moves):
    """Select randomly the available position
    in a given row
    """
    print(available_moves)
    return random.choice(available_moves)


def corner_move(possible_moves):
    """The player plays in a corner square.
    >>> corner_move([3, 5, 6, 7, 9])
    >>> 9
    """
    corner_moves = [1, 3, 7, 9]
    available_moves = [
        index for index in possible_moves if index in corner_moves
    ]
    print(available_moves)
    if available_moves:
        return select_random_move(available_moves)


def edge_move(possible_moves):
    """The player plays in a middle square on any of the 4 sides.
    >>> edges_move([2, 4, 5, 6, 8])
    >>> 4
    """
    edge_moves = [2, 4, 6, 8]
    available_moves = [
        index for index in possible_moves if index in edge_moves
    ]
    print(available_moves)
    if available_moves:
        return select_random_move(available_moves)


def center_move(possible_moves):
    """A player marks the center.
    >>> center_move([2, 5, 8])
    >>> 5
    """
    if 5 in possible_moves:
        return 5


def possible_win_move(board, char):
    """ If the player has two in a row, they can 
    place a third to get three in a row.
    If the opponent has two in a row, the player 
    must play the third themselves to block the opponent.
    """
    move = None
    for row in WINNING_ROW_POSITIONS:
        if char == board[row[0]] == board[row[1]]:
            move = row[2] if board[row[2]] == EMPTY else move
            break
        elif char == board[row[0]] == board[row[2]]:
            move = row[1] if board[row[1]] == EMPTY else move
            break
        elif char == board[row[1]] == board[row[2]]:
            move = row[0] if board[row[0]] == EMPTY else move
            break
    return move


def o_win(board):
    """
    If the player has two in a row, they can 
    place a third to get three in a row.
    """
    return possible_win_move(board, O)


def o_block_x_win(board):
    """
    If the opponent has two in a row, the player 
    must play the third themselves to block the opponent.
    """
    return possible_win_move(board, X)


def move_handler(board):
    """Returns a possible move a player can play.
    If the player has two in a row, they can place 
    a third to get three in a row.

    If the opponent has two in a row, the player must 
    play the third themselves to block the opponent.

    If a corner is among the possible moves. The player 
    plays in a corner square.

    If a middle square along the edges/sides is among the
    possible moves. The player plays in a middle square on 
    any of the 4 sides.

    If the center mark is among the possible moves. A player 
    marks the center.
    """
    if o_win(board):
        return o_win(board)
    elif o_block_x_win(board):
        return o_block_x_win(board)
    else:
        available_moves = [
            index for index, char in enumerate(board) if char == EMPTY and index != 0
        ]

        if corner_move(available_moves):
            return corner_move(available_moves)

        if center_move(available_moves):
            return center_move(available_moves)

        if edge_move(available_moves):
            return edge_move(available_moves)


def can_game_proceed(board_str):
    """
    A board is invalid if any of the board characters are
    not x, o or space.
    A board is invalid if its length is less or greater than
    9 characters.
    A board is in an invalid state if the player has played two
    more times than the opponent player.
    If a player has three marks in a row which is a win, it doesn't
    make sense to proceed playing.
    """
    if not set(board_str).issubset({X, O, EMPTY}):
        return False
    if len(board_str) != NUM_OF_POSITIONS:
        return False
    
    board = create_board(board_str)

    if player_has_a_win(board):
        return False
    
    x_count = board[1:].count(X)
    o_count = board[1:].count(O)

    if (x_count - o_count > 1) or (o_count - x_count > 1):
        return False
    
    return True


def play(board):
    """play a move on the board and return
    a new board
    >>>play(" xxo  o  ")
    >>>"oxxo  o  "
    """
    position = move_handler(board)
    if position:
        board[position] = O
    return "".join(board[1:])


# Drive Code
def main():
    board_input = input("Enter board string: ")
    if can_game_proceed(board_input):
        board = create_board(board_input)
        return play(board)
    return "Invalid board or board state"


if __name__ == "__main__":
    result_board = main()
    print(result_board)
