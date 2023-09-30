
#check the split function in pytonn

log = "joseph is cool"

print(log.split())

#split splits by the space initally
#sort by tye first letter 

words = ["joseph", "cool", "and",  "then"]
words.sort(key=lambda x: (x[0]))

print(words)
