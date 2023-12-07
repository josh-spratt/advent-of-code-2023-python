from typing import List


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


def solve(file_path: str = "inputs/day04.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    lines = [line.split(":") for line in lines]
    counts = []
    for line in lines:
        card_split = line[1].split("|")
        winning_numbers = card_split[0].strip().split(" ")
        winning_numbers = [i for i in winning_numbers if i]
        actual_numbers = card_split[1].strip().split(" ")
        actual_numbers = [i for i in actual_numbers if i]
        results = {}
        for i in winning_numbers:
            results[i] = actual_numbers.count(i)
        starting_count = 0
        if sum(results.values()) > 0:
            starting_count += 1
            for i in range(1, sum(results.values())):
                starting_count *= 2
            counts.append(starting_count)
    return sum(counts)


if __name__ == "__main__":
    solution = solve()
    print(f"Day 4, Part 1: {solution}")
