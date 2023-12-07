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
    times = [int(x) for x in lines[0].replace("Time: ", "").strip().split("     ")]
    distances = [int(x) for x in lines[1].replace("Distance:", "").strip().split("   ")]
    races = []
    for i in range(0, len(times)):
        race = {"race_number": i, "time": times[i], "distance": distances[i]}
        races.append(race)

    all_ways_to_win = []
    for race in races:
        ways_to_win = []
        race = BoatRace(race["time"], race["distance"], race["race_number"])
        for i in range(1, race.race_length + 1):
            if race.calculate_distance(i) > race.record_distance:
                ways_to_win.append(i)
        all_ways_to_win.append(ways_to_win)

    vals = [len(i) for i in all_ways_to_win]
    sum = 1
    for i in vals:
        sum *= i
    return sum


if __name__ == "__main__":
    solution = solve()
    print(f"Day 6, Part 1: {solution}")
