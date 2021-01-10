# advent of code 2015
# day 6

# part 1
input = open('day-06.txt', 'r').read()

def countLights(input, partTwo = False):
    instructions = input.split('\n')
    grid = []
    for r in range(1000):
        if partTwo == False:
            grid.append([-1] * 1000)
        else:
            grid.append([0] * 1000)
    for instr in instructions:
        if 'turn on' in instr:
            coords = [int(x) for x in ','.join(instr.split('turn on ')[1].split(' through ')).split(',')]
            for r in range(coords[0], coords[2] + 1):
                for c in range(coords[1], coords[3] + 1):
                    if partTwo == False:
                        grid[r][c] = 1
                    else:
                        grid[r][c] += 1
        elif 'turn off' in instr:
            coords = [int(x) for x in ','.join(instr.split('turn off ')[1].split(' through ')).split(',')]
            for r in range(coords[0], coords[2] + 1):
                for c in range(coords[1], coords[3] + 1):
                    if partTwo == False:
                        grid[r][c] = -1
                    else:
                        grid[r][c] = max([0, grid[r][c] - 1])
        else:
            coords = [int(x) for x in ','.join(instr.split('toggle ')[1].split(' through ')).split(',')]
            for r in range(coords[0], coords[2] + 1):
                for c in range(coords[1], coords[3] + 1):
                    if partTwo == False:
                        grid[r][c] *= -1
                    else:
                        grid[r][c] += 2
    if partTwo == False:
        return([item for sublist in grid for item in sublist].count(1))
    else:
        return(sum([item for sublist in grid for item in sublist]))

countLights(input)

countLights(input, partTwo = True)