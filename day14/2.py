#from collections import Counter

with open("sample") as fd:
    polymer_template = fd.readline().strip()
    fd.readline()
    pair_insertions = dict([line.strip().split(' -> ')
                            for line in fd.readlines()])

print(polymer_template)
dick = {}
for i in range(len(polymer_template)-1):
    t = polymer_template[i]+polymer_template[i+1]
    if t in dick:
        dick[t] += 1
    else:
        dick[t] = 1

print(dick)

# print(pair_insertions)

# ask anto global variables

#print(pair_insertions)

def step(dick):
    # calculate all insertions
    for p, c in pair_insertions.items():
        #print(p,c)
        c1 = p[0]+c
        c2 = c+p[1]
        if c1 in dick:
            dick[c1] += 1
        if c2 in dick:
            dick[c2] += 1
        pass

step(dick)
print(dick)