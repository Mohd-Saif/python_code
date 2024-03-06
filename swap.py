# Python Program to Swap Two Elements in a List

def swap_two_index(num, pos1, pos2):
    """
    The function `swap_two_index` swaps the elements at two specified positions in a list.
    
    :param num: [1, 2, 3, 4, 5]
    :param pos1: pos1 is the index of the first element you want to swap. In this case, pos1 is 0, which
    means you want to swap the element at index 0 in the list
    :param pos2: pos2 is the index of the second element that you want to swap with the element at index
    pos1 in the list num. In this case, pos2 is 4, which means you want to swap the element at index 0
    with the element at index 4 in the list [1
    :return: The function `swap_two_index` is returning the list `num` after swapping the elements at
    positions `pos1` and `pos2`. In this case, the elements at positions 0 and 4 are being swapped in
    the list `[1, 2, 3, 4, 5]`, so the output will be `[5, 2, 3, 4
    """
    num[pos1], num[pos2] = num[pos2], num[pos1]
    return num


num = [1, 2, 3, 4, 5]
pos1 = 0
pos2 = 4
print(swap_two_index(num, pos1, pos2))
