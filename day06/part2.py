#!/usr/bin/env python3.9

import sys

def main():
    groups = []
    current_group = set('abcdefghijklmnopqrstuvwxyz')

    for line in sys.stdin:
        line = line[:-1]
        if line == '':
            groups.append(current_group)
            current_group = set('abcdefghijklmnopqrstuvwxyz')
            continue

        current_group = current_group.intersection(line)

    print(sum([len(x) for x in groups]))


if __name__ == "__main__":
    main()
