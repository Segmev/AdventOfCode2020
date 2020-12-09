

class HackCodeCal:
    def __init__(self):
        self.previousNb = []

    def testNb(self, nb):
        for index1, nb1 in enumerate(self.previousNb):
            for index2, nb2 in enumerate(self.previousNb):
                if index1 != index2 and nb1 + nb2 == nb:
                    return True
        return False

    def __call__(self, nb):
        if len(self.previousNb) >= 25:
            validity = self.testNb(nb)
            del self.previousNb[0]
            self.previousNb.append(nb)
            return validity
        else:
            self.previousNb.append(nb)
            return True


def main():
    hcc = HackCodeCal()
    f = open("./inputs.txt")
    for l in f:
        if not hcc(int(l)):
            print(l)
            break

if __name__ == "__main__":
    main()
