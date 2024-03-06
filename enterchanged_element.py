Input: [12, 35, 9, 56, 24]


# Output : [24, 35, 9, 56, 12]

def swap(num):
    num[0], num[-1] = num[-1], num[0]
    return num

num = [12, 35, 9, 56, 24]

print(swap(num))
