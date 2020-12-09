

class HackCodeCal:
    def __init__(self):
        self.nbs = []
        self.canditates = []

    def printWeaknesses(self, weakness):
        for index, _ in enumerate(self.nbs):
            total = 0
            istart = index
            while index < len(self.nbs):
                total += self.nbs[index]
                if total == weakness and index != istart:
                    self.canditates.append(self.nbs[istart:index + 1])
                    break
                index += 1
        self.canditates.sort()
        print(self.canditates[0][0] + self.canditates[0][-1])

    def addNb(self, nb):
        self.nbs.append(nb)


def main():
    weakness = 20874512
    hcc = HackCodeCal()
    f = open("./inputs.txt")
    for l in f:
        hcc.addNb(int(l))
    hcc.printWeaknesses(weakness)


if __name__ == "__main__":
    main()
