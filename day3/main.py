with open("input.txt") as infile:
    data = [list(line.rstrip("\n")) for line in infile.readlines()]

# part 1
count = []
for i in data[0]:
    count.append(0)

for entry in data:
    for i in range(len(entry)):
        if entry[i] == "0":
            count[i] -= 1
        else:
            count[i] += 1

gamma_rate = ''
epsilon_rate = ''
for n in count:
    if n > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
print('g', gamma_rate)
print('gamma_rate', int(gamma_rate, 2))
print('epsilon_rate', int(epsilon_rate, 2))
print('power_consumption', int(gamma_rate, 2)*int(epsilon_rate, 2))

# part 2 : rework and push
print('part 2')

def most_common_bit_ox(l: list, index: int):
    total = sum(int(entry[index]) for entry in l)
    return '1' if total >= len(l) / 2 else '0'


def most_common_bits_ox(data: list):
    return ''.join([most_common_bit_ox(data, i) for i in range(len(data[0]))])


def most_common_bit_co2(l: list, index: int):
    total = sum(int(entry[index]) for entry in l)
    return '0' if total >= len(l) / 2 else '1'


def most_common_bits_co2(data: list):
    return ''.join([most_common_bit_co2(data, i) for i in range(len(data[0]))])


copy_ox = data[:]
index = 0
while (len(copy_ox) > 1):
    most_common = most_common_bits_ox(copy_ox)
    copy_ox = [d for d in copy_ox if d[index] == most_common[index]]
    index += 1

copy_co2 = data[:]
index = 0
while (len(copy_co2) > 1):
    most_common = most_common_bits_co2(copy_co2)
    copy_co2 = [d for d in copy_co2 if d[index] == most_common[index]]
    index += 1
print("solution to part2 is", int(
    ''.join(copy_ox[0]), 2) * int(''.join(copy_co2[0]), 2))
