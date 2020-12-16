
class Ticket:
    def __init__(self, fieldsValues, fieldsDict) -> None:
        super().__init__()
        self.values = list(map(lambda x: int(x), fieldsValues.split(',')))
        self.invalidValues = []
        for value in self.values:
            invalid = True
            for boundsArray in fieldsDict.values():
                for bounds in boundsArray:
                    if bounds[0] <= value and value <= bounds[1]:
                        invalid = False
            if invalid:
                self.invalidValues.append(value)

    def getInvalidValues(self):
        return self.invalidValues


def main():
    f = open('./inputs.txt')
    ticketDict = {}
    for l in f:
        if l == '\n':
            break
        key, val = l[:-1].split(': ')
        ticketDict[key] = []
        for bounds in val.split(' or '):
            ticketDict[key].append(
                list(map(lambda x: int(x), bounds.split('-'))))

    f.readline()
    myTicket = Ticket(f.readline()[:-1], ticketDict)
    f.readline()

    tickets = []
    for l in f:
        if l != '\n' and l != 'nearby tickets:\n':
            tickets.append(Ticket(l[:-1], ticketDict))

    total = 0
    for ticket in tickets:
        for v in ticket.getInvalidValues():
            total += v

    print(total)


if __name__ == "__main__":
    main()
