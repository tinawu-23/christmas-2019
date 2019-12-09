with open('input.txt') as f:
    digits = f.readlines()[0]

layers = [[] for i in range(len(digits)//(25*6))]
layer = 0
for i, d in enumerate(digits):
    if i != 0 and i % 150 == 0:
        layer += 1
    layers[layer].append(d)

layer = 0
image = [[] for i in range(6)]

for i in range(25*6):
    if i != 0 and i % 25 == 0:
        layer += 1
    lcnt = 0
    while lcnt < len(layers):
        if layers[lcnt][i] != '2':
            image[layer].append(layers[lcnt][i])
            break
        lcnt += 1

for lst in image:
    print(' '.join(lst))