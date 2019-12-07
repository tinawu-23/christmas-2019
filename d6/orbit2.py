edges = {}
tot = 0

with open('input.txt') as f:
    for line in f:
        a, b = line.strip().split(')')
        edges[b] = a

dist = {}
p = "YOU"
step = 0
while p in edges:
    dist[p] = step
    step += 1
    p = edges[p]

p = "SAN"
step = 0
while p in edges:
    if p in dist:
        print(step + dist[p] - 2)
        exit()
    step += 1
    p = edges[p]