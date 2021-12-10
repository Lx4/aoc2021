with open("input") as infile:
    data = [[char for char in line.rstrip('\n')]
            for line in infile.readlines()]


openers = ['[', '{', '<', '(']


def matching_chars(c1, c2):
    if c1 == '[' and c2 == ']':
        return True
    if c1 == '(' and c2 == ')':
        return True
    if c1 == '{' and c2 == '}':
        return True
    if c1 == '<' and c2 == '>':
        return True
    return False


def return_match(c1):
    if c1 == '[':
        return ']'
    if c1 == '(':
        return ')'
    if c1 == '{':
        return '}'
    if c1 == '<':
        return '>'
    return False


errors = []

lines = []
for line in data:
    stack = []
    lines.append(line)
    for c in line:
        if c in openers:
            stack.append(c)
        elif len(stack) != 0 and matching_chars(stack[-1], c):
            stack.pop()
        else:
            errors.append(c)
            lines.pop()
            stack = []
            break

print(len(lines))

sums = []
for line in lines:
    stack = []
    incompletes = []
    for c in line:
        if c in openers:
            stack.append(c)
        elif len(stack) != 0 and matching_chars(stack[-1], c):
            stack.pop()
    while len(stack):
        incompletes.append(return_match(stack[-1]))
        stack.pop()
    sums.append(incompletes)


def score(c):
    if c == ')':
        return 1
    if c == ']':
        return 2
    if c == '}':
        return 3
    if c == '>':
        return 4


def completion_score(arr):
    total = 0
    for c in arr:
        total = total * 5 + score(c)
    return total


total = []
for sum in sums:
    total.append(completion_score(sum))

total.sort()
print(total[len(total) // 2])
