'''Advent of Code 2021 - Day 6'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd6.txt'

NUM_DAYS = 256
with open(file_path, 'r') as f: 
    lanterns = [int(i) for i in f.readline().split(',')]
    
# lanterns = [3,4,3,1,2]
current_lanterns = {key: lanterns.count(key) for key in range(0, 7)}
new_lanterns = {key: 0 for key in range(0, 9)}

def update_lanterns(current_fish, new_fish) -> dict: 
    spawning_fish = current_fish[0] + new_fish[0]
    
    for i in range(0, 6):
        current_fish[i] = current_fish[i + 1]
    
    current_fish[6] = spawning_fish
    
    for j in range(0, 8):
        new_fish[j] = new_fish[j + 1]
    
    # Add new fish
    new_fish[8] = spawning_fish

    return current_fish, new_fish

for day in range(NUM_DAYS):
    current_lanterns, new_lanterns = update_lanterns(current_lanterns, new_lanterns)
    
print(f"Soln: {sum(current_lanterns.values()) + sum(new_lanterns.values())}")