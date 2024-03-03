import os

game_on = True

# ANSI escape codes for text colors
GREEN = '\033[92m'  # Green color
YELLOW = '\033[93m'  # Yellow color
RED = '\033[91m'     # Red color
RESET = '\033[0m'    # Reset to default color

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the Tic-Tac-Toe board with colorful output
def display_board(input_list):
    print("   |   |   ")
    print(f" {colorize(input_list[6])} | {colorize(input_list[7])} | {colorize(input_list[8])} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {colorize(input_list[3])} | {colorize(input_list[4])} | {colorize(input_list[5])} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {colorize(input_list[0])} | {colorize(input_list[1])} | {colorize(input_list[2])} ")
    print("   |   |   ")

# Function to add color to symbols (X, O)
def colorize(symbol):
    if symbol == 'X':
        return GREEN + symbol + RESET  # Green color for X
    elif symbol == 'O':
        return YELLOW + symbol + RESET  # Yellow color for O
    else:
        return symbol

def position_check(position, available_positions, player_turn):
    """Checks if the input position is valid and available."""
    while True:
        if position not in available_positions or not isinstance(position, int) or position < 1 or position > 9:
            # If position is not valid or not available, prompt the player to input again.
            p_input = int(input(f'(Player {player_turn + 1}) Invalid or already taken position. Please choose an available position (1-9): '))
            position = p_input
        else:
            p_input = position
            break
    return p_input

def game_finished(position_list, available_positions, player_turn):
    """Checks if the game is finished (win/draw)."""
    if len(available_positions) == 0:
        # If no more available positions, the game ends in a draw.
        print('The game ended in a draw!')
        return True
    else:
        # List of winning combinations
        w_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for p1, p2, p3 in w_combinations:
            if((position_list[p1] == position_list[p2] == position_list[p3]) and (position_list[p1] != ' ' and position_list[p2] != ' ' and position_list[p3] != ' ')):
                # If any winning combination is found, the respective player wins.
                print(f'Congratulations, Player {player_turn + 1}! You won the game!')
                return True
        return False

def is_game_on():
    """Asks the user if they want to play again."""
    g_input = input('Do you want to play again? Type "Y" to continue or any other key to quit: ')
    return g_input.lower() == 'y'

def game():
    """Main function to run the Tic-Tac-Toe game."""
    clear_screen()  # Clear the screen before starting the game
    players = [1 , 2]
    symbols = ['O', 'X']
    available_positions = [x for x in range(1, 10)]
    position_list = [' '] * 9

    print('Welcome to Tic-Tac-Toe!')
    print('You can think of the input positions as the numpad on the right side of your keyboard.')

    # Loop to alternate players' turns until the game is finished.
    while True:
        clear_screen() # Clear the screen before each turn
        display_board(position_list)
        player_turn = players[0] if len(available_positions) % 2 == 1 else players[1]

        # Prompt the current player to choose a position.
        p_input = int(input(f'(Player {player_turn}) Choose a position to place your symbol ({symbols[player_turn-1]}): '))
        p_input = position_check(p_input, available_positions, player_turn - 1)

        position_list[p_input - 1] = symbols[player_turn - 1]
        available_positions.remove(p_input)

        # Check if the game is finished
        if game_finished(position_list, available_positions, player_turn - 1):
            display_board(position_list)
            break

if __name__ == '__main__':
    while game_on:
        game()
        game_on = is_game_on()
