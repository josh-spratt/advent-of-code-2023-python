from typing import List
from pprint import pprint
from collections import Counter

STRENGTH_OF_CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


class Hand:
    def __init__(self, cards: List[str]) -> None:
        self.cards = cards

    def translate_hand(self):
        # Five of a kind
        if len(set(self.cards)) == 1:
            return "five_of_a_kind"
        # Four of a kind
        elif 4 in Counter(self.cards).values():
            return "four_of_a_kind"
        # Full house
        elif 2 in Counter(self.cards).values() and 3 in Counter(self.cards).values():
            return "full_house"
        # Three of a kind
        elif 3 in Counter(self.cards).values():
            return "three_of_a_kind"
        # Two pair
        elif len(set(self.cards)) == 3:
            return "two_pair"
        # Pair
        elif 2 in Counter(self.cards).values():
            return "pair"
        # High card
        else:
            return "high_card"


def solve(file_path: str = "inputs/day07.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    lines = [tuple(line.split(" ")) for line in lines]
    cards = [line[0] for line in lines]
    for card in cards:
        print([*card])
        hand = Hand([*card])
        translation = hand.translate_hand()


if __name__ == "__main__":
    solution = solve()
    print(f"Day 7, Part 1: {solution}")
