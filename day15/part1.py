
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
    gameNumbers = [12,1,16,3,11,0]
    index = len(gameNumbers)
    while index < 2020:
        gameNumbers.append(findPreviousOccurrence(gameNumbers, gameNumbers[len(gameNumbers) - 1]))
        index += 1
    print(gameNumbers[index -1])

if __name__ == "__main__":
    main()
