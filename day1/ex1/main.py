

def main():
    tab = []
    f = open("./input.txt", "r")
    for l in f:
        tab.append(int(l))
    for index, nb in enumerate(tab):
        for index2, nb2 in enumerate(tab):
            for index3, nb3 in enumerate(tab):
                if index != index2 and index != index3:
                    if nb + nb2 + nb3 == 2020:
                        return nb * nb2 * nb3
    
print(main())