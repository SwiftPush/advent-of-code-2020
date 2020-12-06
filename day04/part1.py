#!/usr/bin/env python3.9

import sys

def is_passport_valid(passport) -> bool:
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # missing cid
    for required_field in required_fields:
        if required_field not in passport:
            return False
    
    return True

def main():
    passports = []
    
    current_passport = {}
    for line in sys.stdin:
        fields = line.split()

        if len(fields) == 0:
            passports.append(current_passport)
            current_passport = {}
        
        for field in fields:
            key, value = field.split(':')
            current_passport[key] = value

    number_passports_valid = 0
    for passport in passports:
        if is_passport_valid(passport):
            number_passports_valid +=1
    
    print(number_passports_valid)

if __name__ == "__main__":
    main()
