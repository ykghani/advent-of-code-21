'''Advent of Code 2021 day 4'''
'''Advent of Code 2021 - Day 1'''
from pathlib import Path
import numpy as np

script_dir = Path(__file__).parent
file_path = script_dir / 'd4.txt'

class Board: 
    def __init__(self, numbers):
        self.board = np.array(numbers).reshape(5, 5)
        self.marked = np.zeros((5, 5), dtype= bool) 
        self.unmarked = [val for row in numbers for val in row]
        self.has_won = False
    
    def mark_number(self, num):
        positions = np.where(self.board == num)
        if len(positions[0]) > 0: 
            for row, col in zip(positions[0], positions[1]):
                self.marked[row, col] = True
                if num in self.unmarked:
                    self.unmarked.remove(num)
            return self.check_win()
        return False 
    
    def check_win(self):
        self.has_won = any(all(row) for row in self.marked) or any(all(col) for col in self.marked.T)
        return self.has_won
    
    @property
    def score(self):
        return sum(self.unmarked)
    

with open(file_path, 'r') as f:
    numbas = [int(x) for x in f.readline().strip().split(',')]
    
    boards = []
    current_board = []
    
    f.readline()
    
    for line in f: 
        if line.strip() == '':
            if current_board:
                boards.append(Board(current_board))
            current_board = []
            continue
        else:        
            row = [int(num) for num in line.strip().split()]
            current_board.append(row)
    
    if current_board:
        boards.append(Board(current_board))

last_winning_score = None
winning_number = None
boards_remaining = len(boards)    

for numba in numbas: 
    for board in boards: 
        if not board.has_won and board.mark_number(numba):
            boards_remaining -= 1
            last_winning_score = board.score
            winning_number = numba

            if boards_remaining == 0:
                print(f"Last winning board score: {last_winning_score}")
                print(f"Last winning number: {winning_number}")
                print(f"Final score: {last_winning_score * winning_number}")
                exit()