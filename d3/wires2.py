with open('input.txt') as f:
    paths = f.readlines()
    path1, path2 = paths[0].split(','), paths[1].split(',')

points1, points2 = {}, {}
x, y = 0, 0
points1[(x, y)] = 0
points2[(x, y)] = 0

step = 0
for instruction in path1:
    direction = instruction[0]
    steps = int(instruction[1:])
    if direction == 'U':
        while steps > 0:
            y += 1
            step += 1
            if (x, y) not in points1:
                points1[(x, y)] = step
            steps -= 1
    elif direction == 'D':
        while steps > 0:
            y -= 1
            step += 1
            if (x, y) not in points1:
                points1[(x, y)] = step
            steps -= 1
    elif direction == 'L':
        while steps > 0:
            x -= 1
            step += 1
            if (x, y) not in points1:
                points1[(x, y)] = step
            steps -= 1
    elif direction == 'R':
        while steps > 0:
            x += 1
            step += 1
            if (x, y) not in points1:
                points1[(x, y)] = step
            steps -= 1

x, y = 0, 0
step = 0
for instruction in path2:
    direction = instruction[0]
    steps = int(instruction[1:])
    if direction == 'U':
        while steps > 0:
            y += 1
            step += 1
            if (x, y) not in points2:
                points2[(x, y)] = step
            steps -= 1
    elif direction == 'D':
        while steps > 0:
            y -= 1
            step += 1
            if (x, y) not in points2:
                points2[(x, y)] = step
            steps -= 1
    elif direction == 'L':
        while steps > 0:
            x -= 1
            step += 1
            if (x, y) not in points2:
                points2[(x, y)] = step
            steps -= 1
    elif direction == 'R':
        while steps > 0:
            x += 1
            step += 1
            if (x, y) not in points2:
                points2[(x, y)] = step
            steps -= 1

p1 = set(points1.keys())
p2 = set(points2.keys())
intersect = p1 & p2
minsteps = float('INF')
for pt in intersect:
    if pt == (0, 0):
        continue
    totsteps = points1[pt] + points2[pt]
    if totsteps < minsteps:
        minsteps = totsteps

print(minsteps)