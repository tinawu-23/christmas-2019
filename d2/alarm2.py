def findres(data): 
    i = 0
    while data[i] != 99 and i < len(data) and data[i+1] < len(data) and data[i+2] < len(data) and data[i+3] < len(data):
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        i += 4
    return data[0]


with open('input.txt') as f:
    orgdata = [int(n) for n in f.readlines()[0].strip().split(',')]

for n in range(100):
    for v in range(100):
        d = orgdata[:]
        d[1], d[2] = n, v
        if findres(d) == 19690720:
            print(100*n+v)