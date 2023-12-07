from typing import List
from collections import defaultdict


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


def get_neighboring_points(matrix, i, j):
    neighbors = []
    if i == 0 and j == 0:
        right_neighbor = (i, j + 1)
        diag_bottom_right_neighbor = (i + 1, j + 1)
        bottom_neighbor = (i + 1, j)
        neighbors.append(right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
        neighbors.append(bottom_neighbor)
    elif i == 0 and j == len(matrix[0]) - 1:
        bottom_neighbor = (i + 1, j)
        left_neighbor = (i, j - 1)
        diag_bottom_left_neighbor = (i + 1, j - 1)
        neighbors.append(bottom_neighbor)
        neighbors.append(left_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
    elif i == len(matrix) - 1 and j == 0:
        top_neighbor = (i - 1, j)
        diag_top_right_neighbor = (i - 1, j + 1)
        right_neighbor = (i, j + 1)
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(right_neighbor)
    elif i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        top_neighbor = (i - 1, j)
        diag_top_left_neighbor = (i - 1, j - 1)
        left_neighbor = (i, j - 1)
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(left_neighbor)
    elif i == 0:
        right_neighbor = (i, j + 1)
        diag_bottom_right_neighbor = (i + 1, j + 1)
        bottom_neighbor = (i + 1, j)
        diag_bottom_left_neighbor = (i + 1, j - 1)
        left_neighbor = (i, j - 1)
        neighbors.append(right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
        neighbors.append(left_neighbor)
    elif i == len(matrix) - 1:
        diag_top_left_neighbor = (i - 1, j - 1)
        top_neighbor = (i - 1, j)
        diag_top_right_neighbor = (i - 1, j + 1)
        right_neighbor = (i, j + 1)
        left_neighbor = (i, j - 1)
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(right_neighbor)
        neighbors.append(left_neighbor)
    elif j == 0:
        top_neighbor = (i - 1, j)
        bottom_neighbor = (i + 1, j)
        right_neighbor = (i, j + 1)
        diag_top_right_neighbor = (i - 1, j + 1)
        diag_bottom_right_neighbor = (i + 1, j + 1)
        neighbors.append(top_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(right_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
    elif j == len(matrix[0]) - 1:
        top_neighbor = (i - 1, j)
        bottom_neighbor = (i + 1, j)
        left_neighbor = (i, j - 1)
        diag_top_left_neighbor = (i - 1, j - 1)
        diag_bottom_left_neighbor = (i + 1, j - 1)
        neighbors.append(top_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(left_neighbor)
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
    else:
        diag_top_left_neighbor = (i - 1, j - 1)
        top_neighbor = (i - 1, j)
        diag_top_right_neighbor = (i - 1, j + 1)
        right_neighbor = (i, j + 1)
        diag_bottom_right_neighbor = (i + 1, j + 1)
        bottom_neighbor = (i + 1, j)
        diag_bottom_left_neighbor = (i + 1, j - 1)
        left_neighbor = (i, j - 1)
        neighbors.append(diag_top_left_neighbor)
        neighbors.append(top_neighbor)
        neighbors.append(diag_top_right_neighbor)
        neighbors.append(right_neighbor)
        neighbors.append(diag_bottom_right_neighbor)
        neighbors.append(bottom_neighbor)
        neighbors.append(diag_bottom_left_neighbor)
        neighbors.append(left_neighbor)
    return neighbors


def find_matching_coordinates(A, B):
    for index, coordinates in A.items():
        matching_keys = set()

        for coord in coordinates:
            for b_dict in B:
                dict_key = next(iter(b_dict))
                if coord in b_dict[dict_key]:
                    matching_keys.add(dict_key)

        if len(matching_keys) == 2:
            return matching_keys


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


def find_key(tuples_list, dictionary):
    for key, value in dictionary.items():
        if any(t in value for t in tuples_list):
            return key
    return None  # Return None if no match is found


def solve(file_path: str = "inputs/day03.txt") -> int:
    # A gear is any * symbol that is adjacent to exactly two part numbers.
    # Its gear ratio is the result of multiplying those two numbers together.
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    lines = [[*line] for line in lines]

    asterisks = {}
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            if lines[i][j] == "*" and [
                x for x in get_neighbors(lines, i, j) if x.isdigit()
            ]:
                neighbor_points = get_neighboring_points(lines, i, j)
                if [x for x in neighbor_points if lines[x[0]][x[1]].isdigit()]:
                    asterisks[(i, j)] = [
                        x for x in neighbor_points if lines[x[0]][x[1]].isdigit()
                    ]

    number_coordinates = parse_numbers_with_coordinates(lines)
    new_guy = {}
    for k, v in asterisks.items():
        for x in number_coordinates:
            for l, m in x.items():
                if any(i in m for i in v):
                    try:
                        new_guy[k].append(l)
                    except KeyError:
                        new_guy[k] = [l]

    sum = 0
    for k, v in new_guy.items():
        if len(v) == 2:
            sum += int(v[0]) * int(v[1])
    return sum


if __name__ == "__main__":
    solution = solve()
    print(f"Day 3, Part 2: {solution}")
