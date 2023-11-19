import os

def load_game_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("          COLUMN")
    print("         1   2   3")
    print("       -------------")
    for i in range(0, 9, 3):
        row_number = i // 3 + 1
        print(f"ROW {row_number}  | {gameboard[i]} | {gameboard[i + 1]} | {gameboard[i + 2]} |")
        print("       -------------")
    print()

def update_game_board(row, col, symbol):
    index = (row - 1) * 3 + (col - 1)
    gameboard[index] = symbol
    load_game_board()

def check_gameboard():
    return '_' in gameboard or 'X' in gameboard or 'O' in gameboard

def check_winner(symbol):
    for i in range(0, 9, 3):
        if gameboard[i] == gameboard[i + 1] == gameboard[i + 2] == symbol:
            return True
    for i in range(3):
        if gameboard[i] == gameboard[i + 3] == gameboard[i + 6] == symbol:
            return True
    if gameboard[0] == gameboard[4] == gameboard[8] == symbol or \
       gameboard[2] == gameboard[4] == gameboard[6] == symbol:
        return True
    return False

def check_draw():
    return '_' not in gameboard

def clear_screen_and_display_board(player_name, symbol):
    os.system('cls' if os.name == 'nt' else 'clear')
    load_game_board()
    print(f"{player_name}'s turn ({symbol})")


def main():
    global gameboard
    gameboard = ['_', '_', '_',
                 '_', '_', '_',
                 '_', '_', '_']

    player_1_name = input("Enter Player 1's name: ")
    player_2_name = input("Enter Player 2's name: ")

    current_player = 1  # 1 for player 1, 2 for player 2

    while True:
        clear_screen_and_display_board(player_1_name if current_player == 1 else player_2_name, 'X' if current_player == 1 else 'O')

        player_row = int(input('Enter Row Number 1, 2, or 3: '))
        player_col = int(input('Enter Column Number 1, 2, or 3: '))

        if gameboard[(player_row - 1) * 3 + (player_col - 1)] == '_':
            update_game_board(player_row, player_col, 'X' if current_player == 1 else 'O')
        else:
            print('Sorry, that spot is already taken. Try again.')
            continue

        if check_winner('X' if current_player == 1 else 'O'):
            print(f"{player_1_name if current_player == 1 else player_2_name} wins!")
            break

        if check_draw():
            print("It's a draw!")
            break

        current_player = 3 - current_player  # Switch players (1 <-> 2)

if __name__ == "__main__":
    main()


