

def countAnswers(answers=[]):
    answersDict = {}
    for answer in answers:
        for letter in answer:
            if letter in answersDict:
                answersDict[letter] += 1
            else:
                answersDict[letter] = 1
    count = 0
    for key in answersDict:
        if answersDict[key] == len(answers):
            count += 1
    return count


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
