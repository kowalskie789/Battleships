empty_board = [
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]
board_for_placement_player_1 = empty_board
board_for_placement_player_2 = empty_board
#1 3-m, 2 2-m, 3 1-m
big_ship = ['X', 'X', 'X']
medium_ship = ['X', 'X']
small_ship = ['X']
def placement_ships_of_one_kind(ship, user_inputs, placements, board):
    count = 0
    for placement in placements:
        board = placement_ship(ship, user_inputs[count], placement, board)
        count += 1
    return board
def placement_ship(ship, user_input, placement, board):
    distance = 0
    if placement == 'vertical':
        for _ in ship:    
            board[user_input[0]+distance][user_input[1]] = 'X'
            distance += 1
    else:
        for _ in ship:
            board[user_input[0]][user_input[1]+distance] = 'X'
            distance += 1
    return board
player_board = empty_board
print(player_board)
inputs = [[0, 0], [1, 0]]
placements = ['horizontal', 'horizontal']
player_board = placement_ships_of_one_kind(medium_ship, inputs, placements, player_board)
print(player_board)


