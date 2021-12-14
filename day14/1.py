with open("input") as fd:
    polymer_template = fd.readline().strip()
    fd.readline()
    pair_insertions = dict([line.strip().split(' -> ')
                            for line in fd.readlines()])

print(polymer_template)
print(pair_insertions)

#ask anto global variables

def step(polymer_template):
    # calculate all insertions
    inserts = []
    for i in range(len(polymer_template) - 1):
        bin = polymer_template[i]+polymer_template[i+1]
        c = pair_insertions[bin]
        if c:
            inserts.append((c, i + 1))
    # insert
    offset = 0
    for (c, i) in inserts:
        ri = i + offset
        offset += 1
        polymer_template = polymer_template[:ri] + c + polymer_template[ri:]
    return polymer_template

for i in range(10):
    polymer_template = step(polymer_template)
    print(i)

count = {c:polymer_template.count(c) for c in set(polymer_template)}

print(max(count.values()) - min(count.values()))