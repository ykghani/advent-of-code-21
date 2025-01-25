'''Advent of Code 2021 Day 12 - Passage Pathing'''
from pathlib import Path
from collections import defaultdict

script_dir = Path(__file__).parent
file_path = script_dir / 'd12_text.txt'

nodes = set()
edges = defaultdict(list)
with open(file_path, 'r') as f: 
    for line in f: 
        a, b = line.strip().split('-')
        edges[a].append(b)
        edges[b].append(a)
    
def small_cave_visited(path) -> bool:
    return any(node.islower() for node in path)

def find_all_paths(start, end, graph, criteria_fn= None):
    def dfs(cur, path, all_paths, visited):
        visited.add(cur)
        path.append(cur)
        
        if cur == end:
            if criteria_fn is None or criteria_fn(path):
                all_paths.append(path[:])
        else:
            for neighbor in graph[cur]:
                if neighbor not in visited and (criteria_fn is None or criteria_fn(path)):
                        dfs(neighbor, path, all_paths, visited)

        path.pop()
        visited.remove(cur)
    all_paths = []
    dfs('start', [], all_paths, set())
    return all_paths

paths = find_all_paths('start', 'end',edges, small_cave_visited)
for path in paths: 
    print(path)

print(f"Part one: {len(paths)}")
        
