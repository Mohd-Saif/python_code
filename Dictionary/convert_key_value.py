# Python – Convert key-values list to flat dictionary

# Python3 code to demonstrate working of 
# Convert key-values list to flat dictionary
# Using dict() + zip()
from itertools import product
# initializing dictionary
test_dict = {'month' : [1, 2, 3],
			'name' : ['Jan', 'Feb', 'March']}

test=dict(zip(test_dict["month"], test_dict["name"]))
print(type(test))
