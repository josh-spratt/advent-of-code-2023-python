from typing import List, Union
from pprint import pprint
from collections import Counter

CARD_TO_ALPHA_MAP = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


def _score_of_hand(hand: str) -> int:
    card_counts = [hand.count(card) for card in hand]
    if 5 in card_counts:
        return 6
    if 4 in card_counts:
        return 5
    if 3 in card_counts:
        if 2 in card_counts:
            return 4
        return 3
    if card_counts.count(2) == 4:
        return 2
    if 2 in card_counts:
        return 1
    return 0


def _hand_replacements(hand: str) -> List[str]:
    if hand == "":
        return [""]
    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in _hand_replacements(hand[1:])
    ]


def _type_of_hand(hand: str) -> int:
    return max(map(_score_of_hand, _hand_replacements(hand)))


def strength_of_hand(hand: str) -> int:
    return (_type_of_hand(hand), [CARD_TO_ALPHA_MAP.get(card, card) for card in hand])


def solve(file_path: str = "inputs/day07.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    hands_with_bids = [tuple(line.split(" ")) for line in lines]
    hands_with_bids = [
        (hand_with_bid[0], int(hand_with_bid[1])) for hand_with_bid in hands_with_bids
    ]
    hands_with_bids.sort(key=lambda hand_with_bid: strength_of_hand(hand_with_bid[0]))

    bid_sum = 0
    for x, y in enumerate(hands_with_bids, 1):
        bid_sum += x * y[1]
    return bid_sum


if __name__ == "__main__":
    solution = solve()
    print(f"Day 7, Part 2: {solution}")
