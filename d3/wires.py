with open('input.txt') as f:
    paths = f.readlines()
    path1, path2 = paths[0].split(','), paths[1].split(',')

points1, points2 = set(), set()
x, y = 0, 0
points1.add((x, y))
points2.add((x, y))

for instruction in path1:
    direction = instruction[0]
    steps = int(instruction[1:])
    if direction == 'U':
        while steps > 0:
            y += 1
            points1.add((x, y))
            steps -= 1
    elif direction == 'D':
        while steps > 0:
            y -= 1
            points1.add((x, y))
            steps -= 1
    elif direction == 'L':
        while steps > 0:
            x -= 1
            points1.add((x, y))
            steps -= 1
    elif direction == 'R':
        while steps > 0:
            x += 1
            points1.add((x, y))
            steps -= 1

x, y = 0, 0
for instruction in path2:
    direction = instruction[0]
    steps = int(instruction[1:])
    if direction == 'U':
        while steps > 0:
            y += 1
            points2.add((x, y))
            steps -= 1
    elif direction == 'D':
        while steps > 0:
            y -= 1
            points2.add((x, y))
            steps -= 1
    elif direction == 'L':
        while steps > 0:
            x -= 1
            points2.add((x, y))
            steps -= 1
    elif direction == 'R':
        while steps > 0:
            x += 1
            points2.add((x, y))
            steps -= 1

intersect = points1.intersection(points2)
distance = float('INF')
for pt in intersect:
    if pt == (0,0):
        continue
    dist = abs(pt[0]) + abs(pt[1])
    if dist < distance:
        distance = dist
print(distance)
