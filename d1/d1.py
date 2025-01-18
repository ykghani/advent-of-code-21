'''Advent of Code 2021 - Day 1'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd1.txt'

vals = []
with open(file_path, 'r') as f:
    for line in f:
        vals.append(int(line.strip()))
        
part_one = sum(map(lambda x, y: x < y, vals, vals[1:]))
print(f"Part one: {part_one}")

windows = [sum(x) for x in zip(vals, vals[1:], vals[2:])]
part_two = sum(1 for a, b in zip(windows, windows[1:]) if a < b)
print(f"Part two: {part_two}")