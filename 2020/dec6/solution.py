from typing import NamedTuple, List

class Group(NamedTuple):
    answers: List[str]

    def stringify(self) -> str:
        return ''.join(self.answers)

    def get_member_count(self) -> int:
        return len(self.answers)

    def get_count1(self) -> int:
        return len(set(self.stringify()))

    def get_count2(self) -> int:
        answer_count = 0
        for let in set(self.stringify()):
            if self.stringify().count(let) == self.get_member_count():
                answer_count += 1
        return answer_count


with open('input.txt') as f:
    input_list = [Group(group.split("\n")) for group in f.read().split('\n\n')]

# sol 1
print(sum([g.get_count1() for g in input_list]))

# sol 2
print(sum([g.get_count2() for g in input_list]))

'''
### pred's two-liner:
groups = data.split('\n\n')
# Part one
print(sum(len(set.union(*map(set, g.split('\n')))) for g in groups))

# Part two
print(sum(len(set.intersection(*map(set, g.split('\n')))) for g in groups))
'''
