
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


def canContains(bagsDict, bag, bagName):
    count = 0
    for bId in bag.getContains():
        if bId == bagName:
            count += 1
        elif bId in bagsDict.keys():
            count += canContains(bagsDict, bagsDict[bId], bagName)
    return (count)


def main():
    f = open("./inputs.txt")
    bagsDict = {}
    for l in f:
        b = Bag(l)
        bagsDict[b.getId()] = b

    total = 0
    for bag in bagsDict:
        total += 1 if canContains(bagsDict,
                                  bagsDict[bag], "shiny gold") > 0 else 0
    print(total)


if __name__ == "__main__":
    main()
