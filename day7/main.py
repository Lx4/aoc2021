with open("input") as infile:
    data = [int(n) for n in infile.readline().split(',')]

# part1
MAX = max(data)

fuels = []
for i in range(MAX):
    fuel = 0
    for n in data:
        fuel += abs(i - n)
    fuels.append(fuel)

print(f'solution to pqrt 1 is : {min(fuels)}')

# part 2
fuels = []
for i in range(MAX):
    fuel = 0
    for n in data:
        x = abs(i - n)
        t = (x * (x+1))//2
        fuel += t
    fuels.append(fuel)

print(f'solution to pqrt 2 is : {min(fuels)}')
