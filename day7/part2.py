
class Bag:
    def __init__(self, line):
        self.id = line.split(' contain ')[0].split(' bags')[0]
        self.contains = {}
        if line.split(' contain ')[1] != "no other bags.\n":
            for bagTxt in line.split(' contain ')[1].split(', '):
                id = bagTxt[bagTxt.find(' ') + 1:bagTxt.rfind(' ')]
                self.contains[id] = int(bagTxt[:(bagTxt.find(' '))])

    def getId(self):
        return self.id

    def getContains(self):
        return self.contains

    def get(self):
        return self


def countBags(bagsDict, bag):
    count = 0
    for bId in bag.getContains():
        count += bag.getContains()[bId]
        count += countBags(bagsDict, bagsDict[bId]) * bag.getContains()[bId]
    return count


def main():
    f = open("./inputs.txt")
    bagsDict = {}
    for l in f:
        b = Bag(l)
        bagsDict[b.getId()] = b

    print(countBags(bagsDict, bagsDict['shiny gold']))


if __name__ == "__main__":
    main()
