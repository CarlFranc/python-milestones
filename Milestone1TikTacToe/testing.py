
items = [[0,1,2],[3,4,5],[6,7,8]]
list2 = [2,2,2]
to_tuple = tuple(items)

# print(f"index of 3 is {list2.index(3)}")
#
# for elements1 in enumerate(list2):
#     print(elements1)
#
# for index, elements in enumerate(to_tuple):
#     print(type(elements))



# def calculate_average(player_moves):
#
#     return int((sum(player_moves)) / len(player_moves))

# print(calculate_average(list2))
# num = '2'
# print(num.isdigit())
# print(num.isdecimal())

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
    "X_COORDINATES": [0,1,2,1],
    "Y_COORDINATES": [0,1,0,0]
}

# print(check_for_wins(PLAYER_2))

def check_sequential_coordinates(max = 4, num_list = [-1,1,2,3,100,50]):
    print(num_list)
    num_list.sort()
    print(num_list)

    hits = []

    for index, nums in enumerate(num_list):
        uniq = set(hits)
        if len(uniq) == max:
            return True
        if index < len(num_list) - 1:
            if (num_list[index + 1] - nums) == 1:
                hits.append(nums)
                hits.append(num_list[index + 1])
    return False


def hasIdentical(BOARD_SIZE, num_list = [-1,1,2,3,100,50,1,100], max=2):
    print(num_list)
    num_list.sort()
    print(num_list)

    for numbers in range(0, BOARD_SIZE):
        if num_list.count(numbers) == max:
            return True

    return False

def hasSequential(num_list = [1,0,1,2], max = 3):
    num_list.sort()
    hits = []
    for index, nums in enumerate(num_list):
        if len(set(hits)) == max:
            return True
        if index <= len(num_list) - (3 - 1):
            if (num_list[index + 1] - nums) == 1:
                hits.append(nums)
                hits.append(num_list[index + 1])
            else:
                hits.clear()
    return False

def show_statistics():
    print(f'****************{'STATS':^8}****************')
    print(f"{'PLAYER 1':^15}{'vs':^8}{'PLAYER 2':^15}")
    print(f"{'WINS':<12}{PLAYER_1['WINS']:>3}{'-':^8}{'WINS:':<12}{PLAYER_2['WINS']:>3}")
    print(f"{'LOSS':<12}{PLAYER_1['LOSS']:>3}{'-':^8}{'LOSS:':<12}{PLAYER_2['LOSS']:>3}")
    print(f"{'DRAW':<12}{PLAYER_1['DRAW']:>3}{'-':^8}{'DRAW:':<12}{PLAYER_2['DRAW']:>3}")
    print(f"{'ICON':<12}{PLAYER_1['ICON']:>3}{'-':^8}{'ICON:':<12}{PLAYER_2['ICON']:>3}")
    print(f'----------------------------------------')

def tuple_unpacking_test(num_list = [(0,1), (1,1), (2,1)]):
    for x, y in num_list:
        print(f'x is {x} - y is {y}')

    x , y = zip(*num_list)

    print(f'as list: {x} - {y}')

def hasIdentical_alt(num_list = [(0,2), (1,2), (1,0), (2,1),(2,3)]):
    for nums in range(0, 3):
        result_y = [(x, y) for x, y in num_list if y == nums]
        result_x = [(x, y) for x, y in num_list if x == nums]

        if len(result_x) >= 3 or len(result_y) >= 3:
            print(f'Result x: {result_x}')
            print(f'Result y: {result_y}')
            return True

    return False

def hasAntiDiagonal(num_list = [(0,2), (1,2), (1,0), (1,1),(2,0)], max=3):
    winning_coordinates = []
    for x, y in num_list:
        if (x + y) == (max - 1):
            winning_coordinates.append((x, y))
    if len(winning_coordinates) >= max:
        print(f'Winning coords: {winning_coordinates}')
        return True

    return False

def hasDiagonal(num_list = [(2,2), (1,2), (1,1),(0,0)], max=3):
    winning_coordinates = []
    for x, y in num_list:
        if x == y:
            winning_coordinates.append((x, y))
    if len(winning_coordinates) >= max:
        print(f'Winning coords: {winning_coordinates}')
        return True

    return False


# print(check_sequential_coordinates())
# print(hasSequential())
# my_list = [4, 1, 3, 2,6]
# print(3 ** 2)
print(hasDiagonal())


