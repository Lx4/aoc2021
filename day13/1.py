import re

pattern = "fold along ([x,y])=([0-9]+)"

with open("input") as fd:
    input = fd.read().split("\n\n")
    dots = set([tuple([int(x) for x in coords.split(',')])
                for coords in input[0].split()])
    folds = []
    for l in input[1].split('\n'):
        m = re.search(pattern, l)
        if m:
            folds += [(m.group(1), int(m.group(2)))]

# print(dots)
# print(folds)


def fold_vertical(coords, fi):
    s = set()
    for x, y in coords:
        if x > fi:
            t = (fi - (x - fi), y)
            s.add(t)
        else:
            s.add((x, y))
    return s


def fold_horizontal(coords, fi):
    s = set()
    for x, y in coords:
        if y > fi:
            t = (x, fi - (y - fi))
            s.add(t)
        else:
            s.add((x, y))
    return s


# s = fold_vertical(dots, 7)
for fold in folds:
    if fold[0] == 'x':
        dots = fold_vertical(dots, fold[1])
    elif fold[0] == 'y':
        dots = fold_horizontal(dots, fold[1])

for i in range(10):
    for j in range(50):
        if (j, i) in dots:
            print('█', end="")
        else:
            print('.', end="")
    print()
# 860 : too high
