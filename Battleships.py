import random
empty_board = [
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]
columns = [('1', 0), ('2', 1), ('3', 2), ('4', 3), ('5', 4)]
rows = [('A', 0), ('B', 1), ('C', 2), ('D', 3),('E', 4)]
board_for_placement_player_1 = empty_board
board_for_placement_player_2 = empty_board
#1 3-m, 2 2-m, 3 1-m
big_ship = ['X', 'X', 'X']
medium_ship = ['X', 'X']
small_ship = ['X']
def player_name_input():
    return input('Enter your name: ')
def display_one_board(board):
    print('  1 2 3 4 5')
    count = 0
    for row in board:
        print(f'{rows[count][0]} {row[0]} {row[1]} {row[2]} {row[3]} {row[4]}')
        count += 1
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
def is_possible(ship, user_input, placement, board):
    if placement == 'vertical':
        return user_input[0] + len(ship) <= len(board)
    else:
        return user_input[1] + len(ship) <= len(board[0])
def are_there_ships_already(ship, user_input, placement, board):
    area = []
    if placement == 'horizontal':
        if user_input[0]>0:
            count = 0
            for _ in ship:
                area.append(board[user_input[0]-1][user_input[1]+count])
                count += 1
        count = 0
        for _ in ship:
            area.append(board[user_input[0]][user_input[1]+count])
            count += 1
        if user_input[0]+len(ship)<4:
            count = 0
            for _ in ship:
                area.append(board[user_input[0]+1][user_input[1]+count])
                count += 1
        if user_input[1] != 0:
            area.append(board[user_input[0]][user_input[1]-1])
        if user_input[1] + len(ship) <= 4:
            area.append(board[user_input[0]][user_input[1]+len(ship)])
    elif placement == 'vertical':
        if user_input[1]>0:
            count = 0
            for _ in ship:
                area.append(board[user_input[0]+count][user_input[1]-1])
                count += 1
        count = 0
        for _ in ship:
            area.append(board[user_input[0]+count][user_input[1]])
            count += 1
        if user_input[1]+len(ship)<4:
            count = 0
            for _ in ship:
                area.append(board[user_input[0]+count][user_input[1]+1])
                count += 1
        if user_input[0] != 0:
            area.append(board[user_input[0]-1][user_input[1]])
        if user_input[0] + len(ship) <= 4:
            area.append(board[user_input[0]+len(ship)][user_input[1]])
    if 'X' in area:
        return False
    else:
        return True
def ask_for_coordinates_input():
    coordinators = []
    while True:
        user_input = input('Enter coordinators (A1 - E5): ')
        for tuple in rows:
            if user_input[0] == tuple[0]:
                coordinators.append(tuple[1])
        for tuple in columns:
            if user_input[1] == tuple[0]:
                coordinators.append(tuple[1])
        if len(coordinators)>1:
            return coordinators
        else:
            coordinators = []
            print('Incorrect value - try again.')
def ask_for_placement_input():
    while True:
        user_input = input('Would you like your ship to be placed vertically or horizontally?\n[1] Vertically\n[2] Horizontally\n')
        match user_input:
            case '1':
                return 'vertical'
            case '2':
                return 'horizontal'
            case _:
                print('Incorrect input. Try again')
def placement_ships_of_one_kind(board, ship, number, kind_name):
    for count in range(number):
        print(f'{kind_name} {count+1} of {number}')
        variable_for_while = True
        while variable_for_while:
            display_one_board(board)
            coordinates = ask_for_coordinates_input()
            placement = ask_for_placement_input()
            if is_possible(ship, coordinates, placement, board):
                if are_there_ships_already(ship, coordinates, placement, board):
                    board = placement_ship(ship, coordinates, placement, board)
                    variable_for_while = False
                else:
                    print('Some ships are already there')
            else:
                print('The ship is too large to fit')
def player_placement(board):
    kinds_and_numbers = [(big_ship, 1, 'three-masted ship'), (medium_ship, 2, 'two-masted ship'), (small_ship, 3, 'one-masted ship')]
    for kind in kinds_and_numbers:
        board = placement_ships_of_one_kind(board, kind[0], kind[1], kind[2])
    return board
player_placement(empty_board)




