# Python | Ways to remove a key from dictionary
"""
This Python code snippet creates a dictionary called `data` with key-value pairs representing names
and ages. It then uses the `del` keyword to remove the key `'Mani'` from the dictionary. Finally, it
prints the updated dictionary without the key `'Mani'`."""

data={'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21, 'saif': 21}
# del data['Mani']
# using popitems

data.popitem()

print(data)
