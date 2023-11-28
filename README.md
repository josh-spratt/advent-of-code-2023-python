# Advent of Code 2023 - Python

This repository contains my solutions for Advent of Code 2023 in Python. I've chosen to organize each day's challenge into its own runnable package.

## Project Structure

```
  ├── inputs/               Store input data for each day in separate text files (e.g., day01.txt, day02.txt, etc.).
  ├── solutions/            Packages for each day's solution with part1.py and part2.py files.
  │   ├── day01/
  │   │   ├── __init__.py
  │   │   ├── part1.py
  │   │   └── part2.py
  │   ├── day02/
  │   │   ├── __init__.py
  │   │   ├── part1.py
  │   │   └── part2.py
  │   └── ...
  └── run.py                 Script to run solutions for specific days.
```

## Prerequisites

- [Python](https://www.python.org/) installed.
- [Poetry](https://python-poetry.org/) for dependency management (optional but recommended).

## Installation

1. Clone the repository:
```bash
git clone git@github.com:josh-spratt/advent-of-code-2023-python.git
cd advent-of-code-2023-python
```
2. (Optional) Install project dependencies using poetry:
```bash
poetry install
```

## Usage

To run a specific day's solution, run this:
```bash
python run.py <day>
```
Example:
```bash
python run.py 01
```
This will execute the solutions for day 1, part 1 and part 2.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
