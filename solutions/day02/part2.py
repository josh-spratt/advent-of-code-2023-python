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
    power_sum = 0
    for line in lines:
        min_red = 0
        min_green = 0
        min_blue = 0
        regex_matches = re.findall(r"(\b\d+\b)\s+(\w+)", line)
        for item in regex_matches:
            if item[1] == "red" and int(item[0]) > min_red:
                min_red = int(item[0])
            elif item[1] == "green" and int(item[0]) > min_green:
                min_green = int(item[0])
            elif item[1] == "blue" and int(item[0]) > min_blue:
                min_blue = int(item[0])
        power = min_red * min_green * min_blue
        power_sum += power
    return power_sum


if __name__ == "__main__":
    solution = solve()
    print(f"Day 2, Part 2: {solution}")
