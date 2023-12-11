from itertools import groupby
from typing import List


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
    lines = [list(y) for x, y in groupby(lines, key=bool) if x]
    seeds = [int(seed) for seed in lines[0][0].replace("seeds: ", "").split(" ")]

    all_location_numbers = []  # Find the min of this to get the answer

    for seed in seeds:
        for mapping in lines[1:]:
            mapping_integers = [x.split(" ") for x in mapping[1:]]
            mapping_integers = [[int(x) for x in y] for y in mapping_integers]
            for mapping_integer in mapping_integers:
                if (
                    seed >= mapping_integer[1]
                    and seed <= mapping_integer[1] + mapping_integer[2]
                ):
                    seed = seed - (mapping_integer[1] - mapping_integer[0])
                    break
                seed = seed
        all_location_numbers.append(seed)
    return min(all_location_numbers)


if __name__ == "__main__":
    solution = solve()
    print(f"Day 5, Part 1: {solution}")
