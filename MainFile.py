import random
from time import sleep

print('Welcome to tictac toe game!')

PLAYER_1 = {
    "LABEL": "Player 1",
    "ICON": "X",
    "WINS": 0,
    "LOSS": 0,
    "DRAW": 0,
    "TURNS": 0,
    "X_COORDINATES": [],
    "Y_COORDINATES": []
}

PLAYER_2 = {
    "LABEL": "Player 2",
    "ICON": "O",
    "WINS": 0,
    "LOSS": 0,
    "DRAW": 0,
    "TURNS": 0,
    "X_COORDINATES": [],
    "Y_COORDINATES": []
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
            player["X_COORDINATES"].append(index)
            player["Y_COORDINATES"].append(col)

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
    if len(player["X_COORDINATES"]) >= FINAL_MINIMUM_COMBINATION and len(player["Y_COORDINATES"]) >= FINAL_MINIMUM_COMBINATION:
        coords_x = player["X_COORDINATES"]
        coords_y = player["Y_COORDINATES"]
        print(f'{player['LABEL']} - X = {coords_x}')
        print(f'{player['LABEL']} - Y = {coords_y}')
        if hasSequential(coords_x) and hasIdentical(coords_y):
            print('cond1')
            return True
        elif hasSequential(coords_y) and hasIdentical(coords_x):
            print('cond2')
            return True
        elif hasSequential(coords_x) and hasSequential(coords_y):
            print('cond3')
            return True

    return False

def hasSequential(num_list, max = FINAL_MINIMUM_COMBINATION):
    # num_list.sort()

    hits = []
    for index, nums in enumerate(num_list):
        if len(set(hits)) == max:
            return True
        if index < len(num_list) - (max - 1):
            if (num_list[index + 1] - nums) == 1:
                hits.append(nums)
                hits.append(num_list[index + 1])
            else:
                hits.clear()
    return False

def hasIdentical(num_list, BOARD_SIZE = FINAL_BOARD_SIZE, max = FINAL_MINIMUM_COMBINATION):

    for numbers in range(0, BOARD_SIZE):
        if num_list.count(numbers) == max:
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
    PLAYER_1['X_COORDINATES'].clear()
    PLAYER_1['Y_COORDINATES'].clear()
    PLAYER_1['TURNS'] = 0
    PLAYER_2['X_COORDINATES'].clear()
    PLAYER_2['Y_COORDINATES'].clear()
    PLAYER_2['TURNS'] = 0


playing_board = drawBoard()
#playing_board = draw(([0, 1, 2], [3, 4, 5], [6, 7, 8]))
receive_input(playing_board)

#TODO: FIX DIAGONAL WIN