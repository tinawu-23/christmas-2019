from itertools import permutations


class IntcodeComputer:

    def __init__(self, inputs):
        with open('input.txt') as f:
            self.codes = [int(x) for x in f.readlines()[0].split(',')]

        self.i = 0
        self.icnt = 0
        self.input = [inputs]

    def compute(self, newinput):
        self.input.append(newinput)

        while self.i < len(self.codes):
            code = ('00000' + str(self.codes[self.i]))[-5:]

            p1 = code[1]
            p2 = code[2]
            p = code[3:5]

            self.i += 1

            if p == '99':
                return None

            if p == '03':  # input
                self.codes[self.codes[self.i]] = self.input[self.icnt]
                self.icnt += 1
                self.i += 1

            elif p == '04':  # output
                output = self.codes[self.codes[self.i]]
                self.i += 1
                return output

            else:
                x = self.codes[self.codes[self.i]] if p2 == '0' else self.codes[self.i]
                y = self.codes[self.codes[self.i + 1]] if p1 == '0' else self.codes[self.i + 1]

                if p == '01':  # addition
                    self.codes[self.codes[self.i + 2]] = x + y
                    self.i += 3

                elif p == '02':  # multiplication
                    self.codes[self.codes[self.i + 2]] = x * y
                    self.i += 3

                elif p == '05':  # jump-if-true
                    if x != 0:
                        self.i = y
                    else:
                        self.i += 2

                elif p == '06':  # jump-if-false
                    if x == 0:
                        self.i = y
                    else:
                        self.i += 2

                elif p == '07':  # less than
                    self.codes[self.codes[self.i + 2]] = 1 if x < y else 0
                    self.i += 3

                elif p == '08':  # equals
                    self.codes[self.codes[self.i + 2]] = 1 if x == y else 0
                    self.i += 3


seq = permutations([5, 6, 7, 8, 9])
best = 0

for s in list(seq):
    ampA = IntcodeComputer(s[0])
    ampB = IntcodeComputer(s[1])
    ampC = IntcodeComputer(s[2])
    ampD = IntcodeComputer(s[3])
    ampE = IntcodeComputer(s[4])

    ampseq = [ampA, ampB, ampC, ampD, ampE]
    
    i = 0
    n2 = 0
    status = 'run'
    while status != 'done':
        if i == 5:
            i = 0
        n2 = ampseq[i].compute(n2)
        if not n2:
            status = 'done'
            break
        best = max(best, n2)
        i += 1

print(best)