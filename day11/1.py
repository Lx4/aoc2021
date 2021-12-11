with open("input") as fd:
    data = [[int(num) for num in line.strip()] for line in fd]

print(data)
# X vertical, Y horizontal
X_SIZE = len(data)  # number of lines
Y_SIZE = len(data)  # length of a line

# tuples of adjacent coords : grid
grid = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if (i, j) != (0, 0):
            grid.append((i, j))

# First, the energy level of each octopus increases by 1. this remove all 0 cases
def increase_all_by_1():
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            data[x][y] += 1

# handle flash and immediate propagation from coord x,y


def calculate_flash(x, y):
    if data[x][y] <= 9:
        return False
    data[x][y] = 0
    for (i, j) in grid:
        x1 = x + i
        y1 = y + j
        # if data[x1][y1] = 0, it flashes this time
        if x1 in range(0, X_SIZE) and y1 in range(0, Y_SIZE) and data[x1][y1] != 0:
            data[x1][y1] += 1
    return True

def step(num):
    total_flash = 0
    for _ in range(num):
        increase_all_by_1()
        flash = True
        while(flash):
            flash = False
            for x in range(X_SIZE):
                for y in range(Y_SIZE):
                    if calculate_flash(x, y):
                        total_flash+= 1
                        flash = True
    return total_flash

print(step(100))
