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


total = 0
for i in range(SIZE_X):
    for j in range(SIZE_Y):
        if isLowPoint((i, j)):
            total += heights[i][j] + 1

print(total)
