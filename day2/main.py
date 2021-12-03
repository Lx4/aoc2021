from input import input


def split_tuple(line):
    a, b = line.split()
    return (a, int(b))

with open("raw.txt") as infile:
    data = [split_tuple(line) for line in infile.readlines()]

# part 1    

def plannedCourse(input):
    horizontal = 0
    depth = 0

    for direction, mov in input:
        if direction == 'up':
            depth -= mov
        if direction == 'down':
            depth += mov
        if direction == 'forward':
            horizontal += mov
    return horizontal * depth


print("solution to part 1 is", plannedCourse(input))

# part 2


def plannedCourse2(input):
    horizontal = 0
    depth = 0
    aim = 0

    for direction, mov in input:
        if direction == 'up':
            aim -= mov
        if direction == 'down':
            aim += mov
        if direction == 'forward':
            horizontal += mov
            depth += aim * mov
    return horizontal * depth


print("solution to part 2 is", plannedCourse2(input))
