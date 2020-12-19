class Cube:
    def __init__(self, x, y, z) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return "|%d|%d|%d|" % (self.x, self.y, self.z)

    def __repr__(self):
        return "|%d|%d|%d|" % (self.x, self.y, self.z)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Cube):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.x == o.x and self.y == o.y and self.z == o.z

    def getNeighbors(self, cubes):
        neighbors = []
        for cube in cubes:
            if (abs(self.x - cube.x) > 1 or abs(self.y - cube.y) > 1 or abs(self.z - cube.z) > 1) or (self == cube):
                continue
            neighbors.append(cubes)
        return neighbors


def main():
    f = open('./inputs.txt')
    cubes = []
    for il, l in enumerate(f):
        for ic, c in enumerate(l):
            if c == '#':
                cubes.append(Cube(ic, il, 0))

    print(cubes)
    for _ in range(6):
        nextCubes = []
        for cube in cubes:
            if (len(cube.getNeighbors(cubes))) in [2, 3]:
                if cube not in nextCubes:
                    nextCubes.append(cube)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for k in range(-1, 2):
                        if not(i == j and j == k):
                            testCube = Cube(
                                cube.x + i,
                                cube.y + j,
                                cube.z + k
                            )
                            if not testCube in cubes and len(testCube.getNeighbors(cubes)) == 3:
                                if testCube not in nextCubes:
                                    nextCubes.append(testCube)
        cubes = nextCubes
        print(len(cubes))

def printCubes(cubes):
    for z in range (-5, 5):
        filteredCubes = list(filter(lambda x: x.z == z, cubes))
        filteredCubes.sort(key = lambda o: o.y)
        for y in range (-5, 5):
            for x in range(-5, 5):
                testCube = Cube(x, y, z)
                if testCube in filteredCubes:
                    print('#', end='')
                else:
                    print('.', end='')
            print()
        print("\n\n")

if __name__ == '__main__':
    main()
