#!/usr/bin/env python3.9

import sys

def main():
    nums = []
    for line in sys.stdin:
        nums.append(int(line))
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)-1):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(nums[i]*nums[j]*nums[k])
                    return

    print("no match found")

if __name__ == "__main__":
    main()
