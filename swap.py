# Python Program to Swap Two Elements in a List

def swap_two_index(num, pos1, pos2):
    num[pos1], num[pos2] = num[pos2], num[pos1]
    return num


num = [1, 2, 3, 4, 5]
pos1 = 0
pos2 = 4
print(swap_two_index(num, pos1, pos2))
