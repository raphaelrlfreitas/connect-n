import pytest
from game.connect_n_lib import *

## CONTANTS
NUM_ROWS = 6
NUM_COLS = 7
WIN_COUNT = 4
PLAYER_ONE = 1
PLAYER_TWO = 2



@pytest.fixture
def empty_board():
    empty_board = create_board(NUM_ROWS, NUM_COLS)
    return empty_board

@pytest.fixture
def horizontal_check_board():
    board = create_board(NUM_ROWS, NUM_COLS)
    board[NUM_ROWS - 1, 1:5] = PLAYER_ONE
    board[NUM_ROWS - 2, 1:4] = PLAYER_TWO
    return board


@pytest.fixture
def vertical_check_board():
    board = create_board(NUM_ROWS, NUM_COLS)
    board[0:4, 1] = PLAYER_ONE
    board[0:4, 2] = PLAYER_TWO
    return board


@pytest.fixture
def positive_slope_check_board():
    board = create_board(NUM_ROWS, NUM_COLS)
    board[0, 0] = PLAYER_ONE
    board[1, 1] = PLAYER_ONE
    board[2, 2] = PLAYER_ONE
    board[3, 3] = PLAYER_ONE
    board[0, 1:4] = PLAYER_TWO
    return board


def test_create_board():
    new_board = np.zeros((NUM_ROWS, NUM_COLS), np.int8)
    assert create_board(NUM_ROWS, NUM_COLS).all() == new_board.all()

def test_input_validation_str():
    assert input_validation("asd") == -1
    assert input_validation("") == -1



def test_col_range_validation():
    assert col_range_validation(NUM_COLS, NUM_COLS-1) == False
    assert col_range_validation(NUM_COLS+2, NUM_COLS-1) == False
    assert col_range_validation(-2, NUM_COLS-1) == False


def test_check_winner_horizontal_player_one_win(horizontal_check_board):
    assert check_winner(horizontal_check_board, PLAYER_ONE, WIN_COUNT, NUM_ROWS-1, 4) == True


def test_check_winner_vertical_player_one_win(vertical_check_board):
    assert check_winner(vertical_check_board, PLAYER_ONE, WIN_COUNT, 2, 1) == True
