# advent of code 2015
# day 4

# part 1
from hashlib import md5 as md5

input = open('day-04.txt', 'r').read()

def findMinHash(input, partTwo = False):
    i = 0
    while(True):
        key = input + str(i)
        hex = md5(key.encode()).hexdigest()
        if partTwo == True and ''.join([x for x in hex][0:6]) == '000000':
            return(i)
        elif partTwo == False and ''.join([x for x in hex][0:5]) == '00000':
            return(i)
        i += 1

findMinHash(input)

# part 2
findMinHash(input, partTwo = True)