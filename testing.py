
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


# print(check_sequential_coordinates())
print(hasIdentical(3))
# my_list = [4, 1, 3, 2,6]


