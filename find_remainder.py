
def remainder(num,d):
    mul = 1
    for i in num:
        mul=mul*i
    return mul%d
num=[100, 10, 5, 25, 35, 14]
d=11
print(remainder(num,d))
