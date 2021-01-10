# advent of code 2015
# day 5

# part 1
input = open('day-05.txt', 'r').read()

def countNiceStrings(input, partTwo = False):
    strings = input.split('\n')
    def evaluateString(string):
        characters = [x for x in string]
        if partTwo == False:
            vowels = len([x for x in string if x in ['a', 'e', 'i', 'o', 'u']]) >= 3
            sequential = sum([x == y for (x, y) in zip(characters[:-1], characters[1:])]) > 0
            forbidden = not ('ab' in string or 'cd' in string or 'pq' in string or 'xy' in string)
            criteria = [vowels, sequential, forbidden]
        else:
            doubles = False
            for i in range(len(string) - 2):
                substr = ''.join(characters[i:(i + 2)])
                if len(string.split(substr)) > 2:
                    doubles = True
                    break
            skip = sequential = sum([x == y for (x, y) in zip(characters[:-2], characters[2:])]) > 0
            criteria = [skip, doubles]
        return(sum(criteria) == len(criteria))
    return(sum([evaluateString(x) for x in strings]))

countNiceStrings(input)

# part 2
countNiceStrings(input, partTwo = True)