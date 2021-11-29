from typing import List, NamedTuple, NewType

with open('input.txt') as f:
    input_list = [line.strip() for line in f]

# example line in input_list: '3-8 t wttlmpdkfkf'

class Password_Validator(NamedTuple):
    min_num: int
    max_num: int
    let: str
    password: str

    def validate(self) -> bool:
        return self.min_num <= self.password.count(self.let) <= self.max_num

    def validate_position(self) -> bool:
        return (self.password[self.min_num -1] == self.let) \
               != (self.password[self.max_num -1] == self.let)


    @staticmethod
    def line_parser(line: str) -> NamedTuple:
        bounds, let, password = line.strip().split(" ")
        min, max = [int(n) for n in bounds.split("-")]
        let = let.strip(":")
        return Password_Validator(min, max, let, password)


def check_passwords(input: List[str]) -> int:
    passwords = [Password_Validator.line_parser(line) for line in input_list]
    return (sum((obj.validate() for obj in passwords)),
            sum((obj.validate_position() for obj in passwords)))

test_input = [
'1-3 a: abcde',
'1-3 b: cdefg',
'2-9 c: ccccccccc'
]

print(check_passwords(input_list))
# answer: (393, 690)
