with open('input.txt') as f:
    data = [int(n) for n in f.readlines()[0].strip().split(',')]

i = 0
while i < len(data) and data[i] != 99:
    if data[i] == 1:
        data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
    elif data[i] == 2:
        data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
    i += 4

print(data)