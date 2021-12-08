with open("input") as infile:
    data = [line.rstrip().split('|')[1].lstrip().split(' ') for line in infile.readlines()]

counts = [[len(digits) for digits in l] for l in data]
# 1 : 2 digits
# 4 : 4
# 7 : 3
# 8 : 7


EASY_DIGITS = [2, 4, 3, 7]

def easyDigits(digit):
    if digit in EASY_DIGITS:
        return True
    return False

total = 0
for row in counts:
    for digit in row:
        if easyDigits(digit):
            total+=1

print(data)
print(counts)
print(total)

#2

def decode(signal_patterns):
    decoded = ['']*10
    for signal in signal_patterns:
        size = len(signal)
        if (size == 2):
            decoded[1] = signal
