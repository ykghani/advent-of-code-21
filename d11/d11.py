'''Advent of Code 2021 Day 11 - Dumbo Octopus'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd11.txt'

STEPS = 1000
grid = []
with open(file_path, 'r') as f: 
    for line in f:
        grid.append([int(n) for n in line.strip()])

def print_grid(grid):
    for row in grid:
        print(row)
    print('\n')
    return


num_rows, num_cols = len(grid), len(grid[0])
def get_neighbors(i: int, j: int) -> list:
    
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
    neighbors = []
    for di, dj in directions:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < num_rows and 0 <= new_j < num_cols:
            neighbors.append((new_i, new_j))
    
    return neighbors

def update_grid() -> int: 
    '''Updates the energy levels of all octopi and returns the number of flashes'''
    flashes = 0
    flashed = set()
    for i in range(num_rows):
        for j in range(num_cols):
            grid[i][j] += 1
    
    while True: 
        new_flashes = False
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] > 9 and (i, j) not in flashed:
                    flashes += 1
                    flashed.add((i, j))
                    new_flashes = True
                    for neigh in get_neighbors(i, j):
                        grid[neigh[0]][neigh[1]] += 1
        if not new_flashes:
            break
        
    for octopus in flashed:
        grid[octopus[0]][octopus[1]] = 0

    return flashes    

def check_sync() -> bool:
    return all(grid[i][j] == 0 for i in range(num_rows) for j in range(num_cols))

num_flashes = 0
part_two = True
print(f"INITIAL GRID:")
print_grid(grid)
for step in range(STEPS):
    num_flashes += update_grid()
    if part_two:
        if check_sync():
            print(f'Part two: {step + 1}')
            break 

print(f"Part one: {num_flashes}")