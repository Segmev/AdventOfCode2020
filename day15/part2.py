
def findPreviousOccurrence(tab, nb):
    if tab.count(nb) < 2:
        return 0
    index = len(tab) - 2
    while index >= 0:
        if tab[index] == nb:
            return len(tab) - index - 1
        index -= 1
    return 0

def main():
    gameNumbers = {}
    inputs = [12,1,16,3,11,0]
    index = 0
    for nb in inputs:
        index += 1
        gameNumbers[nb] = [index]
    lastNb = inputs[len(inputs) - 1]
    while index < 30000000:
        index +=1
        roundsNumber = gameNumbers.get(lastNb, [index])
        if len(roundsNumber) == 1:
            gameNumbers[0].append(index)
            if len(gameNumbers[0]) > 2:
                gameNumbers[0] = gameNumbers[0][-2:]
            lastNb = 0
        else:
            lastNb = roundsNumber[-1] - roundsNumber[-2]
            if lastNb in gameNumbers:
                gameNumbers[lastNb].append(index)
                gameNumbers[lastNb] = gameNumbers[lastNb][-2:]
            else:
                gameNumbers[lastNb] = [index]

    print(lastNb)

if __name__ == "__main__":
    main()
