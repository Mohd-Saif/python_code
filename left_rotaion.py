def left_rotation(num, d):
    n = len(num)
    return num[d % n:] + num[:d % n]


d = 1
num = [1, 2, 3, 4, 5, 5, 6, 7, 8]
print(left_rotation(num, d))
