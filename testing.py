
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



def calculate_average(player_moves):

    return int((sum(player_moves)) / len(player_moves))

print(calculate_average(list2))
# num = '2'
# print(num.isdigit())
# print(num.isdecimal())