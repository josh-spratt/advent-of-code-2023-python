from typing import List
from pprint import pprint


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


def solve(file_path: str = "inputs/day05.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()


if __name__ == "__main__":
    solution = solve()
    print(f"Day 5, Part 2: {solution}")
