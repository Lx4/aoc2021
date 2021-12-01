from input import data


def sonar(array):
    counter = 0
    for i, _ in enumerate(array):
        if i == 0:
            continue
        if (array[i] > array[i-1]):
            counter = counter + 1
    return counter

# part 1  
print("answer part 1 is", sonar(data))

# part 2
summed = [data[i] + data[i+1] + data[i+2] for i in range(0, len(data) - 2)]

print(sonar(summed))
