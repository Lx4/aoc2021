with open("input") as infile:
    data = [int(n) for n in infile.readline().split(',')]

NUM_DAYS = 256

# init state with data
state = [0] * 9
for i in data:
    state[i] += 1

# rotate table, keep list concise
for _ in range(NUM_DAYS):
    spawns = state[0]
    # rotate index 0 to 6
    state = state[1:7] + state[0:1] + state[7:9]
    state[6] += state[7]
    state[7] = state[8]
    state[8] = spawns

print(f'solution is {sum(state)}')
