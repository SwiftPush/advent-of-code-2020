#!/usr/bin/env python3.9

import sys

def main():
    nums = []
    for line in sys.stdin:
        nums.append(int(line))
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)-1):
            if nums[i] + nums[j] == 2020:
                print(nums[i]*nums[j])
                return

    print("no match found")

if __name__ == "__main__":
    main()
