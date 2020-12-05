#!/usr/bin/env python3.9

import sys
import collections

def main():
    Line = collections.namedtuple('line', ['index1', 'index2', 'letter', 'password'])
    lines = []
    for line in sys.stdin:
        indicies, letter, password = line.split()
        index1, index2 = [int(x) for x in indicies.split('-')]
        letter = letter.split(':')[0]
        line = Line(index1, index2, letter, password)
        lines.append(line)

    passwords_allowed = 0
    for line in lines:
        index1Correct = line.password[line.index1-1] == line.letter
        index2Correct = line.password[line.index2-1] == line.letter

        if index1Correct ^ index2Correct:
            passwords_allowed += 1

    print(passwords_allowed)

if __name__ == "__main__":
    main()
