
def palindrom(n):
    return n[::-1] == n

n="malayalam"
test=palindrom(n)

if test:
    print("yes")
else:
    print("No")