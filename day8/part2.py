
class Microkernel:
    def __init__(self, filepath):
        f = open(filepath, 'r')
        self.instrs = []
        self.index = 0
        self.accumulator = 0
        self.testedFaulty = []
        self.actualFaulty = -1
        for l in f:
            self.instrs.append({
                "countExec": 0,
                "instrName": l.split(' ')[0],
                "instrVal": int(l.split(' ')[1]),
                "faulty": True
            })

    def jmp(self):
        if self.faulty():
            self.index += 1
        else:
            self.index += self.instrs[self.index]["instrVal"] if self.instrs[self.index]["instrVal"] != 0 else 1

    def nop(self):
        if self.faulty():
            self.index += self.instrs[self.index]["instrVal"] if self.instrs[self.index]["instrVal"] > 0 else 1
        else:
            self.index += 1

    def acc(self):
        self.accumulator += self.instrs[self.index]["instrVal"]
        self.index += 1

    def restart(self):
        if self.actualFaulty > 0:
            print('restart with index', self.actualFaulty,
                  'and already tested', self.testedFaulty)
        if self.actualFaulty >= 0:
            self.testedFaulty.append((self.actualFaulty))
        self.actualFaulty = -1
        self.accumulator = 0
        self.index = 0
        for i in self.instrs:
            i['countExec'] = 0

    def faulty(self):
        if self.actualFaulty < 0 and self.index not in self.testedFaulty:
            self.actualFaulty = self.index
            print('testing ', self.actualFaulty)
            return True
        return self.actualFaulty == self.index

    def execute(self):
        while not self.index == len(self.instrs):
            self.restart()
            while self.index < len(self.instrs) and self.instrs[self.index]['countExec'] < 10:
                self.instrs[self.index]['countExec'] += 1
                if self.instrs[self.index]["instrName"] == "nop":
                    self.nop()
                elif self.instrs[self.index]["instrName"] == "acc":
                    self.acc()
                elif self.instrs[self.index]["instrName"] == "jmp":
                    self.jmp()

        print("response:", self.accumulator)


def main():
    mk = Microkernel("inputs.txt")
    mk.execute()


if __name__ == "__main__":
    main()
