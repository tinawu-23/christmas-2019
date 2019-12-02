fuel = 0
with open('input.txt') as f:
    for line in f:
        mass = int(line.strip())
        fuel += mass // 3 - 2
print(fuel)