from typing import List

class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


def recursive_calculate_differences(line: List[int]) -> List[List[int]]:
    if len(line) <= 1 or all(elem == 0 for elem in line):
        return [line]
    else:
        differences = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        return [line] + recursive_calculate_differences(differences)


def fill_up(matrix: List[List]) -> List[List]:
    # Add an additional 0 to the bottom list
    matrix[-1].append(0)
    
    # Iterate over the matrix in reverse order
    for i in range(len(matrix) - 1, 0, -1):
        # Calculate the sum of the last element in the current list and the last element in the next list
        total = matrix[i][-1] + matrix[i - 1][-1]
        # Add the sum to the next list
        matrix[i - 1].append(total)
    return matrix


def solve(file_path: str = "inputs/day09.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    lines = [list(map(int, line.split(" "))) for line in lines]
    total_sum = 0
    for line in lines:
        differences = recursive_calculate_differences(line)
        matrix = fill_up(differences)
        total_sum += matrix[0][-1]
    return total_sum


if __name__ == "__main__":
    solution = solve()
    print(f"Day 9, Part 1: {solution}")
