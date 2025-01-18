'''Advent of Code 2021 - Day 5'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd5.txt'

class Line:
    def __init__(self, line):
        self.points = []
        
        start, end = line.strip().split(' -> ')
        coords1, coords2 = start.split(','), end.split(',')
        x1, y1 = int(coords1[0].strip()), int(coords1[1].strip())
        x2, y2 = int(coords2[0].strip()), int(coords2[1].strip())
        self.points.extend([(x1, y1), (x2, y2)])
        
        try:
            self.slope = (y2 - y1) / (x2 - x1)
        except ZeroDivisionError:
            self.slope = None
        
        self.is_horizontal = y1 == y2
        self.is_vertical = x1 == x2
        
        try: 
            self.is_diagonal = abs(self.slope) == 1
        except TypeError: 
            self.is_diagonal = False

        if self.is_horizontal:
            if x1 < x2:
                self.points.extend([(x, y1) for x in range(x1 + 1, x2)])
            else:
                self.points.extend([(x, y2) for x in range(x2 + 1, x1)])
        elif self.is_vertical:
            if y1 < y2:
                self.points.extend([(x1, y) for y in range(y1 + 1, y2)])
            else:
                self.points.extend([(x1, y) for y in range(y2 + 1, y1)])
        elif self.is_diagonal:
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            steps = abs(x2 - x1)
            self.points.extend([(x1 + i*dx, y1 + i*dy) for i in range(1, steps)])

grid = {}
with open(file_path, 'r') as f:
    for line_str in f: 
        line = Line(line_str)
        
        if line.is_vertical or line.is_horizontal or line.is_diagonal:
            for point in line.points:
                grid[point] = grid.get(point, 0) + 1

print(f"Part one: {sum([1 for point in grid if grid[point] >= 2])}")