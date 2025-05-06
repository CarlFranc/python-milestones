import random
from time import sleep

print('Welcome to tictac toe game!')

PLAYER_1 = {
    "LABEL": "Player 1",
    "ICON": '\u2716',
    "WINS": 0,
    "LOSS": 0,
    "DRAW": 0,
    "TURNS": 0,
    "COORDS":[]
}

PLAYER_2 = {
    "LABEL": "Player 2",
    "ICON": '\u25EF',
    "WINS": 0,
    "LOSS": 0,
    "DRAW": 0,
    "TURNS": 0,
    "COORDS":[]
}

PLAYERS_INFO = (PLAYER_1,PLAYER_2)
last_turn = None
FINAL_BOARD_SIZE = 3
FINAL_MINIMUM_COMBINATION = 3
FINAL_QUIT = 'quit'
FINAL_RESTART = 'restart'
FINAL_STATS = 'stats'
FINAL_SLEEP_TIME = 2

def drawBoard(BOARD_SIZE = FINAL_BOARD_SIZE):
    counter = 0
    column = 0
    board = []
    items = []

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            print(f'|{counter + column + row:^10}', end='')
            items.append(counter + column + row)
        board.append(items.copy())
        counter += column
        items.clear()
        print('\n')

    return tuple(board)

def draw(board):
    for x,y,z in board:
        print(f'|{x:^10}',f'{y:^10}',f'{z:^10}',sep='|', end='\n\n')

    return board

def isElementExist(board, item):
    if not item.isdigit():
        return False

    for rows in board:
        if int(item) in rows:
            return True

def receive_input(playing_board):
    BOARD = playing_board
    current_player = None
    has_winner = False
    while not has_winner:
        while True:
            current_player = player_turns()
            display_menu()
            answer = input(f'{current_player['LABEL']} turn: ')
            if answer == FINAL_QUIT:
                print('Bye..')
                exit(0)
            elif answer == FINAL_RESTART:
                print('Restarting...')
                receive_input(drawBoard())
            elif answer == FINAL_STATS:
                show_statistics()
                player_turns()
                sleep(FINAL_SLEEP_TIME)
            elif isElementExist(BOARD, answer):
                current_player['TURNS'] += 1
                updatedBoard = updateBoard(BOARD, answer, current_player)
                draw(updatedBoard)
            else:
                print('Invalid move!')
                player_turns()
            break

        has_draw = check_draw()
        has_winner = check_for_wins(current_player)
        opponent = PLAYERS_INFO[(1 - PLAYERS_INFO.index(current_player))]
        if has_winner :
            print(f'{current_player['LABEL']} WINS!')
            sleep(FINAL_SLEEP_TIME)
            current_player['WINS'] += 1
            opponent['LOSS'] += 1
            clear_moves()
            show_statistics()
            receive_input(drawBoard())
        elif has_draw:
            print(f'DRAW!!')
            sleep(FINAL_SLEEP_TIME)
            current_player['DRAW'] += 1
            opponent['DRAW'] += 1
            clear_moves()
            show_statistics()
            receive_input(drawBoard())

def updateBoard(BOARD, element, player):
    element_search = int(element)
    for index, rows in enumerate(BOARD):
        if element_search in rows:
            col = rows.index(element_search)
            BOARD[index][col] = player['ICON']
            player["COORDS"].append((index, col))

    return BOARD

def player_turns():
    global last_turn

    if last_turn is None:
        turn = random.randrange(0, 2)
        last_turn = turn
    else:
        last_turn = 1 - last_turn

    return PLAYERS_INFO[last_turn]

def check_for_wins(player):
    if len(player["COORDS"]) >= FINAL_MINIMUM_COMBINATION:
        if hasIdentical(player["COORDS"]):
            return True
        elif hasDiagonal(player["COORDS"]):
            return True
        elif hasAntiDiagonal(player["COORDS"]):
            return True

    return False

def hasIdentical(num_list, max = FINAL_MINIMUM_COMBINATION):

    for nums in range(0, max):
        result_y = [(x, y) for x, y in num_list if y == nums]
        result_x = [(x, y) for x, y in num_list if x == nums]

        if len(result_x) >= max or len(result_y) >= max:
            return True

    return False

def hasAntiDiagonal(num_list, max = FINAL_MINIMUM_COMBINATION):
    winning_coordinates = []
    for x , y in num_list:
        if (x + y) == (max - 1):
            winning_coordinates.append((x, y))
    if len(winning_coordinates) >= max:
        return True

    return False

def hasDiagonal(num_list, max = FINAL_MINIMUM_COMBINATION):
    winning_coordinates = []
    for x, y in num_list:
        if x == y:
            winning_coordinates.append((x, y))
    if len(winning_coordinates) >= max:
        return True

    return False

def display_menu():
    print(f'****************{'MENU':^8}****************')
    print(f'{FINAL_QUIT:<10} - Exit the game')
    print(f'{FINAL_RESTART:<10} - Restart the game')
    print(f'{FINAL_STATS:<10} - Show statistics')
    print(f'----------------------------------------')

def show_statistics():
    print(f'****************{'STATS':^8}****************')
    print(f"{'PLAYER 1':^15}{'-':^8}{'PLAYER 2':^15}")
    print(f"{'WINS':<12}{PLAYER_1['WINS']:>3}{'-':^8}{'WINS:':<12}{PLAYER_2['WINS']:>3}")
    print(f"{'LOSS':<12}{PLAYER_1['LOSS']:>3}{'-':^8}{'LOSS:':<12}{PLAYER_2['LOSS']:>3}")
    print(f"{'DRAW':<12}{PLAYER_1['DRAW']:>3}{'-':^8}{'DRAW:':<12}{PLAYER_2['DRAW']:>3}")
    print(f"{'ICON':<12}{PLAYER_1['ICON']:>3}{'-':^8}{'ICON:':<12}{PLAYER_2['ICON']:>3}")
    print(f'----------------------------------------')

def check_draw():
    if (PLAYER_1['TURNS'] + PLAYER_2['TURNS']) == (FINAL_BOARD_SIZE ** 2):
        return True

    return False

def clear_moves():
    PLAYER_1['TURNS'] = 0
    PLAYER_1['COORDS'].clear()
    PLAYER_2['TURNS'] = 0
    PLAYER_2['COORDS'].clear()

def check_diagonal_win(player):
    for coordinates in player['COORDS']:
        pass


playing_board = drawBoard()
#playing_board = draw(([0, 1, 2], [3, 4, 5], [6, 7, 8]))
receive_input(playing_board)