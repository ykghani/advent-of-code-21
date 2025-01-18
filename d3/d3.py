'''Advent of Code 2021 - Day 1'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd3.txt'

BIT_LEN = 12

vals = [[] for _ in range(BIT_LEN)]
oxy, co2 = [], []

with open(file_path, 'r') as f:
    for line in f: 
        line = line.strip() 
        oxy.append(line)
        co2.append(line)
        for idx, char in enumerate(line):
            vals[idx].append(char)
gamma, epsilon = [], []

part_two = True 

def bit_criteria(bits: list, idx: int, oxy_gen=True) -> list:
    if len(bits) == 1: 
        return bits
    
    ones = sum(1 for bit in bits if bit[idx] == '1')
    zeros = len(bits) - ones
    
    if oxy_gen:
        keep_bit = '1' if ones >= zeros else '0'
    else:
        keep_bit = '0' if zeros <= ones else '1'
    
    return [bit for bit in bits if bit[idx] == keep_bit]
            
            
# for bit in vals: 
for idx, bit in enumerate(vals):
    ones = bit.count('1')
    zeros = bit.count('0')
    
    if ones > zeros:
        gamma.append('1')
        epsilon.append('0')
    else:
        epsilon.append('1')
        gamma.append('0')
        
oxy_list = oxy.copy()
co2_list = co2.copy()

for idx in range(BIT_LEN):
    if len(oxy_list) > 1:
        oxy_list = bit_criteria(oxy_list, idx, True)
    if len(co2_list) > 1:
        co2_list = bit_criteria(co2_list, idx, False)


print(f"Part one: {int(''.join(gamma), 2) * int(''.join(epsilon), 2)}")
print(f"Part two: {int(oxy_list[0], 2) * int(co2_list[0], 2)}")