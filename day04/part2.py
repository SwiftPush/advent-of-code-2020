#!/usr/bin/env python3.9

import sys

def is_valid_byr(input) -> bool:
    return int(input) >= 1920 and int(input) <= 2002

def is_valid_iyr(input) -> bool:
    return int(input) >= 2010 and int(input) <= 2020

def is_valid_eyr(input) -> bool:
    return int(input) >= 2020 and int(input) <= 2030

def is_valid_hgt(input) -> bool:
    num = int(''.join(c for c in input if c.isdigit()))
    unit = ''.join(c for c in input if not c.isdigit())
    if unit == 'cm':
        return num >= 150 and num <= 193
    elif unit == 'in':
        return num >= 59 and num <= 76
    return False

def is_valid_hcl(input) -> bool:
    if len(input) != 7:
        return False
    
    if input[0] != '#':
        return False
    
    valid_chars = [x for x in input[1:] if x in '0123456789abcdef']
    return len(valid_chars) == 6

def is_valid_ecl(input) -> bool:
    return input in ['amb','blu','brn','gry','grn','hzl','oth']

def is_valid_pid(input) -> bool:
    if len(input) != 9:
        return False
    
    valid_chars = [x for x in input if x in '0123456789']
    return len(valid_chars) == 9

def is_passport_valid(passport) -> bool:
    validators = {
        'byr': is_valid_byr,
        'iyr': is_valid_iyr,
        'eyr': is_valid_eyr,
        'hgt': is_valid_hgt,
        'hcl': is_valid_hcl,
        'ecl': is_valid_ecl,
        'pid': is_valid_pid,
    }
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # missing cid
    for field in required_fields:
        if field not in passport:
            return False
        
        value = passport[field]
        if not validators[field](value):
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
