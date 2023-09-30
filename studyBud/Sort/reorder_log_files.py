

# letter logs consists of letters as shown here
'''
# letter logs start with letters @ second place:

let2 own kit dig

# digit logs start with digits there:

dig1 8 1 5 1

'''
class Solution:
   def reorderLogFiles(self, logs):
      words = []
      nums = []
      for log in logs:
         s = log.split()


         # all the digits will be shown at the 2nd character here
         if s[1].isdigit():
            nums.append(log)
         else:
            words.append(log)


      for word in words:
         print(word)
      #then we sort the logs by their content first and then identifier next
      words.sort(key = lambda x:(x.split(' ', 1)[1], x.split(' ', 1)[0]))
      return words + nums

ob = Solution()
print(ob.reorderLogFiles(["dig1 9 2 5 2","let1 art can","dig2 4\
8","let2 own kit dig","let3 art zero"]))