def part_1():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            nums = list(filter(lambda x: x.isnumeric(), line.strip('')))
            total += int(nums[0] + nums[-1])
        print(total)


def part_2():
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        total = 0
        numbers = []
        for line in lines:
            i = 0
            arr = []
            while i < len(line):
                if line[i: i + 3] == 'one':
                    arr.append(1)
                    i += 3
                elif line[i: i + 3] == 'two':
                    arr.append(2)
                    i += 3
                elif line [i : i + 4] == 'three':
                    arr.append(3)
                    i += 4
