'''Advent of Code 2021 Day 16: Packet Decoder'''
from pathlib import Path

script_dir = Path(__file__).parent
file_path = script_dir / 'd16.txt'

def hex_to_binary(hex_string):
    """Converts a hexadecimal string to binary."""
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)

print(hex_to_binary('D2FE28'))