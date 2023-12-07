from typing import List
import re


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


def solve(file_path: str = "inputs/day04.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    lines = [line.split(":") for line in lines]
    card_names = [line[0].replace("   ", " ").replace("  ", " ") for line in lines]
    counts = []
    cards = {k[1]: 1 for k in enumerate(card_names)}
    for line in lines:
        card_name = line[0].replace("   ", " ").replace("  ", " ")
        card_number = re.findall(r'\d+', card_name)[0]
        card_split = line[1].split("|")
        winning_numbers = card_split[0].strip().split(" ")
        winning_numbers = [i for i in winning_numbers if i]
        actual_numbers = card_split[1].strip().split(" ")
        actual_numbers = [i for i in actual_numbers if i]
        results = {}
        for i in winning_numbers:
            results[i] = actual_numbers.count(i)
        winning_cards = sum(results.values())
        for i in range(int(card_number) + 1, int(card_number) + winning_cards + 1):
            for j in range(0, cards[card_name]):
                cards[f"Card {i}"] += 1

    return sum(cards.values())


if __name__ == "__main__":
    solution = solve()
    print(f"Day 4, Part 2: {solution}")
