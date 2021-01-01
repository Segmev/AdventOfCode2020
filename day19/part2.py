
def cleanRule(instructions):
    cleanedInstructions = []
    for instr in instructions:
        if instr[0] == "\"":
            return (instr[1:-1])
        else:
            cleanedInstructions.append(int(instr))
    return cleanedInstructions

def main():
    f = open('./inputs.txt')
    rules = {}
    for l in f:
        if l == '\n':
            break
        rules[int(l.split(': ')[0])] = list(map(cleanRule, [r.split(' ')
                                                            for r in l.split(': ')[1][:-1].split(' | ')]))

    messages = []
    for l in f:
        messages.append(l[:-1])

    count = 0
    for m in messages:
        if checkMessage(rules, m):
            count += 1
    print(count)

maxCount = 0
def checkRule(rules, rulesId, message, inloopcount = 0):
    if inloopcount >= maxCount:
        return -1
    indexes = []
    for i, ruleId in enumerate(rulesId):
        indexes.append(indexes[len(indexes) - 1] if len(indexes) > 0 else 0)
        tmp = []
        for idInstr, instr in enumerate(rules[ruleId]):
            tmp.append(0)
            if isinstance(instr, str):
                if indexes[i] < len(message) and message[indexes[i]] == instr:
                    indexes[i] += 1
                else:
                    return 0
            else:
                if rulesId == instr:
                    inloopcount += 1
                tmp[idInstr] = checkRule(rules, instr, message[indexes[i]:], inloopcount)
                if inloopcount > maxCount:
                    tmp[idInstr] = 0
        indexes[i] += max(tmp)
    return max(indexes)

def checkMessage(rules, message):
    return checkRule(rules, rules[0][0], message) == len(message)

if __name__ == "__main__":
    while maxCount < 150:
        print(maxCount)
        main()
        maxCount += 1