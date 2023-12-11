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
    values = [int(seed) for seed in lines[0][0].replace("seeds: ", "").split(" ")]
    seeds = []
    for i in range(0, len(values), 2):
        seeds.append((values[i], values[i] + values[i + 1]))

    for line in lines[1:]:
        mapping_integers = [x.split(" ") for x in line[1:]]
        mapping_integers = [[int(x) for x in y] for y in mapping_integers]
        
        new = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for a, b, c in mapping_integers:
                start_overlap = max(start, b)
                end_overlap = min(end, b + c)
                if start_overlap < end_overlap:
                    new.append((start_overlap - b + a, end_overlap - b + a))
                    if start_overlap > start:
                        seeds.append((start, start_overlap))
                    if end > end_overlap:
                        seeds.append((end_overlap, end))
                    break
            else:
                new.append((start, end))
        seeds = new
    return min(seeds)[0]


if __name__ == "__main__":
    solution = solve()
    print(f"Day 5, Part 2: {solution}")
