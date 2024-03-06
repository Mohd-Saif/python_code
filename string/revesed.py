# Reverse Words in a Given String in Python
# str =" geeks quiz practice code"
# l=[]
# reverseds=str.split()
# print(reverseds)
# for i in reverseds[::-1]:
#     l.append(i)
# print(" ".join(l))


def reveseds(n):
    l=[]
    data=n.split()
    for i in data[::-1]:
        l.append(i)
    return " ".join(l)
n =" geeks quiz practice code"
print(reveseds(n))
