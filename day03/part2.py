#!/usr/bin/env python3.9

import sys

def tree_count(map, down_step: int, right_step: int) -> int:
    line_width = len(map[0])
    result = 0
    x = 0
    y = 0
    while y < len(map):
        if map[y][x % line_width] == '#':
            result += 1
        x += right_step
        y += down_step

    return result

def main():
    map = [line[:-1] for line in sys.stdin]
    slopes = [[1,1], [3, 1], [5, 1], [7, 1], [1, 2]]
    result = 1
    for slope in slopes:
        result *= tree_count(map, slope[1], slope[0])
    print(result)

if __name__ == "__main__":
    main()
