# # Vertical Concatenation in Matrix

# # Input =[[“Gfg”, “good”], [“is”, “for”]] 
# # Output : [‘Gfgis’, ‘goodfor’] 
# from itertools import zip_longest
# # from itertools import zip_longest
# test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]
# # saif=zip_longest(test_list)
# # for i in saif:
# test_str=str(test_list)
# test=["".join(els) for els in zip_longest(*test_str,fillvalue ="")]
# print("List after column Concatenation : " + str(test))


# Python3 code to demonstrate working of 
# Vertical Concatenation in Matrix
# Using join() + list comprehension + zip_longest()
from itertools import zip_longest

# initializing lists
test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]
test_str=str(test_list)
res=["".join(i) for i in zip_longest(*test_list,fillvalue='')]
print(res)
