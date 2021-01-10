# advent of code 2015
# day 3

# part 1
input = open('day-03.txt', 'r').read()

def countHouses(input, partTwo = False):
    x = 0
    y = 0
    X = 0
    Y = 0
    i = 0
    addresses = {str(x) + ',' + str(y): 1}
    for sym in [symb for symb in input]:
        if partTwo == True & i % 2 != 0:
            if sym == '>':
                X += 1
            elif sym == '<':
                X -= 1
            elif sym == '^':
                Y += 1
            else:
                Y -= 1
            key = str(X) + ',' + str(Y)
        else:
            if sym == '>':
                x += 1
            elif sym == '<':
                x -= 1
            elif sym == '^':
                y += 1
            else:
                y -= 1
            key = str(x) + ',' + str(y)
        if(key not in addresses.keys()):
            addresses[key] = 1
        i += 1
    return(len(addresses.keys()))

countHouses(input)

# part 2
countHouses(input, partTwo = True)