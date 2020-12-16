import pprint

pp = pprint.PrettyPrinter(indent=4)

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

    tickets = [myTicket]
    for l in f:
        if l != '\n' and l != 'nearby tickets:\n':
            tickets.append(Ticket(l[:-1], ticketDict))

    tickets = list(filter(lambda x: (len(x.getInvalidValues()) == 0), tickets))

    for ticket in tickets:
        for index, value in enumerate(ticket.values):
            for boundsArray in ticketDict.values():
                for bounds in boundsArray[:2]:
                    if bounds[0] <= value and value <= bounds[1]:
                        if len(boundsArray) < 3:
                            boundsArray.append([])
                        boundsArray[2].append(index)


    resultDict = {}
    while (len(ticketDict) > len(resultDict)):
        toBeRemoved = []
        for ticketDictKey in ticketDict:
            indexes = []
            maxCount = 0
            for i in range(min(ticketDict[ticketDictKey][2]), max(ticketDict[ticketDictKey][2]) + 1):
                if maxCount < (ticketDict[ticketDictKey][2].count(i)):
                    indexes = [i]
                    maxCount = ticketDict[ticketDictKey][2].count(i)
                elif maxCount == (ticketDict[ticketDictKey][2].count(i)):
                    indexes.append(i)
            if len(indexes) == 1 and not(ticketDictKey in resultDict):
                resultDict[ticketDictKey] = indexes[0]
                toBeRemoved.append(indexes[0])

        for index in toBeRemoved:
            for ticketDictKey in ticketDict:
                ticketDict[ticketDictKey][2] = list(filter(lambda x: x != index, ticketDict[ticketDictKey][2]))
    pp.pprint(resultDict)

    pp.pprint(myTicket.values)
    res = 1
    for key in resultDict:
        if key.split(' ')[0] == 'departure':
            res *= myTicket.values[resultDict[key]]

    print(res)

if __name__ == "__main__":
    main()
