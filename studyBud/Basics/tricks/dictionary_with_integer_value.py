import collections

# this is important so we don't have to check if the key is empty or null
# when we add data


patternedCount = collections.defaultdict(int)

i = 0
while i< 5:
    patternedCount["cool"] += patternedCount["cool"] + 1
    i+=1