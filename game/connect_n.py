from connect_n_lib import *


# Perform a play
def player_turn(player_num, current_board, win_count):
    print_board(current_board)
    sel = input("\nPlayer {0} Turn, please make a selection (0-{1}) ".format(player_num, col_count - 1))

    # Validate the input as an integer
    sel = input_validation(sel)
    while sel == -1 or not col_range_validation(sel, len(current_board[0])) or not play_validation(current_board, sel):
        print("\nSorry, your play is not valid, please select column with a free row in it.")
        print_board(current_board)
        sel = input("\nPlayer {0} Turn, please make a selection (0-{1}) ".format(player_num, col_count - 1))
        sel = input_validation(sel)
    # Check available row
    open_row = check_open_row(current_board, sel)

    # Perform the play on the chosen column
    new_board = drop_piece(board, open_row, sel, player_num)
    return new_board, open_row, sel


# Start game code


# CONSTANTS

row_count = 6
col_count = 7
win_count = 4

game_over = False
board = create_board(row_count, col_count)
turn_count = 0
player_sel = 0

while not game_over:
    # Player 1 turn
    if player_sel == 0:
        player_number = 1
        board, piece_row, piece_col = player_turn(player_number, board, win_count)
        # Checks if play is winner play
        game_over = check_winner(board, player_number, win_count, piece_row, piece_col)

    # Player 2 turn
    else:
        player_number = 2
        board, piece_row, piece_col = player_turn(player_number, board, win_count)
        # Checks if play is winner play
        game_over = check_winner(board, player_number, win_count, piece_row, piece_col)

    turn_count += 1
    player_sel = turn_count % 2
