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
        pos = 1
        for i, token in enumerate(tokens):
            if token == '+':
                pos = i
                break
        tokens[pos + 1] = operations(int(tokens[pos - 1]), tokens[pos], int(tokens[pos + 1]))
        del(tokens[pos - 1])
        del(tokens[pos - 1])
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
            l = l[:(l.find('(' + m + ')'))] + str(res) + l[(l.find('(' + m + ')')) + (len('(' + m + ')')):]
            matches = re.findall(regex, l)
        total += calculate(l)
    print(total)

if __name__ == "__main__":
    main()