with open('input.txt') as f:
    digits = f.readlines()[0]

layers = [[] for i in range(len(digits)//(25*6))]
layer = 0
for i, d in enumerate(digits):
    if i != 0 and i % 150 == 0:
        layer += 1
    layers[layer].append(d)

minzero = float('INF')
layerid = -1
for i, l in enumerate(layers):
    zerocnt = l.count('0')
    if zerocnt < minzero:
        layerid = i
        minzero = zerocnt

print(layers[layerid].count('1') * layers[layerid].count('2'))