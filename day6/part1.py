

def countAnswers(answers=[]):
    answersDict = {}
    for answer in answers:
        for letter in answer:
            answersDict[letter] = 1
    return len(answersDict)


def main():
    f = open("./inputs.txt")
    answers = []
    total = 0
    for l in f:
        if l[:-1] != "":
            answers += (l[:-1].split(' '))
        else:
            total += countAnswers(answers)
            answers = []
    total += countAnswers(answers)
    print(total)


if __name__ == "__main__":
    main()
