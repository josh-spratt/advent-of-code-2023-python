from typing import List


class FileParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def parse_input_lines_to_list(self) -> List[List[int]]:
        with open(self.file_path, "r") as file:
            data = [line for line in file]
        return data


def solve(file_path: str = "inputs/day01.txt") -> int:
    calibration_values = FileParser(file_path).parse_input_lines_to_list()
    calibration_value_sum = 0
    for calibration_value in calibration_values:
        transformed_value = []
        for char in calibration_value:
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                transformed_value.append(char)
        transformed_value = transformed_value[0] + transformed_value[-1]
        calibration_value_sum += int(transformed_value)
    return calibration_value_sum


if __name__ == "__main__":
    solution = solve()
    print(f"Day 1, Part 1: {solution}")
