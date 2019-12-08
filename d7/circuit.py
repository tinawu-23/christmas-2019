from itertools import permutations

def computer(inputs):

    with open('input.txt') as f:
        codes = [int(x) for x in f.readlines()[0].split(',')]

    i = 0
    icnt = 0
    output = 0

    while i < len(codes):
        code = ('00000' + str(codes[i]))[-5:]

        p1 = code[1]
        p2 = code[2]
        p = code[3:5]

        i += 1

        if p == '99':
            return

        if p == '03':  # input
            codes[codes[i]] = inputs[icnt]
            icnt += 1
            i += 1

        elif p == '04':  # output
            return codes[codes[i]]

        else:
            x = codes[codes[i]] if p2 == '0' else codes[i]
            y = codes[codes[i + 1]] if p1 == '0' else codes[i + 1]

            if p == '01': # addition
                codes[codes[i + 2]] = x + y
                i += 3

            elif p == '02': # multiplication
                codes[codes[i + 2]] = x * y
                i += 3

            elif p == '05':  # jump-if-true
                if x != 0: i = y
                else: i += 2

            elif p == '06':  # jump-if-false
                if x == 0: i = y
                else: i += 2

            elif p == '07':  # less than
                codes[codes[i + 2]] = 1 if x < y else 0
                i += 3

            elif p == '08':  # equals
                codes[codes[i + 2]] = 1 if x == y else 0
                i += 3
      

seq = permutations([0, 1, 2, 3, 4])
best = 0

for s in list(seq):
    i = 0
    n1, n2 = 0, 0
    while i < len(s):
        n1 = s[i]
        n2 = computer([n1, n2])
        i += 1
    best = max(n2, best)

print(best)