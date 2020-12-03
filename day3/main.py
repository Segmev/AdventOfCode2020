
class Map:
    def __init__(self, path) -> None:
        self.content = []
        self.rowsCount = 0
        f = open(path, 'r')
        for l in f:
            self.rowsCount += 1
            self.content.append(l[:-1])

    def rowsCount(self):
        return self.rowsCount
    
    def rowsLen(self):
        return len(self.content[0])

    def countTrees(self, stepsX, stepsY):
        trees = 0
        x, y = 0, 0
        while y < self.rowsCount:
            if self.content[y][x % self.rowsLen()] == '#':
                trees += 1
            x += stepsX
            y += stepsY
            
        return trees

def main():
    map = Map("inputs.txt")
    stepsList = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res = 1
    print(map.countTrees(stepsList[1][0], stepsList[1][1]))
    for steps in stepsList:
        res *= map.countTrees(steps[0], steps[1])
    print(res)

main()