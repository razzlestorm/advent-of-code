from typing import Dict, List
import re

with open('input.txt') as f:
    input_list = f.read().split('\n\n')
    entries = [entry.replace("\n", " ").split(" ") for entry in input_list]
    del entries[-1][-1]
#res = dict(map(lambda l:l.split(":"), x))
# example of 2/4 valid passports in batch file (can be missing cid):
'''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''
# Pre-parsed entry looks like:
# 'pid:782547454 hcl:z ecl:#b0805f iyr:2013 eyr:2023 hgt:159cm byr:1935 cid:230'
def create_dictlist(input: List[str]) -> List[dict]:
    entry_dict = [dict(map(lambda e:e.split(":"), entry)) for entry in input]
    return entry_dict

def validate_fields(input: Dict) -> bool:
    standard = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    return set(input.keys()) == set(standard[:-1]) or set(input.keys()) == set(standard)


def validate_values(input: Dict) -> bool:

    try:
        height = re.compile("^\d{2,3}cm|\d{2,3}in$", re.I)
        hgt = height.match(input['hgt'])[0][:-2]
    except TypeError:
        return False

    hair = re.compile("^#[\w\d]{6}$", re.I)
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    conditions = [(1920 <= int(input['byr']) <= 2002),
                  (2010 <= int(input['iyr']) <= 2020),
                  (2020 <= int(input['eyr']) <= 2030),
                  ((150 <= int(hgt) <= 193) or (59 <= int(hgt) <= 76)),
                  (hair.match(input['hcl'])),
                  (input['ecl'] in eye_colors),
                  (len(input['pid']) == 9),]
    return all(conditions)

passports = create_dictlist(entries)
valid_passports = [p for p in passports if validate_fields(p)]

print('passports: ', len(passports))
print('valid passports: ', len(valid_passports))

# solutions
print(sum([validate_fields(entry) for entry in passports]))
print(sum([validate_values(entry) for entry in valid_passports]))
