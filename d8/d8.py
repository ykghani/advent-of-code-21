'''Advent of Code 2021 Day 8'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd8.txt'

def create_decoder(signal):
    sigs = [set(sig) for sig in signal.split()]
    signals_by_length = {}
    for sig in sigs:
        signals_by_length.setdefault(len(sig), []).append(sig)
    
    decoder = {
        1: signals_by_length[2][0],
        4: signals_by_length[4][0],
        7: signals_by_length[3][0],
        8: signals_by_length[7][0]
    }
    
    top_bar = decoder[7] - decoder[1]
    sixers = signals_by_length[6]
    for six_char in sixers[:]:
        if len(six_char - (top_bar | decoder[4])) == 1:
            bottom_bar = six_char - (top_bar | decoder[4])
            decoder[9] = six_char
            sixers.remove(six_char)
            break 
    
    
    bottom_left = decoder[8] - decoder[9]
    for six_char in sixers[:]:
        if decoder[1] < six_char: 
            decoder[0] = six_char
            mid_bar = decoder[8] - six_char
            sixers.remove(six_char)
            break
    
    decoder[6] = sixers[0]
    
    top_right = decoder[8] - decoder[6]
    bottom_right = decoder[1] - top_right
    top_left = decoder[8] - top_bar - mid_bar - bottom_bar - bottom_left - decoder[1]
    
    decoder[3] = decoder[1] | top_bar | mid_bar | bottom_bar
    decoder[5] = decoder[8] - top_right - bottom_left
    decoder[2] = decoder[8] - top_left - bottom_right
    
    return decoder


def decode(signal, output):
    
    digits = []
    segment_counts = create_decoder(signal)
    
    outs = [set(out) for out in output.split()]
    for out in outs:
        for key, val in segment_counts.items(): 
            if out == val: 
                digits.append(key)
    
    return int(''.join(map(str,digits)))

def solve(file):
    digits = 0
    part_two = 0
    with open(file_path, 'r') as f:
        for line in f: 
            signal, output = line.strip().split('|')
            
            part_two += decode(signal, output)
                    
            for val in output.split():
                if len(set(list(val))) in {2, 3, 4, 7}:
                    digits += 1
    
    return digits, part_two

print(solve(file_path))