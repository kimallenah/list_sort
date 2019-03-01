def missing_num(numbers):
    miss = []
    i = 1
    for digit in numbers:
        while digit != i:
            miss.append(i)
            i += 1
        if digit == i:
            i += 1


    return miss

print(missing_num([1, 5]))

