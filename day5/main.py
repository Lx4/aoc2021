def strListToIntTuple(s):
    l = s.split(',')
    a, b = l
    return (int(a), int(b))


with open('input') as infile:
    data = [[strListToIntTuple(n)
             for n in line.rstrip('\n').split('->')] for line in infile.readlines()]

print(data)

# init a diagram 1000x1000
DIMENSION = 1000
diagram = []
for i in range(DIMENSION):
    arr = []
    for j in range(DIMENSION):
        arr.append(0)
    diagram.append(arr)


# coords are tuple (x, y)
def draw(coord1, coord2):
    # draw horizontal line
    x1, y1 = coord1
    x2, y2 = coord2
    if x1 == x2:
        print('draw horizontal', x1)
        r = range(y1, y2+1)
        if y1 > y2:
            r = range(y2, y1+1)
        for i in r:
            diagram[x1][i] += 1
    # draw vertical line
    elif y1 == y2:
        print('draw vertical', y1)
        r = range(x1, x2+1)
        if x1 > x2:
            r = range(x2, x1+1)
        for i in r:
            diagram[i][y1] += 1
    # draw diagonal
    elif abs(x1-x2) == abs(y1-y2):
        # point de depart et direction
        dirX = 1
        dirY = 1
        if x2 < x1:
            dirX = -1
        if y2 < y1:
            dirY = -1
        for i in range(abs(x1-x2) + 1):
            diagram[x1+(i*dirX)][y1+(i*dirY)] += 1
        print("draw diag")


# draw in diagram
for coord1, coord2 in data:
    draw(coord1, coord2)

print(diagram)

# count all value > 2 in diagram
count = 0
for row in diagram:
    for elem in row:
        if elem >= 2:
            count += 1
print(count)

# guess 21942 (too high) wrong direction implementation
# guess 18843 (too low) range error
# time to complete : 1h10mn
