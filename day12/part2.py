import math

directions = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W'
}

class Coor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, value):
        value = math.radians(value)
        nx = self.x * math.cos(value) - self.y * (math.sin(value))
        ny = self.x * (math.sin(value)) + self.y * math.cos(value)
        self.x = round(nx)
        self.y = round(ny)

class Boat(Coor):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.wp = Coor(10, -1)

    def action(self, command):
        order = command[:1]
        value = int(command[1:])

        if order == 'F':
            self.x += value * self.wp.x
            self.y += value * self.wp.y
        elif order == 'R':
            self.wp.rotate(value)
        elif order == 'L':
            self.wp.rotate(-value)
        else:
            if order == 'N':
                self.wp.y -= value
            elif order == 'S':
                self.wp.y += value
            elif order == 'W':
                self.wp.x -= value
            elif order == 'E':
                self.wp.x += value
        print(order, [order, value], [self.x, self.y], [self.wp.x, self.wp.y])

    def printPosition(self):
        print(abs(self.x) + abs(self.y))


def main():
    boat = Boat(0, 0)
    f = open("inputs.txt")
    for l in f:
        boat.action(l[:-1])
    boat.printPosition()


if __name__ == "__main__":
    main()
