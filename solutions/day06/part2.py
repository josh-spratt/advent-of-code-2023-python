from typing import List


class InputFileReader:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        with open(self.file_path, "r") as file:
            lines = [line.strip() for line in file]
        return lines


class BoatRace:
    def __init__(
        self, race_length: int, record_distance: int, race_number: int
    ) -> None:
        self.race_length = race_length
        self.record_distance = record_distance
        self.race_number = race_number

    def calculate_distance(self, hold_time: int) -> int:
        moving_time = self.race_length - hold_time
        boat_velocity = hold_time
        distance = boat_velocity * moving_time
        return distance


def solve(file_path: str = "inputs/day06.txt") -> int:
    reader = InputFileReader(file_path)
    lines = reader.read_lines()
    time = int(lines[0].replace("Time:", "").strip().replace(" ", ""))
    distance = int(lines[1].replace("Distance:", "").strip().replace(" ", ""))

    ways_to_win = []

    race = {"race_number": 0, "time": time, "distance": distance}
    race = BoatRace(race["time"], race["distance"], race["race_number"])
    for i in range(1, race.race_length + 1):
        if race.calculate_distance(i) > race.record_distance:
            ways_to_win.append(i)
    return len(ways_to_win)


if __name__ == "__main__":
    solution = solve()
    print(f"Day 6, Part 2: {solution}")
