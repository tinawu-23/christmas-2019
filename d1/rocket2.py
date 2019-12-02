def getfuel(fuel):
    fuel = fuel // 3 - 2
    if fuel < 9:
        return fuel
    fuel += getfuel(fuel)
    return fuel

total = 0
with open('input.txt') as f:
    for line in f:
        mass = int(line.strip())
        total += getfuel(mass)
print(total)
