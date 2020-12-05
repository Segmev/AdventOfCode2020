import math

def upperHalf(a, b):
    return math.ceil((b - a) / 2)

def lowerHalf(a, b):
    return math.floor((b - a) / 2)

class BoardPlace:
    def __init__(self) -> None:
        self.vl = 0
        self.vu = 127
        
        self.hl = 0
        self.hu = 7
    
    def __call__(self, instruction):
        if instruction == 'B':
            self.vl += upperHalf(self.vl, self.vu)
        elif instruction == 'F':
            self.vu -= lowerHalf(self.vl, self.vu)
        elif instruction == 'R':
            self.hl += upperHalf(self.hl, self.hu)
        elif instruction == 'L':
            self.hu -= lowerHalf(self.hl, self.hu)

    def print(self):
        print(self.vl, self.vu, self.hl, self.hu)

    def id(self):
        return self.vl * 8 + self.hl

def main():
    f = open("./inputs.txt")
    higherId = 0
    for instr in f:
        bp = BoardPlace()
        for letter in instr:
            bp(letter)
        higherId = bp.id() if higherId < bp.id() else higherId
    print(higherId)

main()