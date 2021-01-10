# advent of code 2015
# day 1

# part 1
import timeit
input = open('day-01.txt', 'r').read()

def navigateFloors(input, partTwo = False):
    inputList = [1 if char == '(' else -1 if char == ')' else 0 for char in input]
    if partTwo == False:
        return(sum(inputList))
    else:
        i = 0
        cumSum = 0
        while(cumSum >= 0):
            cumSum += inputList[i]
            i += 1
        return(i)

navigateFloors(input)

# part 2
navigateFloors(input, partTwo = True)
