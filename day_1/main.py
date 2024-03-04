def part_1():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            nums = list(filter(lambda x: x.isnumeric(), line.strip('')))
            total += int(nums[0] + nums[-1])
        return total


def part_2():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            i = 0
            arr = []
            while i < len(line):
                if line[i: i + 3] == 'one':
                    arr.append('1')
                    i += 2
                elif line[i: i + 3] == 'two':
                    arr.append('2')
                    i += 2
                elif line[i: i + 5] == 'three':
                    arr.append('3')
                    i += 4
                elif line[i: i + 4] == 'four':
                    arr.append('4')
                    i += 3
                elif line[i: i + 4] == 'five':
                    arr.append('5')
                    i += 3
                elif line[i: i + 3] == 'six':
                    arr.append('6')
                    i += 2
                elif line[i: i + 5] == 'seven':
                    arr.append('7')
                    i += 4
                elif line[i: i + 5] == 'eight':
                    arr.append('8')
                    i += 4
                elif line[i: i + 4] == 'nine':
                    arr.append('9')
                    i += 3
                elif line[i].isnumeric():
                    arr.append(line[i])
                    i += 1
                else:
                    i += 1
            total += int(arr[0] + arr[-1])
    return total

print(part_1())
print(part_2())
