import importlib
import os
import sys

# Load virtual environment created by Poetry
os.environ["POETRY_ACTIVE"] = "1"
sys.path.append(os.path.join(os.path.dirname(__file__), ".venv", "lib", "site-packages"))


def run_day(day: int):
    try:
        # Import the part1 and part2 modules dynamically
        module_part1 = importlib.import_module(f"solutions.day{day}.part1")
        module_part2 = importlib.import_module(f"solutions.day{day}.part2")

        # Call the solve function from each module
        print(f"Day {day}, Part 1: {module_part1.solve()}")
        print(f"Day {day}, Part 2: {module_part2.solve()}")

    except ImportError:
        print(f"No solutions found for Day {day}.")


if __name__ == "__main__":
    day_to_run = input("Enter the day (e.g., 01): ")
    run_day(day_to_run.zfill(2))
