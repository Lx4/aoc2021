with open("input") as infile:
    signal_patterns = [line.rstrip().split('|')[0].rstrip().split(' ')
                       for line in infile.readlines()]
with open("input") as infile:
    output_values = [line.rstrip().split('|')[1].lstrip().split(' ')
                     for line in infile.readlines()]

# print(signal_patterns)
# print(output_values)

# digit has 7 position : 0 to 6
# 0 top, 1 topR, 2 mid, 3 botR, 4 bot, 5 botL, 6 topL

# botR is 4 and 1 intersection
# topR is the rest
# top is 7 - 1
# 3 includes 1 and has len5
# 9 includes 3 and has len6 (3 - 9 => topL)
# 8 - 9 => botL
# 6 is 8 without topR
# 5 is len5


# 0 : 6
# 2 : 5
# 3 : 5
# 5 : 5
# 6 : 6
# 9 : 6

# 5 = 9 - 1 + 4
# 2 =

# 0 il a 6 et include 1

def isSubStr(sub, str):
    for c in sub:
        if c not in str:
            return False
    return True


def decodeSignal(signal_pattern):
    decoded = ['']*10
    decoded[1] = [l for l in signal_pattern if len(l) == 2][0]
    decoded[4] = [l for l in signal_pattern if len(l) == 4][0]
    decoded[7] = [l for l in signal_pattern if len(l) == 3][0]
    decoded[8] = [l for l in signal_pattern if len(l) == 7][0]
    # 0 il a 6 et include 1
    decoded[9] = [l for l in signal_pattern if len(
        l) == 6 and isSubStr(decoded[4], l)][0]
    decoded[6] = [l for l in signal_pattern if len(l) == 6 and not isSubStr(
        decoded[4], l) and not isSubStr(decoded[1], l)][0]
    decoded[0] = [l for l in signal_pattern if len(l) == 6 and not isSubStr(
        decoded[4], l) and isSubStr(decoded[1], l)][0]
    decoded[3] = [l for l in signal_pattern if len(
        l) == 5 and isSubStr(decoded[1], l)][0]
    decoded[5] = [l for l in signal_pattern if len(
        set(l) & set(decoded[6])) == 5 and l not in decoded][0]
    return decoded


def decOutput(output, decodeTable):
    s1 = set(output)
    for i in range(10):
        if set(decodeTable[i]) == s1:
            # print(i)
            return i
    # only one not in table xd
    return 2


sol = []
for i in range(len(signal_patterns)):
    decodeTable = decodeSignal(signal_patterns[i])
    # print(decodeTable)
    dec = ''
    for output in output_values[i]:
        dec += str(decOutput(output, decodeTable))
    sol.append(dec)

total = 0
for num in sol:
    total += int(num)

print(total)

# print(sol)
