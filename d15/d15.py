'''Advent of Code Day 2021 Day 15 - Chiton'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd15.txt'

grid = []
with open(file_path, 'r') as f: 
    for line in f: 
        grid.append([int(i) for i in line.strip()])


