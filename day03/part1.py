#!/usr/bin/env python3.9

import sys

def main():
    lines = [line[:-1] for line in sys.stdin]
    line_width = len(lines[0])
    tree_count = 0
    x = 0
    for line in lines:
        if line[x % line_width] == '#':
            tree_count += 1
        x += 3

    print(tree_count)

if __name__ == "__main__":
    main()
