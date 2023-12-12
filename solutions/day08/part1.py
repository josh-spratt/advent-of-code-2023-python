from typing import List, Union
from pprint import pprint
import itertools

POSITION_MAP = {"L": 1, "R": 2}


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


def solve(file_path: str = "inputs/day08.txt") -> int:
    reader = InputFileReader(file_path)
    lines = [line for line in reader.read_lines() if line]

    left_right_instructions = [*lines[0]]
    network = [
        line.replace(" = (", " ").replace(")", "").replace(",", "").split(" ")
        for line in lines[1:]
    ]

    # Starting at point (0, 0), select L (1) or R (2) for that line.
    position = (0, 0)
    for instruction in itertools.cycle(left_right_instructions):
        print(f"Instruction: {instruction}")
        mapping = POSITION_MAP[instruction]
        print(f"Instruction Mapping: {mapping}")
        next_value = network[position[0]][mapping]
        print(f"Next Value: {next_value}")
        for val in itertools.cycle(range(position[0], len(network))):
            print(val)
            print(next_value)
            if network[val][0] == next_value and network[val][0] == "ZZZ":
                print(f"Found ZZZ match.")
                print(f"Exiting loop")
                break
            elif network[val][0] == next_value:
                print(f"Value in Col 1 Matches Previous Value: {network[val][0]}")
                next_value = network[position[0]][mapping]
                position = (val, 0)
                break

    # Whatever the value of L or R point is, search (x, 0) for next occurrence of that value.


if __name__ == "__main__":
    solution = solve()
    print(f"Day 8, Part 1: {solution}")
