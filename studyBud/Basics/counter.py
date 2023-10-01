from collections import Counter

s = "joseph"


def count(s):
    # this will create a dictionary with occurence and count of each character
    # here
    print(Counter(s))

count(s)