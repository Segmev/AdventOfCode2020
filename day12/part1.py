
directions = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}


class Boat():
    def __init__(self):
        self.coorX = 0
        self.coorY = 0
        self.dir = 90

    def action(self, order):
        direction = order[:1]
        value = int(order[1:])
        if direction == 'F':
            direction = directions[self.dir]
        if direction == 'L' or direction == 'R':
            self.dir = ((self.dir + value) %
                        360) if direction == 'R' else (abs((self.dir - value) % 360))
        else:
            if direction == 'N':
                self.coorY -= value
            elif direction == 'S':
                self.coorY += value
            elif direction == 'E':
                self.coorX += value
            elif direction == 'W':
                self.coorX -= value
        print(order, [direction, value], [self.dir, self.coorX, self.coorY])

    def printPosition(self):
        print(abs(self.coorX) + abs(self.coorY))


def main():
    boat = Boat()
    f = open("inputs.txt")
    for l in f:
        boat.action(l[:-1])
    boat.printPosition()


if __name__ == "__main__":
    main()
