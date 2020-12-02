from collections import namedtuple
from typing import List


'''
To try to debug the problem, they have created a list (your puzzle input)
 of passwords (according to the corrupted database) and
 the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times
 a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time
 and at most 3 times.

In the above example, 2 passwords are valid.
The middle password, cdefg, is not; it contains no instances of b,
but needs at least 1. The first and third passwords are valid:
 they contain one a or nine c,
 both within the limits of their respective policies.
'''

with open('input.txt') as f:
    input_list = [line.strip() for line in f]

# example group in input_list: ['3-8 t', ' wttlmpdkfkf']

Validator = namedtuple('Validator', ['min_num', 'max_num', 'let'])

class Password_Validator:
    def __init__(self, policy: List[str]):
        policy = policy.split(" ")
        self.policy = Validator(int(policy[0].split("-")[0]),
                                int(policy[0].split("-")[1]),
                                policy[1].strip(":"))
        self.password = policy[2].strip()


    def validate(self):
        if self.policy.min_num <= self.password.count(self.policy.let) <= self.policy.max_num:
            return True
        return False

    def validate_pos(self):
        if self.password[self.policy.min_num - 1] == self.policy.let or \
           self.password[self.policy.max_num - 1] == self.policy.let:
            if self.password[self.policy.min_num - 1] != self.password[self.policy.max_num - 1]:
                return True
        return False


def check_passwords(input: List[str]) -> int:
    first_count = 0
    pos_count = 0
    for group in input:
        x = Password_Validator(group)
        if x.validate():
            first_count += 1
        if x.validate_pos():
            pos_count += 1
    return (first_count, pos_count)

test_input = [
'1-3 a: abcde',
'1-3 b: cdefg',
'2-9 c: ccccccccc'
]

print(check_passwords(input_list))
