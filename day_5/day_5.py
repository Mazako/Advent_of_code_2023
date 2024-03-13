from typing import Callable, Any


class InputRange:
    def __init__(self, input_range, f):
        self.input_range = input_range
        self.f = f


def read_map(filename):
    STEPS = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    steps_map = {}
    with open(filename, 'r') as file:
        seeds = file.readline().strip()
        seeds = list(map(int, seeds[seeds.find(':') + 2:].split(' ')))
        for i in range(7):
            file.readlines(2)
            arr = []
            while True:
                line = file.readline().strip()
                if line == '':
                    break
                numbers = list(map(int, line.split(' ')))
                source = numbers[1]
                destination = numbers[0]
                _range = numbers[2]
                source_range = range(source, source + _range)
                map_function = lambda x, dest=destination, src=source: dest + (x - src)
                arr.append(InputRange(source_range, map_function))
            steps_map[STEPS[i]] = arr
        return seeds, steps_map

def part_1():
    seeds, steps_map = read_map('example.txt')
    seed = seeds[0]
    example = steps_map['soil'][1]
    if seed in example.input_range:
        print(example.f(seed))



part_1()
