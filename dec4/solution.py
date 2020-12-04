from typing import Dict, List
import re


FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
REQUIRED_FIELDS = FIELDS - {'cid'}

# Pre-parsed entry looks like:
# 'pid:782547454 hcl:z ecl:#b0805f iyr:2013 eyr:2023 hgt:159cm byr:1935 cid:230'
def create_dictlist(input: List[str]) -> List[dict]:
    entry_dict = [dict(map(lambda e:e.split(":"), entry)) for entry in input]
    return entry_dict

# Previously compared sets with ==, but that seems more brittle.
def validate_fields(passport: Dict) -> bool:
    return all(field in passport for field in REQUIRED_FIELDS)

def validate_values(passport: Dict) -> bool:
    try:
        height = re.compile("^\d{2,3}cm|\d{2,3}in$", re.I)
        hgt = height.match(passport['hgt'])[0]
    except TypeError:
        return False
    hair = re.compile(r"^#[\da-f]{6}$", re.I)
    pid = re.compile(r"^\d{9}$")
    eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    conditions = [(1920 <= int(passport['byr']) <= 2002),
                  (2010 <= int(passport['iyr']) <= 2020),
                  (2020 <= int(passport['eyr']) <= 2030),
                  (validate_height(hgt)),
                  (hair.match(passport['hcl'])),
                  (passport['ecl'] in eye_colors),
                  (pid.match(passport['pid']))]
    return all(conditions)

def validate_height(height):
    if height.endswith('in'):
        return 59 <= int(height[:-2]) <= 76
    return 150 <= int(height[:-2]) <= 193


with open('input.txt') as f:
    input_list = f.read().split('\n\n')
    entries = [entry.replace("\n", " ").split(" ") for entry in input_list]
    del entries[-1][-1]

passports = create_dictlist(entries)
valid_passports = [p for p in passports if validate_fields(p)]

print('passports: ', len(passports))
print('valid passports: ', len(valid_passports))

# Solutions
print(sum([validate_fields(entry) for entry in passports]))
print(sum([validate_values(entry) for entry in valid_passports]))
