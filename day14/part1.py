
def nbToBin36(nb):
    str = bin(int(nb))[2:]
    i = 0
    res = ''
    while i + len(str) < 36:
        res += '0'
        i += 1
    res += str
    return res


def applyMask(nb, mask):
    nbList = list(nb)
    for index, b in enumerate(mask):
        if b != 'X':
            nbList[index] = b
    return "".join(nbList)


class Memory:
    def __init__(self) -> None:
        super().__init__()
        self.mask = ''
        self.data = {}

    def executeInstruction(self, line):
        ist, data = line[:-1].split(' = ')
        if ist == 'mask':
            self.mask = data
        else:
            address = ist.split('[')[1][:-1]
            self.addData(address, data)

    def addData(self, address, value):
        self.data[address] = applyMask(nbToBin36(value), self.mask)

    def sumUp(self):
        total = 0
        for v in self.data.values():
            total += int(v, 2)
        return total


def main():
    mem = Memory()
    f = open('./inputs.txt')
    for l in f:
        mem.executeInstruction(l)
    print(mem.sumUp())


if __name__ == "__main__":
    main()
