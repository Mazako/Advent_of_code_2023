import math


def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def is_symbol(string: str) -> bool:
    return not string.isnumeric() and string != '.'


def part_1():
    total = 0
    arr = read_input('input.txt')
    for i in range(0, len(arr)):
        tmp = ''
        adjacent = False
        j = 0
        while j < len(arr[i]):
            while j < len(arr[i]) and arr[i][j].isnumeric():
                tmp += arr[i][j]
                for k in range(i - 1, i + 2):
                    for L in range(j - 1, j + 2):
                        if 0 <= k < len(arr) and 0 <= L < len(arr[i]) and is_symbol(arr[k][L]):
                            adjacent = True
                j += 1
            if adjacent:
                total += int(tmp)
            tmp = ''
            adjacent = False
            j += 1
    return total


def part_2():
    arr = read_input('input.txt')
    numbers = []
    symbols = {}
    for i in range(len(arr)):
        tmp = ''
        for j in range(len(arr[i])):
            if arr[i][j].isnumeric():
                tmp += arr[i][j]
            elif tmp != '':
                numbers.append((int(tmp), i, j - len(tmp), j - 1))
                tmp = ''
            if arr[i][j] == '*':
                symbols[(i, j)] = []
        if tmp != '':
            numbers.append((int(tmp), i, len(arr[i]) - len(tmp), len(arr[i])))
    for number in numbers:
        for i in range(number[1] - 1, number[1] + 2):
            for j in range(number[2] - 1, number[3] + 2):
                if symbols.get((i, j)) is not None:
                    symbols[(i, j)].append(number[0])

    total = 0
    for symbol in symbols.values():
        if len(symbol) == 2:
            total += math.prod(symbol)

    return total


print(part_1())
print(part_2())
