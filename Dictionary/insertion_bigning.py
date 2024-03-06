

# # original_dict = {'a': 1, 'b': 2}
# # item_to_insert = ('c', 3)
# # new_dict={item_to_insert[0]:item_to_insert[1]}
# # print(new_dict)
# # new_dict.update(original_dict)
# # print(new_dict)\

# # Python code to demonstrate
# # insertion of items in beginning of ordered dict
# from  collections import OrderedDict
# # original_dict = {'a': 1, 'b': 2}
# # item_to_insert = ('c', 3)
# data= OrderedDict(list('c', 3) + OrderedDict(list('a': 1, 'b': 2)))))))


# print(data)


# Python code to demonstrate a dictionary
# with multiple inputs in a key.
import random as rn

# creating an empty dictionary
dict = {}

# Insert first triplet in dictionary
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z;

# Insert second triplet in dictionary
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z;

# print the dictionary
print(dict)

