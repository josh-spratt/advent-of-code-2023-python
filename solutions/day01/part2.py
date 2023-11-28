from itertools import groupby
from typing import List


class InputFile:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def parse_input_lines_to_list(self) -> List[List[int]]:
        with open(self.file_path, "r") as file:
            data = [
                int(line.strip()) if line != "\n" else line.strip() for line in file
            ]
        return [list(g) for k, g in groupby(data, key=bool) if k]


def calculate_top3_elf_calories(data: List[List[int]]) -> int:
    elf_calories = [sum(group) for group in data]
    elf_calories.sort(reverse=True)
    return sum(elf_calories[0:3])


def solve(file_path: str = "inputs/day01.txt") -> int:
    input_file = InputFile(file_path)
    parsed_data = input_file.parse_input_lines_to_list()
    result = calculate_top3_elf_calories(data=parsed_data)
    return result


if __name__ == "__main__":
    solution = solve()
    print(f"Day 1, Part 2: {solution}")
