

def main():
    f = open('inputs.txt')
    nbs = [0]
    for l in f:
        nbs.append(int(l))
    nbs.sort()
    nbs.append(nbs[-1] + 3)

    nbsDict = {}
    nbsDict[0] = 1

    for nb in nbs[1:]:
        nbsDict[nb] = nbsDict.get(nb-3, 0) + nbsDict.get(nb-2, 0) + nbsDict.get(nb-1, 0)
    print(nbsDict)
    print(nbsDict[max(nbsDict.keys())])


if __name__ == "__main__":
    main()
