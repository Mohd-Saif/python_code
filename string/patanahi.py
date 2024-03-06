from collections import Counter
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
counter_strings=test_str.split()
print(counter_strings)
count_the_words=Counter(counter_strings)
print(count_the_words)

