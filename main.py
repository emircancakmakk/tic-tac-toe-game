# Simple Tic-Tac-Toe Game

game_on = True
position_list = [' '] * 9

def display_board(input_list):
    print(f'{input_list[8]} | {input_list[7]} | {input_list[6]}')
    print(f'{input_list[5]} | {input_list[4]} | {input_list[3]}')
    print(f'{input_list[2]} | {input_list[1]} | {input_list[0]}')

def position_check(position, available_positions):
    if position not in available_positions:
        return False
    else:
        return True
    

def game():
    players = [1 , 2]
    symbols = ['O', 'X']
    available_positions = [x for x in range(0, 9)]

    print(f'Player {players[0]} will start!')
    
    p = 0
    s = 0

    while True:
        display_board(position_list)
        player_turn = players[p]

        while True: # fonksiyon içinde yapılması çok daha doğru olacaktır
            p_input = int(input(f'(To player {player_turn}) Which position do you want put {symbols[s]}?: '))

            p_check = position_check(p_input, available_positions)

            if p_check:
                position_list[p_input] = symbols[s] 
                available_positions.remove(p_input)

                if p == 0:
                    p = 1
                    s = 1
                else: 
                    p = 0
                    s = 0
                
                break
            else:
                print(f'(To player {player_turn}) You cannot put something to position {p_input}.')
                print(f'(To player {player_turn}) Available positions are: {available_positions}.')

        # check game is finished or not! (bütün karelerin dolması ihtimali veya birinin kazanmış olma ihtimali)

def is_game_on():
    input = input('Do you want to play again, type "Y" or "N": ')

    if input == 'Y':
        return True
    else:
        return False

if __name__ == '__main__':
    while game_on:
        game()
        game_on = is_game_on()
