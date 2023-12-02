from typing import List


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


def solve(file_path: str = "inputs/day01.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    calibration_value_sum = 0
    for line in lines:
        integer_line = []
        for char in line:
            if char.isdigit():
                integer_line.append(char)
        calibration_value_sum += int(integer_line[0] + integer_line[-1])
    return calibration_value_sum


if __name__ == "__main__":
    solution = solve()
    print(f"Day 1, Part 1: {solution}")
