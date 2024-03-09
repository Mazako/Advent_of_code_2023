def create_game(line: str):
    line = line.strip()
    pos = line.find(':')
    game_id = int(line[:pos].split(' ')[1])
    games = line[pos + 2:].split('; ')
    arr = []
    for game in games:
        colors = [0, 0, 0]
        for c in game.split(', '):
            c = c.split(' ')
            if c[1] == 'red':
                colors[0] = int(c[0])
            elif c[1] == 'green':
                colors[1] = int(c[0])
            else:
                colors[2] = int(c[0])
        arr.append(colors)

    return game_id, arr


def part_1():
    with open('input.txt', 'r') as file:
        d = {x: y for (x, y) in [create_game(line) for line in file.readlines()]}
        total = 0
        for (k, v) in d.items():
            exceeded = False
            for game in v:
                if game[0] > 12 or game[1] > 13 or game[2] > 14:
                    exceeded = True
            if not exceeded:
                total += k
        return total

def part_2():
    with open('input.txt', 'r') as file:
        d = {x: y for (x, y) in [create_game(line) for line in file.readlines()]}
        total = 0
        for v in d.values():
            red = max(list(map(lambda x: x[0], v)))
            green = max(list(map(lambda x: x[1], v)))
            blue = max(list(map(lambda x: x[2], v)))
            total += red * green * blue
        return total


print(part_1())
print(part_2())
