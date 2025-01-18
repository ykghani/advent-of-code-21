'''Advent of Code 2021 - Day 1'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd2.txt'

hor, vert, aim = 0, 0, 0
part_one_flag = False
with open(file_path, 'r') as f:
    for line in f: 
        line = line.strip().split()
        if part_one_flag: 
            if line[0] == 'up':
                vert -= int(line[1])
            elif line[0] == 'down':
                vert += int(line[1])
            else:
                hor += int(line[1])
        else:
            if line[0] == 'up':
                aim -= int(line[1])
            elif line[0] == 'down':
                aim += int(line[1])
            else:
                hor += int(line[1])
                vert += int(line[1]) * aim
            
print(f"Soln: {hor * vert}")