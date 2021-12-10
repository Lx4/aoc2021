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

stack = []
errors = []

for line in data:
    for c in line:
        if c in openers:
            stack.append(c)
        elif len(stack) != 0 and matching_chars(stack[-1], c):
            stack.pop()
        else:
            errors.append(c)
            stack = []
            break

total = 0
for c in errors :
    if c == ')':
        total+=3
    if c == ']':
        total+=57
    if c == '}':
        total+=1197
    if c == '>':
        total+=25137


print(total)

