from collections import deque


def read_cards(filename: str):
    with open(filename, 'r') as file:
        cards = []
        for line in file.readlines():
            card = line[line.find(':') + 2:].strip().split('|')
            winning = {int(x) for x in card[0].split(' ') if x != ''}
            picks = [int(x) for x in card[1].split(' ') if x != '']
            cards.append((winning, picks))
        return cards


def part_1():
    cards = read_cards('input.txt')
    total = 0
    for game in cards:
        i = 0
        for pick in game[1]:
            if pick in game[0]:
                i += 1
        if i != 0:
            total += 2 ** (i - 1)
    return total


def part_2():
    cards = read_cards('input.txt')
    cards_queue = deque()
    cards_queue.extend(list(range(1, len(cards) + 1)))
    cards_memo = {}
    total_won = len(cards)
    while len(cards_queue) != 0:
        card_id = cards_queue.pop()
        if cards_memo.get(card_id) is None:
            correct = 0
            winning, picks = cards[card_id - 1]
            for p in picks:
                if p in winning:
                    correct += 1
            cards_memo[card_id] = correct
        correct = cards_memo[card_id]
        total_won += correct
        cards_queue.extend(list(range(card_id + 1, card_id + correct + 1)))
    return total_won


print(part_1())
print(part_2())
