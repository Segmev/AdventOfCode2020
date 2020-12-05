

class PassportChecker:
    def __init__(self, words) -> None:
        self.words = words
        super().__init__()

    def checkFields(self, passportFields):
        passDict = {}
        for baseField in self.words:
            passDict[baseField] = 0
        for field in passportFields:
            fieldName, _ = field.split(':')
            passDict[fieldName] = 1
        for fieldname in self.words:
            if passDict[fieldname] == 0:
                return False
        print(passDict, passportFields)        
        return True
        
    

def main():
    passportFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    f = open("inputs.txt", "r")
    passport = []
    pChecker = PassportChecker(passportFields)

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