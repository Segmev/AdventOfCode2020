  
class Microkernel:
    def __init__(self, filepath):
        f = open(filepath, 'r')
        self.instrs = []
        self.index = 0
        self.acc = 0
        for l in f:
            self.instrs.append({
                "countExec": 0,
                "instrName": l.split(' ')[0],
                "instrVal": int(l.split(' ')[1])
            })

    def execute(self):
        while(self.instrs[self.index]['countExec'] == 0):
            self.instrs[self.index]['countExec'] += 1
            if self.instrs[self.index]["instrName"] == "nop":
                self.index += 1
            elif self.instrs[self.index]["instrName"] == "acc":
                self.acc += self.instrs[self.index]["instrVal"]
                self.index += 1
            elif self.instrs[self.index]["instrName"] == "jmp":
                self.index += self.instrs[self.index]["instrVal"]
        print(self.acc)
        

def main():
    mk = Microkernel("inputs.txt")
    mk.execute()

if __name__ == "__main__":
    main()
