'''Advent of Code Day 2021 Day 14 - Extended Polymerization'''
from pathlib import Path
from collections import Counter

script_dir = Path(__file__).parent
file_path = script_dir / 'd14.txt'

STEPS = 10

templates = {}
with open(file_path, 'r') as f: 
    
    mol = list(f.readline().strip())
    for line in f:
        if line.strip():
            k, v = line.strip().split('->')
            templates[k.strip()] = v.strip()

test_replacements = {
    'CH': 'B',
    'HH': 'N',
    'CB': 'H',
    'NH': 'C',
    'HB': 'C',
    'HC': 'B',
    'HN': 'C',
    'NN': 'C',
    'BH': 'H',
    'NC': 'B',
    'NB': 'B',
    'BN': 'B',
    'BB': 'N',
    'BC': 'B',
    'CC': 'N',
    'CN': 'C'
}
# print(mol)
# print(templates)



def run_insertions(mol: list, replacements= templates) -> list: 
    '''Returns updated molecule after all insertions have been done''' 
    mol = list(mol)
    i = 0
    while i < len(mol) - 1:
        k = ''.join(mol[i: i + 2])
        if k in replacements: 
            mol.insert(i + 1, replacements[k])
            i += 2
        else: 
            i += 1 
    return mol

def part_two(mol: list, replacements= templates, steps= STEPS) -> int:
    '''Optimized logic for part 2'''
    pair_counts = Counter()
    for i in range(len(mol) - 1): 
        k = mol[i] + mol[i + 1]
        pair_counts[k] += 1
    
    letter_counts= Counter(mol)
    for _ in range(steps):
        new_pairs = Counter()
        
        for pair, count in pair_counts.items():
            if pair in replacements:
                insert = replacements[pair]
                pair1 = pair[0] + insert
                pair2 = insert + pair[1]
                new_pairs[pair1] += count
                new_pairs[pair2] += count
                letter_counts[insert] += count
        
        pair_counts = new_pairs
    
    return max(letter_counts.values()) - min(letter_counts.values())

def update_counts(mol: list, counts: dict) -> None: 
    '''Updates the seen counts based on the latest mol'''
    for k in counts.keys():
        counts[k] += mol.count(k)
    return

def evaluate_mol(mol) -> int: 
    '''Scores molecules based on most and least common value'''
    counts = {k: mol.count(k) for k in set(mol)}
    # print(counts)
    return max([v for v in counts.values()]) - min([v for v in counts.values()])

mol_counts = {k: mol.count(k) for k in set(mol)}
debug = False
part_two_mol = mol.copy()

if debug:
    mol = 'NNCB' 
    print(f"INTIAL MOL: {mol}")
    

for _ in range(STEPS):
    if debug: 
        mol = run_insertions(mol, test_replacements)
        print(f"STEP: {_} MOLECULE: {''.join(mol)}")
        print(len(mol))
    else:
        mol = run_insertions(mol)
    # update_counts(mol, mol_counts)

print(evaluate_mol(mol))

print(f"Part one: {evaluate_mol(mol)}")
print(f"Part two: {part_two(part_two_mol, templates, 40)}")