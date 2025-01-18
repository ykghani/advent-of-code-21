'''Advent of Code 2021 - Day 7: The Treachery of Whales'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd7.txt'

def part_two_fuel(x_coord, pos) -> int: 
    return sum(range(1, abs(pos - x_coord) + 1))

with open(file_path, 'r') as f: 
    crabs = [int(i) for i in f.readline().split(',')]

unique_positions = set(crabs)
min_fuel = 10_000_000_000_000_000_000
part_two = True
for pos in range(0, max(crabs)+ 1):
    if part_two:
        fuel = sum([part_two_fuel(x, pos) for x in crabs]) 
    else:
        fuel = sum([abs(x - pos) for x in crabs])
    
    if fuel < min_fuel:
        min_fuel = fuel

print(f"Soln: {min_fuel}")