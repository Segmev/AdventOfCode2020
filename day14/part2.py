
def nbToBin36(nb):
    str = bin(int(nb))[2:]
    i = 0
    res = ''
    while i + len(str) < 36:
        res += '0'
        i += 1
    res += str
    return res


def getAddresses(addresses):
    i = 0
    print(addresses)
    while i < len(addresses):
        if addresses[i].count('X') > 0:
            address = addresses.pop(i)
            secondAddress = address[:]
            fx = address.index('X')
            address[fx] = '0'
            secondAddress[fx] = '1'
            addresses.append(address)
            addresses.append(secondAddress)
            i = 0
        else:
            i += 1
    return addresses


def applyMaskOnAddress(nb, mask):
    nbList = list(nbToBin36(nb))
    print(nbList, nb)
    for index, b in enumerate(mask):
        if b != '0':
            nbList[index] = b

    addresses = getAddresses([nbList])
    intAddresses = []
    for address in addresses:
        intAddresses.append(int("".join(address), 2))
    return intAddresses


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
        addresses = applyMaskOnAddress(address, self.mask)
        for address in addresses:
            self.data[address] = (value)

    def sumUp(self):
        total = 0
        for v in self.data.values():
            total += int(v)
        return total


def main():
    mem = Memory()
    f = open('./inputs.txt')
    for l in f:
        mem.executeInstruction(l)
    print(mem.sumUp())


if __name__ == "__main__":
    main()
