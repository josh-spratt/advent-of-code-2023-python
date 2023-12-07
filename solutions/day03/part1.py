from typing import List


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


def get_neighbors(matrix, i, j):
    neighbors = []
    if i == 0 and j == 0:
        right_neighbor = matrix[i][j + 1]
        diag_bottom_right_neighbor = matrix[i + 1][j + 1]
        bottom_neighbor = matrix[i + 1][j]
        neighbors.append(right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
        neighbors.append(bottom_neighbor)
    elif i == 0 and j == len(matrix[0]) - 1:
        bottom_neighbor = matrix[i + 1][j]
        left_neighbor = matrix[i][j - 1]
        diag_bottom_left_neighbor = matrix[i + 1][j - 1]
        neighbors.append(bottom_neighbor)
        neighbors.append(left_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
    elif i == len(matrix) - 1 and j == 0:
        top_neighbor = matrix[i - 1][j]
        diag_top_right_neighbor = matrix[i - 1][j + 1]
        right_neighbor = matrix[i][j + 1]
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(right_neighbor)
    elif i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        top_neighbor = matrix[i - 1][j]
        diag_top_left_neighbor = matrix[i - 1][j - 1]
        left_neighbor = matrix[i][j - 1]
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(left_neighbor)
    elif i == 0:
        right_neighbor = matrix[i][j + 1]
        diag_bottom_right_neighbor = matrix[i + 1][j + 1]
        bottom_neighbor = matrix[i + 1][j]
        diag_bottom_left_neighbor = matrix[i + 1][j - 1]
        left_neighbor = matrix[i][j - 1]
        neighbors.append(right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
        neighbors.append(left_neighbor)
    elif i == len(matrix) - 1:
        diag_top_left_neighbor = matrix[i - 1][j - 1]
        top_neighbor = matrix[i - 1][j]
        diag_top_right_neighbor = matrix[i - 1][j + 1]
        right_neighbor = matrix[i][j + 1]
        left_neighbor = matrix[i][j - 1]
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(right_neighbor)
        neighbors.append(left_neighbor)
    elif j == 0:
        top_neighbor = matrix[i - 1][j]
        bottom_neighbor = matrix[i + 1][j]
        right_neighbor = matrix[i][j + 1]
        diag_top_right_neighbor = matrix[i - 1][j + 1]
        diag_bottom_right_neighbor = matrix[i + 1][j + 1]
        neighbors.append(top_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(right_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
    elif j == len(matrix[0]) - 1:
        top_neighbor = matrix[i - 1][j]
        bottom_neighbor = matrix[i + 1][j]
        left_neighbor = matrix[i][j - 1]
        diag_top_left_neighbor = matrix[i - 1][j - 1]
        diag_bottom_left_neighbor = matrix[i + 1][j - 1]
        neighbors.append(top_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(left_neighbor)
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
    else:
        diag_top_left_neighbor = matrix[i - 1][j - 1]
        top_neighbor = matrix[i - 1][j]
        diag_top_right_neighbor = matrix[i - 1][j + 1]
        right_neighbor = matrix[i][j + 1]
        diag_bottom_right_neighbor = matrix[i + 1][j + 1]
        bottom_neighbor = matrix[i + 1][j]
        diag_bottom_left_neighbor = matrix[i + 1][j - 1]
        left_neighbor = matrix[i][j - 1]
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
        neighbors.append(left_neighbor)
    return neighbors


def parse_numbers_with_coordinates(matrix: List[List]) -> List[dict]:
    numbers = []
    chars = ""
    coords = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j].isdigit() and j == len(matrix[0]) - 1:
                # print("matrix[i][j].isdigit() and j == len(matrix[0])")
                chars += matrix[i][j]
                # print("adding to chars")
                coords.append((i, j))
                # print("appending coords to list")
                number_dict = {}
                number_dict[chars] = coords
                numbers.append(number_dict)
                # print("adding list of coords to numbers dict")
                chars = ""
                # print("resetting chars to empty")
                coords = []
                # print("resetting coords to empty")
            elif matrix[i][j].isdigit() and j < len(matrix[0]) - 1:
                # print("matrix[i][j].isdigit() and j < len(matrix[0])")
                chars += matrix[i][j]
                # print("adding to chars")
                coords.append((i, j))
                # print("appending coords to list")
            elif matrix[i][j] and chars:
                # print("elif matrix[i][j] and chars:")
                number_dict = {}
                number_dict[chars] = coords
                numbers.append(number_dict)
                # print("adding list of coords to numbers dict")
                chars = ""
                # print("resetting chars to empty")
                coords = []
                # print("resetting coords to empty")
    return numbers


def solve(file_path: str = "inputs/day03.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    lines = [[*line] for line in lines]

    points_neighboring_special_characters = set()

    # Find all the coordinates that neighbor special characters
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            if lines[i][j].isdigit():
                all_neighbors = get_neighbors(lines, i, j)
                if [x for x in all_neighbors if x != "." and not x.isdigit()]:
                    points_neighboring_special_characters.add((i, j))

    # Parse integer coordinates into data structure consisting of their integer value and list of coordinates
    number_coordinates = parse_numbers_with_coordinates(lines)
    totals = []

    # Iterate over all numbers, check if any point neighboring special chars exists
    for x in number_coordinates:
        for y in x.values():
            if any(i in points_neighboring_special_characters for i in y):
                totals.append(int(list(x.keys())[0]))
    return sum(totals)


if __name__ == "__main__":
    solution = solve()
    print(f"Day 3, Part 1: {solution}")
