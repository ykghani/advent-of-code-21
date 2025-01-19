'''Advent of Code 2021 Day 10: Syntax Scoring'''
from pathlib import Path
from functools import reduce 
from statistics import median

script_dir = Path(__file__).parent
file_path = script_dir / 'd10.txt'

syntax_scores = {
    ')': [3, 0], 
    ']': [57, 0],
    '}': [1197, 0],
    '>': [25137, 0]
}

def process_line(line, part_two = False):
    
    opening_chars = [line[0]]
    closing_chars = []
    
    complement = {
        '[': ']',
        '(': ')',
        '<': '>',
        '{': '}'
    }
    
    for char in line[1:]: 
        if char in ['(', '[', '{', '<']:
            opening_chars.append(char)
        elif char == complement.get(opening_chars[-1]):
            opening_chars.pop()
        else:
            syntax_scores[char][1] += 1
            return
    
    if part_two:
        for char in opening_chars[::-1]:
            closing_chars.append(complement[char])
        
        completion_scores.append(score_completion_string(closing_chars))
    
    

def score_completion_string(inp: str) -> int: 
    '''Returns the value of the completion string based on given puzzle rules'''
    score = 0
    char_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4 
    }
    
    for char in inp: 
        score *= 5
        score += char_points[char]
    
    return score

completion_scores = []
with open(file_path, 'r' ) as f:
    for line in f:
        process_line(line.strip(), True)

part_one = sum([reduce(lambda x, y: x * y, char) for char in syntax_scores.values()])
part_two = median(completion_scores)
print(f"Part one: {part_one}")
print(f"Part two: {part_two}")