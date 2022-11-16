import random
def empty_board():
    empty_board = [
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    return empty_board
columns = [('1', 0), ('2', 1), ('3', 2), ('4', 3), ('5', 4)]
rows = [('A', 0), ('B', 1), ('C', 2), ('D', 3),('E', 4)]
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
        if len(user_input) == 2:
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
    new_board = board
    for count in range(number):
        print(f'{kind_name} {count+1} of {number}')
        input()
        variable_for_while = True
        while variable_for_while:
            display_one_board(new_board)
            coordinates = ask_for_coordinates_input()
            if len(ship) > 1:
                placement = ask_for_placement_input()
            else:
                placement = 'vertical'
            if is_possible(ship, coordinates, placement, new_board):
                if are_there_ships_already(ship, coordinates, placement, new_board):
                    new_board = placement_ship(ship, coordinates, placement, new_board)
                    variable_for_while = False
                else:
                    print('Some ships are already there')
            else:
                print('The ship is too large to fit')
    return new_board
def player_placement(board, name):
    print(f'{name}, your turn to place ships on a board.')
    input()
    kinds_and_numbers = [(big_ship, 1, 'three-masted ship'), (medium_ship, 2, 'two-masted ship'), (small_ship, 3, 'one-masted ship')]
    for kind in kinds_and_numbers:
        board = placement_ships_of_one_kind(board, kind[0], kind[1], kind[2])
    return board
def display_two_boards(board_1, board_2):
    print('Your ships  | Enemy ships')
    print('  1 2 3 4 5 |   1 2 3 4 5')
    count = 0
    for row in board_1:
        print(f'{rows[count][0]} {row[0]} {row[1]} {row[2]} {row[3]} {row[4]} | {rows[count][0]} {board_2[board_1.index(row)][0]} {board_2[board_1.index(row)][1]} {board_2[board_1.index(row)][2]} {board_2[board_1.index(row)][3]} {board_2[board_1.index(row)][4]}')
        count += 1
def move_is_succesfull(placement_board, user_input):
    if placement_board[user_input[0]][user_input[1]] == 'X':
        return True
    else:
        return False
def hit_or_miss(placement_board, displayed_board, user_input):
    if move_is_succesfull(placement_board, user_input):
        if placement_board[user_input[0]][user_input[1]] == 'X':
            if_sunk_list = []
            if user_input[0]-1 >= 0:
                if_sunk_list.append(placement_board[user_input[0]-1][user_input[1]])
            if user_input[0]+1 < len(placement_board):
                if_sunk_list.append(placement_board[user_input[0]+1][user_input[1]])
            if user_input[1]-1 >= 0:
                if_sunk_list.append(placement_board[user_input[0]][user_input[1]-1])
            if user_input[1]+1 < len(placement_board):
                if_sunk_list.append(placement_board[user_input[0]][user_input[1]+1])            
            if 'X' not in if_sunk_list:
                displayed_board[user_input[0]][user_input[1]] = 'S'
                if user_input[0]-1 >= 0:
                    if placement_board[user_input[0]-1][user_input[1]] == 'H':
                        displayed_board[user_input[0]-1][user_input[1]] = 'S'
                        if user_input[0]-2 >= 0:
                            displayed_board[user_input[0]-2][user_input[1]] = 'S'
                if user_input[0]+1 < len(placement_board):
                    if placement_board[user_input[0]+1][user_input[1]] == 'H':
                        displayed_board[user_input[0]+1][user_input[1]] = 'S'
                        if user_input[0]+2 < len(placement_board):
                            displayed_board[user_input[0]+2][user_input[1]] = 'S'
                if user_input[1]-1 >= 0:
                    if placement_board[user_input[0]][user_input[1]-1] == 'H':
                        displayed_board[user_input[0]][user_input[1]-1] = 'S'
                        if user_input[1]-2 >= 0:
                            displayed_board[user_input[0]][user_input[1]-2] = 'S'
                if user_input[1]+1 < len(placement_board):
                    if placement_board[user_input[0]][user_input[1]+1] == 'H':
                        displayed_board[user_input[0]][user_input[1]+1] = 'S'
                        if user_input[1]+2 < len(placement_board):
                            displayed_board[user_input[0]][user_input[1]+2] = 'S'
                print('Hit and sunk!')
            else:
                displayed_board[user_input[0]][user_input[1]] = 'H'
                print('Hit')
    else:
        displayed_board[user_input[0]][user_input[1]] = 'M'
        print('Missed')
    return displayed_board
def change_placement_board(placement_board, user_input):
    if move_is_succesfull(placement_board, user_input):
        placement_board[user_input[0]][user_input[1]] = 'H'
    return placement_board
def ask_for_coordinates_in_game_input(displayed_board):
    while True:
        user_input = ask_for_coordinates_input()
        if was_not_already_used(user_input, displayed_board):
            return user_input
        else:
            print('Coordinators already used. Try again')
def was_not_already_used(user_input, displayed_board):
    if displayed_board[user_input[0]][user_input[1]] == '0':
        return True
    else:
        return False
def turn(displayed_board_1, displayed_board_2, placement_board):
    display_two_boards(displayed_board_1, displayed_board_2)
    while True:
        coordinators = ask_for_coordinates_in_game_input(displayed_board_2)
        if was_not_already_used(coordinators, displayed_board_2):
            displayed_board_2 = hit_or_miss(placement_board, displayed_board_2, coordinators)
            placement_board = change_placement_board(placement_board, coordinators)
            break
def check_win(placement_boards):
    rows_without_x_1 = 0
    rows_without_x_2 = 0
    for any_row in placement_boards[0]:
        if 'X' not in any_row:
            rows_without_x_1 += 1
    for any_row in placement_boards[1]:
       if 'X' not in any_row:
            rows_without_x_2 += 1
    if rows_without_x_1 == 5:
        return 1
    elif rows_without_x_2 == 5:
        return 0
    else:
        return None 
def game(placement_boards, display_boards, names):
    player = 0
    winning_player = None
    while winning_player == None:
        if player == 0:
            print(f'{names[0]}\'s turn')
            input()
            turn(display_boards[0], display_boards[1], placement_boards[1])
            player = 1
        else:
            print(f'{names[1]}\'s turn')
            input()
            turn(display_boards[1], display_boards[0], placement_boards[0])
            player = 0
        winning_player = check_win(placement_boards)
    print(f'{names[winning_player]} wins the game!')
def settings():
    placement_boards = []
    display_boards = []
    names = []
    for number in range(2):
        print(f'Player {number} of 2')
        input()
        name = player_name_input()
        names.append(name)
        display_board = empty_board()
        display_boards.append(display_board)
        board = empty_board()
        board = player_placement(board, name)
        placement_boards.append(board)
    setting_list = [placement_boards, display_boards, names]
    return setting_list
def menu(game_settings):
    while True:
        menu_input = input('[1] Play\n[2] Change settings\n[3] Quit\n')
        match menu_input:
            case '1':
                game(game_settings[0], game_settings[1], game_settings[2])
            case '2':
                game_settings = settings()
            case '3':
                break
            case _:
                print('Incorrect input')

game_settings = settings()
menu(game_settings)





