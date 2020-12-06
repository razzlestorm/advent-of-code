from typing import NamedTuple, List

class Group(NamedTuple):
    answers: List

    def get_member_count(self):
        pass
    def get_count1(self) -> int:
        return len(set(''.join(self.answers)))

    def get_count2(self) -> int:
        pass



with open('input.txt') as f:
    input_list = [Group(group.split("\n")) for group in f.read().split('\n\n')]

print(input_list)
# sol 1
print(sum([g.get_count() for g in input_list]))
