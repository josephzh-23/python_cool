
#this will sort by the 2nd word first before sorting by the first word here


# sort by the first one and then by the 2nd one here
words = [ "joseph is not cool", "joseph is super cool", "joseph is cool"]
words.sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))

print(words)


#W
words = ["qizheng is not cool", "joseph is super cool", "joseph is cool"]
words.sort(key=lambda x: (x.split(' ', 1)[0], x.split(' ', 1)[1]))

print(words)









