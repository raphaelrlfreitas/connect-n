import numpy as np


# FUNCTIONS LIBRARY

# Function to create a board for n rows and columns
def create_board(rows, columns):
    new_board = np.zeros((rows, columns), np.int8)
    return new_board


# Print current board
def print_board(board):
    print(np.flipud(board))


# Player input validation
def input_validation(player_input) -> int:
    try:
        return int(player_input)
    except ValueError:
        return -1

def col_range_validation(sel, num_cols):
    return 0 <= sel < num_cols


# Checks if the play chosen is valid
def play_validation(current_board, col):
    if current_board[-1, col] == 0:
        return True
    else:
        return False


# Check in which row
def check_open_row(current_board, col):
    return int(np.argwhere(current_board[:, col] == 0)[0])


# Drop the piece on the specified column
def drop_piece(current_board, row, col, player_num):
    current_board[row][col] = player_num
    return current_board


# Checks if there is a winner in the game
def check_winner(current_board, player_num, win_count, row, col):
    # Check for horizontal win condition
    connect_count = 0
    for i_h in range(-win_count + 1, win_count, 1):
        if 0 <= col + i_h < len(current_board[0]):
            if current_board[row][col + i_h] == player_num:
                connect_count += 1
            else:
                connect_count = 0
            if connect_count == win_count:
                print_board(current_board)
                print("\nCONGRATULATIONS! Player {0} is the WINNER!".format(player_num))
                return True

    # Check for vertical win condition
    connect_count = 0
    for i_v in range(-win_count + 1, win_count, 1):
        if 0 <= row + i_v < len(current_board):
            if current_board[row + i_v][col] == player_num:
                connect_count += 1
            else:
                connect_count = 0
            if connect_count == win_count:
                print_board(current_board)
                print("\nCONGRATULATIONS! Player {0} is the WINNER!".format(player_num))
                return True

    # Check for positive slope win condition
    connect_count = 0
    for i_ps in range(-win_count + 1, win_count, 1):
        if 0 <= row + i_ps < len(current_board) and 0 <= col + i_ps < len(current_board[0]):
            if current_board[row + i_ps][col + i_ps] == player_num:
                connect_count += 1
            else:
                connect_count = 0
            if connect_count == win_count:
                print_board(current_board)
                print("\nCONGRATULATIONS! Player {0} is the WINNER!".format(player_num))
                return True

    # Check for negative slope win condition
    connect_count = 0
    for i_ns in range(-win_count + 1, win_count, 1):
        if 0 <= row - i_ns < len(current_board) and 0 <= col + i_ns < len(current_board[0]):
            if current_board[row - i_ns][col + i_ns] == player_num:
                connect_count += 1
            else:
                connect_count = 0
            if connect_count == win_count:
                print_board(current_board)
                print("\nCONGRATULATIONS! Player {0} is the WINNER!".format(player_num))
                return True

    return False