import math

with open("input") as infile:
    heights = [[int(height) for height in line.rstrip(
        '\n')] for line in infile.readlines()]

print(heights)
SIZE_X = len(heights)
SIZE_Y = len(heights[0])

grid = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if (i, j) != (0, 0):
            grid.append((i, j))

# print(grid)


def isLowPoint(coords):
    x, y = coords
    for t in grid:
        x1 = x + t[0]
        y1 = y + t[1]
        if x1 in range(0, SIZE_X) and y1 in range(0, SIZE_Y) and heights[x][y] > heights[x1][y1]:
            return False
    return True


low_points = []
for i in range(SIZE_X):
    for j in range(SIZE_Y):
        if isLowPoint((i, j)):
            low_points.append((i, j))


def basin(x, y, sett):
    sett.add((x, y))
    for (i, j) in grid:
        x1 = x + i
        y1 = y + j
        if x1 in range(0, SIZE_X) and y1 in range(0, SIZE_Y) and heights[x][y]+1 == heights[x1][y1] and heights[x1][y1] != 9:
            sett.add((x1, y1))
            basin(x1, y1, sett)
    return sett


basins = []
for (x, y) in low_points:
    basins.append(len(basin(x, y, set())))

basins.sort(reverse=True)
print(basins)

# too low You guessed 849060
# (You guessed 857070.) [Return to Day 9]