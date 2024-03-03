def part_1():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            nums = list(filter(lambda x: x.isnumeric(), line.strip('')))
            total += int(nums[0] + nums[-1])
        print(total)



