
class LineCheck:
    def __init__(self, line) -> None:
        tokens = line.split(' ')
        self.password = tokens[2][:-1]
        self.rule = list(map(lambda t: int(t) - 1, tokens[0].split('-')))
        self.letter = tokens[1][0]
    
    def __call__(self):
        if self.rule[0] < len(self.password):
            if self.password[self.rule[0]] == self.letter and (self.rule[1] >= len(self.password) or self.password[self.rule[1]] != self.letter):
                return True
        if self.rule[1] < len(self.password):
            if self.password[self.rule[1]] == self.letter and self.password[self.rule[0]] != self.letter:
                return True
        return False

def main():
    f = open("inputs.txt", 'r')

    lineCheckers = []
    for l in f:
        lineCheckers.append(LineCheck(l))
    
    count = 0
    for LC in lineCheckers:
        if LC():
            count += 1
    print(count)

main()