from itertools import groupby
from pprint import pprint
from typing import List


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


class MediumMap:
    def __init__(
        self,
        source_category: str,
        destination_category: str,
        source_range_start: int,
        destination_range_start: int,
        range_length: int,
    ) -> None:
        self.source_category = source_category
        self.destination_category = destination_category
        self.source_range_start = source_range_start
        self.destination_range_start = destination_range_start
        self.range_length = range_length


def solve(file_path: str = "inputs/day05.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    lines = [list(y) for x, y in groupby(lines, key=bool) if x]
    seeds = [int(seed) for seed in lines[0][0].replace("seeds: ", "").split(" ")]
    for mapping in lines[1:]:
        mappings = [line.split(" ") for line in mapping[1:]]
        mapping_name = mapping[0].replace(" map:", "")
        mappings = [[int(mapping) for mapping in x] for x in mappings]
        print(mapping_name)
        pprint(mappings)
        

if __name__ == "__main__":
    solution = solve()
    print(f"Day 5, Part 1: {solution}")
