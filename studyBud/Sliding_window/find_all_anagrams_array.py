
alphabetSize = 26

s = 'cbaebabacd'
p = 'abc'

# find all anagrams
def findAllAnagrams(s, p):

    ans= []
    shash = [0]*26
    phash = [0]*26

    sLen, pLen = len(s), len(p)
    l, r = 0, 0
    #fill them up for the first window only
    while(r < pLen):
        print(p[r])
        phash[ord(p[r]) - ord('a')]+=1
        shash[ord(s[r]) - ord('a')]+=1
        r+=1
    r-=1
    while (r < sLen):

    # This is when all hash.size are the same
    # then add the left pointer idx
        if (phash == shash):
            ans.append(l)

        r+=1

        # if not at the end yet
        # Increase the counter for the character at the right
        if (r != sLen):
            shash[ord(s[r])-ord('a')]+=1


        # decrease counter for elem at the left
        shash[ord(s[l])-ord('a')]-=1
        l+=1

    return ans

print(findAllAnagrams(s, p))











