# this is a hard problem here


# to the englihs stuff here

# 123 here to

# reduce the problem to how to convert 3-digit interger to English word here
#




def thousands(num):
    switcher = {
        0:"",
        1:"Thousands",
        2:"Millions",
        3: "Billions"
    }
    return switcher.get(num)

# for any less than 20 the 2 digits here
def lessThan20(num):
    switcher = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen'
    }
    return switcher.get(num)

# for anything less than 3 digits here
def lessThan100(num):
    switcher = {
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety'
    }
    return switcher.get(num)


def numsToWords(num):
    if(num ==0): return "Zero"

    sb = ""
    index = 0

    while (num > 0):
        if num % 1000 != 0:
            tmp = ""
            tmp = helper(tmp, num %1000)

            # we add the tmp at the begininng here
            print(" the tmp is ", tmp)
            sb = (tmp+thousands(index))+ sb +" "

        index+=1
        num = num//1000

    return sb


# number here is the remainder of each division here
def helper(tmp, num):
    if (num == 0):
        print("finally here", tmp)
        return tmp


    elif num < 20:
        tmp += (lessThan20(num)) + " "
        print("i came here", tmp)
        return tmp

    elif num < 100:
        print("i came here")
        tmp += (lessThan100(num // 10)) + " "
        return helper(tmp, num % 10)
    # this will handle > 100: the 3 digits  if 333 / 100: num = 33
    else:
        print("num is ", num)
        tmp += (lessThan20(num //100)) + " hundred "
        return helper(tmp, num % 100)
print(numsToWords(123))


print(lessThan20(1))