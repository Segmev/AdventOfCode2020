

def countSeats(map):
    total = 0
    for l in map:
        total += l.count('#')
    return total


def getValue(map, x, y):
    if y >= 0 and y < len(map) and x >= 0 and x < len(map[y]):
        return map[y][x]
    return '.'


def countAround(map, x, y, tc):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if getValue(map, x + i, y + j) in tc:
                    count += 1
    return count


def emptySeat(map, x, y):
    if countAround(map, x, y, ['#']) == 0:
        return '#'
    return 'L'


def occupiedSeat(map, x, y):
    if countAround(map, x, y, ['#']) >= 4:
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
    f = open("./inputs.txt")
    for l in f:
        map.append(l[:-1])

    for _ in range(0, 1000):
        # printMap(map)
        print(countSeats(map))
        map = nextStep(map)


if __name__ == "__main__":
    main()
