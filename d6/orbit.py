edges = {}
planets = set()
tot = 0

with open('input.txt') as f:
    for line in f:
        a, b = line.strip().split(')')
        edges[b] = a
        planets.add(b)

for planet in planets:
    p = planet
    while p in edges:
        p = edges[p]
        tot += 1

print(tot)