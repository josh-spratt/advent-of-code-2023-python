from typing import List
import re


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


def solve(file_path: str = "inputs/day02.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    game_number = 1
    impossible_games = set()
    for line in lines:
        regex_matches = re.findall(r"(\b\d+\b)\s+(\w+)", line)
        for item in regex_matches:
            if (
                item[1] == "red"
                and int(item[0]) > 12
                or item[1] == "green"
                and int(item[0]) > 13
                or item[1] == "blue"
                and int(item[0]) > 14
            ):
                impossible_games.add(game_number)
        game_number += 1
    counter = 0
    for i in range(1, 101):
        if i not in impossible_games:
            counter += i
    return counter


if __name__ == "__main__":
    solution = solve()
    print(f"Day 2, Part 1: {solution}")
