from typing import List

MAPPING_DICT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}


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
        transformed_values = []
        calibration_value = [*calibration_value]
        word = ""
        for char in calibration_value:
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                transformed_values.append(char)
                break
            else:
                word += char
            if any(
                (match := substring) in word for substring in list(MAPPING_DICT.keys())
            ):
                transformed_values.append(str(MAPPING_DICT[match]))
                word = ""
                break
        calibration_value.reverse()
        word = ""
        for char in calibration_value:
            if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                transformed_values.append(char)
                break
            else:
                word += char
            if any(
                (match := substring) in word[::-1]
                for substring in list(MAPPING_DICT.keys())
            ):
                transformed_values.append(str(MAPPING_DICT[match]))
                word = ""
                break
        first_last = transformed_values[0] + transformed_values[-1]
        calibration_value_sum += int(first_last)
    return calibration_value_sum


if __name__ == "__main__":
    solution = solve()
    print(f"Day 1, Part 1: {solution}")
