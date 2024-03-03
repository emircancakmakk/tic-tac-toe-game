# Simple Tic-Tac-Toe Game
game_on = True

def display_board(input_list):
    print(f'{input_list[6]} | {input_list[7]} | {input_list[8]}')
    print(f'{input_list[3]} | {input_list[4]} | {input_list[5]}')
    print(f'{input_list[0]} | {input_list[1]} | {input_list[2]}')

def position_check(position, available_positions, player_turn):
    while True:
        if position not in available_positions:
            p_input = int(input(f'(To player {player_turn + 1}) Position {position} is not correct or available, please type it again: '))

            position = p_input
        else:
            p_input = position
            
            break
    
    return p_input

def game_finished(position_list, available_positions, player_turn):
    if len(available_positions) == 0:
        print('The game ended in a draw!')

        return True
    else:
        w_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for p1, p2, p3 in w_combinations:
            if((position_list[p1] == position_list[p2] == position_list[p3]) and (position_list[p1] != ' ' and position_list[p2] != ' ' and position_list[p3] != ' ')):
                print(f'(To player {player_turn + 1}) Congratulations, you won the game!')
                return True

        return False

def is_game_on():
    g_input = input('Do you want to play again, type "Y" or "N": ')

    if g_input == 'Y':
        return True
    else:
        return False

def game():
    players = [1 , 2]
    symbols = ['O', 'X']
    available_positions = [x for x in range(1, 10)]
    position_list = [' '] * 9

    print('Welcome to the Tic-Tac-Toe Game!')
    print('You can think of the input positions as the numpad on the right side of your keyboard.')
    print(f'Player {players[0]} will start!')
    
    p = 0
    s = 0

    while True:
        display_board(position_list)
        player_turn = players[p]

        p_input = int(input(f'(To player {player_turn}) Which position do you want put {symbols[s]}?: '))

        p_input = position_check(p_input, available_positions, p)

        position_list[p_input - 1] = symbols[s]
        available_positions.remove(p_input)
        g_input = game_finished(position_list, available_positions, player_turn)

        if g_input == True:
            break
        else:
            if p == 0:
                p = 1
                s = 1
            else:
                p = 0
                s = 0

        
if __name__ == '__main__':
    while game_on:
        game()
        game_on = is_game_on()
