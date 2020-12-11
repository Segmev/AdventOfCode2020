

def countSeats(map):
    total = 0
    for l in map:
        total += l.count('#')
    return total


def getValue(map, x, y):
    if y >= 0 and y < len(map) and x >= 0 and x < len(map[y]):
        return map[y][x]
    return ' '


def getFirstSeats(map, x, y):
    seats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                stepI, stepJ = i, j
                while getValue(map, x + stepI, y + stepJ) == '.':
                    stepI += i
                    stepJ += j
                seats.append(getValue(map, x + stepI, y + stepJ))
    return seats


def emptySeat(map, x, y):
    if getFirstSeats(map, x, y).count('#') == 0:
        return '#'
    return 'L'


def occupiedSeat(map, x, y):
    if getFirstSeats(map, x, y).count('#') >= 5:
        return 'L'
    return '#'


def nextStep(map=[]):
    newMap = []
    for yindex, l in enumerate(map):
        newMap.append('')
        for xindex, val in enumerate(l):
            if l[xindex] == 'L':
                newMap[yindex] += emptySeat(map, xindex, yindex)
            elif l[xindex] == '#':
                newMap[yindex] += occupiedSeat(map, xindex, yindex)
            else:
                newMap[yindex] += val
    return newMap


def printMap(map):
    for l in map:
        print(l)


def main():
    map = []
    f = open("inputs.txt")
    for l in f:
        map.append(l[:-1])

    for _ in range(0, 100):
        # printMap(map)
        print(countSeats(map))
        map = nextStep(map)


if __name__ == "__main__":
    main()
