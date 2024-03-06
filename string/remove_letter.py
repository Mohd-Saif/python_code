# How to Remove Letters From a String in Python

# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks

#  Hear remove 123 in this Charecter:
# import re
# str = 'Geeks123For123Geeks'
# # output_string = re.sub(r'\d+',"", str)
# # print(output_string)
# for i in str:
#     if i.isdigit():

# Input string
input_string = 'Geeks123For123Geeks'

# saif=''.join( char for char in input_string if not char.isdigit())
# print(saif)

saif=''.join(char for char in input_string if not char.isdigit())
print(saif)