import re

def operations(nb1, operator, nb2):
    if operator == '+':
        return nb1 + nb2
    if operator == '-':
        return nb1 - nb2
    if operator == '/':
        return nb1 / nb2
    if operator == '*':
        return nb1 * nb2
    if operator == '%':
        return nb1 % nb2
    print(operator)
    return 0

def calculate(str):
    tokens = str.split(' ')
    while len(tokens) > 2:
        tokens[2] = operations(int(tokens[0]), tokens[1], int(tokens[2]))
        del(tokens[0])
        del(tokens[0])
    return int(tokens[0])

def main():
    regex = r'\(([^(]*?)\)'
    f = open('./inputs.txt')

    total = 0
    for l in f:
        matches = re.findall(regex, l)
        while len(matches) > 0:
            m = matches[0]
            res = calculate(m)
            l = l[:l.find(m) - 1] + str(res) + l[l.find(m) + len(m) + 1:]
            matches = re.findall(regex, l)
        total += calculate(l)
    print(total)

if __name__ == "__main__":
    main()