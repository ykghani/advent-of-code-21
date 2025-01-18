'''Advent of Code 2021 Day 9: Smoke Basin'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd9.txt'

grid = [] 
with open(file_path, 'r') as f: 
    for line in f:
        grid.append([int(n) for n in line.strip()])

num_rows, num_cols = len(grid), len(grid[0])

def get_neighbors(i: int, j: int) -> list:
    
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    neighbors = []
    for di, dj in directions:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < num_rows and 0 <= new_j < num_cols:
            neighbors.append((new_i, new_j))
    
    return neighbors

def get_neighbor_values(neighbors):        
    return [grid[n[0]][n[1]] for n in neighbors]

risk_level = 0
low_points = []
for i in range(num_rows):
    for j in range(num_cols):
        if grid[i][j] < min(get_neighbor_values(get_neighbors(i, j))):
            risk_level += grid[i][j] + 1
            low_points.append((i, j))
print(f"Part one: {risk_level}")

def find_basin(basin, grid, seen= set()) -> int: 
    '''Returns an int for the size of a basin starting from the lowest point'''
    size = 1
    seen.add(basin)
    
    neighbors = [neigh for neigh in get_neighbors(basin[0], basin[1]) if neigh not in seen]
    for neigh in neighbors:
        i, j = neigh[0], neigh[1]
        if grid[i][j] == 9 or (i, j) in seen:
            continue
        else:
            seen.add((i, j))
            size += find_basin((i, j), grid, seen)
    return size

basin_sizes = []
for point in low_points: 
    basin_sizes.append(find_basin(point, grid))

basin_sizes.sort(reverse= True)
print(f"Part two: {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}")