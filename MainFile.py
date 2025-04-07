import random

print('Welcome to tictac toe game!')

PLAYER_1 = {
    "LABEL": "Player 1",
    "ICON": "X",
    "WINS": 0,
    "LOSS": 0,
    "DRAW": 0,
    "X_COORDINATES": [],
    "Y_COORDINATES": []
}

PLAYER_2 = {
    "LABEL": "Player 2",
    "ICON": "O",
    "WINS": 0,
    "LOSS": 0,
    "DRAW": 0,
    "X_COORDINATES": [],
    "Y_COORDINATES": []
}

PLAYERS_INFO = (PLAYER_1,PLAYER_2)
last_turn = None

def drawBoard(BOARD_SIZE = 3):
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

def receive_input(BOARD):
    current_player = None
    has_winner = False
    while not has_winner:
        while True:
            current_player = player_turns()
            answer = input(f'{current_player['LABEL']} turn: ')
            if isElementExist(BOARD, answer):
                updatedBoard = updateBoard(BOARD, answer, current_player)
                draw(updatedBoard)
            break

        has_winner = check_for_wins(current_player)
        if has_winner :
            print(f'{current_player['LABEL']} WINS!')

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
    if len(player["X_COORDINATES"]) == 3 and len(player["Y_COORDINATES"]) == 3:
        for acceptable_avg in range(3):
            if int((sum(player["X_COORDINATES"])) / len(player["X_COORDINATES"])) == acceptable_avg or int((sum(player["X_COORDINATES"])) / len(player["X_COORDINATES"])) == acceptable_avg:
                return True
    return False


playing_board = drawBoard()
#playing_board = draw(([0, 1, 2], [3, 4, 5], [6, 7, 8]))
receive_input(playing_board)
