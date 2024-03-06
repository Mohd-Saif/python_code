import re
str =" dbsjdjsdjsn121343nnn1k2n"
# result= "".join(char for char in str if not char.isdigit())
# print(result)

match=re.sub(r"\d+", "",str)
print(match)