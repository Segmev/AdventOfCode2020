import re

eclVal = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def betweenCheck(nb1, nb2):
    return lambda nb: nb1 <= int(nb) and int(nb) <= nb2


def heightCheck(fieldVal):
    if fieldVal[-2:] == "cm":
        return betweenCheck(150, 193)(int(fieldVal[:-2]))
    if fieldVal[-2:] == "in":
        return betweenCheck(59, 76)(int(fieldVal[:-2]))
    return False


def hairCheck(fieldVal):
    return re.match('^#[0-9a-f]{6}$', fieldVal) != None


def eclCheck(fieldVal):
    return fieldVal in eclVal


def pidCheck(fieldVal):
    return re.match("^[0-9]{9}$", fieldVal) != None


class PassportChecker:
    def __init__(self) -> None:
        self.rules = {
            "byr": betweenCheck(1920, 2002),
            "iyr": betweenCheck(2010, 2020),
            "eyr": betweenCheck(2020, 2030),
            "hgt": heightCheck,
            "hcl": hairCheck,
            "ecl": eclCheck,
            "pid": pidCheck,
            "cid": lambda x: True
        }
        self.optionalRules = ["cid"]

    def checkEnoughFields(self, passportFields):
        passDict = {}
        for baseField in self.rules:
            passDict[baseField] = 0
        for field in passportFields:
            fieldName, _ = field.split(':')
            passDict[fieldName] = 1
        for fieldname in self.rules:
            if fieldname not in self.optionalRules and passDict[fieldname] == 0:
                return False
        print(passDict, passportFields)
        return True

    def checkFields(self, passportFields):
        if not self.checkEnoughFields(passportFields):
            return False
        for field in passportFields:
            fieldName, fieldVal = field.split(':')
            if self.rules[fieldName](fieldVal) == False:
                return False
        print(passportFields)
        return True


def main():
    f = open("inputs.txt", "r")
    passport = []
    pChecker = PassportChecker()

    counter = 0
    for l in f:
        if l != "\n":
            passport += (l[:-1].split(' '))
        else:
            if pChecker.checkFields(passport):
                counter += 1
            passport = []
    print(counter)


main()
