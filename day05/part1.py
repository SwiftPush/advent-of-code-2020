#!/usr/bin/env python3.9

import sys

def decode(boarding_pass):
    part_1 = boarding_pass[:7]
    part_2 = boarding_pass[7:10]

    part_1 = ''.join([str(1 if x == 'B' else 0) for x in part_1])
    part_2 = ''.join([str(1 if x == 'R' else 0) for x in part_2])

    row = int(part_1, 2)
    col = int(part_2, 2)

    return row * 8 + col

def main():
    lines = [line.split()[0] for line in sys.stdin]
    results = [decode(x) for x in lines]
    print(max(results))


if __name__ == "__main__":
    main()
