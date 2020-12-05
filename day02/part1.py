#!/usr/bin/env python3.9

import sys
import collections

def main():
    Line = collections.namedtuple('line', ['lower_bound', 'upper_bound', 'letter', 'password'])
    lines = []
    for line in sys.stdin:
        bounds, letter, password = line.split()
        lower_bound, upper_bound = [int(x) for x in bounds.split('-')]
        letter = letter.split(':')[0]
        line = Line(lower_bound, upper_bound, letter, password)
        lines.append(line)

    passwords_allowed = 0
    for line in lines:
        matching_count = 0
        for char in line.password:
            if char == line.letter:
                matching_count += 1
        
        if matching_count >= line.lower_bound and matching_count <= line.upper_bound:
            passwords_allowed += 1
    
    print(passwords_allowed)

if __name__ == "__main__":
    main()
