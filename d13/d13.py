'''Advent of Code 2021 Day 13 - Transparent Origami'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd13.txt'

points = []
folds = []

with open(file_path, 'r') as f:
    for line in f: 
        if ',' in line:
            x, y = line.strip().split(',')
            points.append((int(x), int(y)))
        
        if 'fold' in line:
            params = line.strip().split()
            folds.append(params[2])

x_dim, y_dim = max([p[0] for p in points]), max([p[1] for p in points])

grid = [[0 for _ in range(x_dim + 1)] for _ in range(y_dim + 1)]
for p in points:
    x, y = p[0], p[1]
    grid[y][x] = 1

def fold(grid: list, fold: str) -> list:
    '''Returns a new grid that has been folded based on the input string'''
    dir, fold_line = fold.split('=')
    fold_line = int(fold_line)
    
    if dir == 'x': #Right side of grid is folded to the left
        x_dim, y_dim = fold_line, len(grid)
        out = [[0 for _ in range(x_dim)] for _ in range(y_dim)]
        
        for y in range(y_dim):
            for x in range(fold_line):
                out[y][x] = grid[y][x]
        
        for y in range(y_dim):
            for x in range(fold_line + 1, len(grid[0])):
                if grid[y][x] == 1: 
                    dist = x - fold_line
                    new_x = fold_line - dist
                    out[y][new_x] = 1
    else:
        x_dim, y_dim = len(grid[0]), fold_line
        out = [[0 for _ in range(x_dim)] for _ in range(y_dim)]
        
        for y in range(fold_line):
            for x in range(x_dim): 
                out[y][x] = grid[y][x]
        
        for y in range(fold_line + 1, len(grid)):
            for x in range(x_dim):
                if grid[y][x] == 1: 
                    dist = y - fold_line
                    new_y = fold_line - dist
                    out[new_y][x] = 1
    
    return out 

def visible_points(grid) -> int: 
    '''Returns the integer score of a grid'''
    score = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            score += grid[y][x]
    return score

def visualize_grid(grid):
    return '\n'.join(''.join('#' if cell == 1 else '.' for cell in row) for row in grid)

folded_grid = grid.copy()
for f in folds: 
    folded_grid = fold(folded_grid, f)
    print(visible_points(folded_grid))

print(visualize_grid(folded_grid))