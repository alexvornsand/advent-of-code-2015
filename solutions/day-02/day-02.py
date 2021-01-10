# advent of code 2015
# day 2

# part 1
input = open('day-02.txt', 'r').read()

def orderPaper(input, partTwo = False):
    boxes = input.split('\n')
    def processBox(box, partTwo):
        dims = [int(x) for x in box.split('x')]
        if partTwo == False:
            sides = [dims[0] * dims[1], dims[0] * dims[2], dims[1] * dims[2]]
            sqFeet = 2 * sum(sides) + min(sides)
        else:
            circ = 2 * sum(sorted(dims)[0:2])
            vol = dims[0] * dims[1] * dims[2]
            sqFeet = circ + vol
        return(sqFeet)
    return(sum([processBox(x, partTwo = partTwo) for x in boxes]))

orderPaper(input)

# part 2
orderPaper(input, partTwo = True)
