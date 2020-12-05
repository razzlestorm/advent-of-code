from typing import Tuple
import math


ROWS = (0, 127)
# F = lower half, B = upper half
COLS = (0, 7)
# L = lower half, R = upper half

example = 'FBFBBFFRLR'
example_rows = example[:7]
example_cols = example[7:]

print(example_rows)
print(example_cols)
class Ticket:
    def __init__(self, code, rows=ROWS, cols=COLS):
        self.code = code
        self.rows = rows
        self.cols = cols
        self.id = self.parse_rows() * 8 + self.parse_cols()

    def parse_rows(self):
        for let in self.code[:7]:
            self.rows = self.choose_half(let, self.rows)
        return self.rows[0]

    def parse_cols(self):
        for let in self.code[7:]:
            self.cols = self.choose_half(let, self.cols)
        return self.cols[0]

    @staticmethod
    def choose_half(let: str, tick_range: Tuple) -> Tuple:
        total_sum = tick_range[0]+tick_range[1]
        if let in {'F', 'L'}:
            return (tick_range[0], total_sum//2)
        elif let in {'B', 'R'}:
            return (math.ceil(total_sum/2), tick_range[1])



with open('input.txt') as f:
    input_list = f.read().split('\n')
    tickets = [line for line in input_list]

ticket_ids = [Ticket(ticket).id for ticket in tickets]
print(min(ticket_ids))
print(max(ticket_ids))

for ii in range(min(ticket_ids), max(ticket_ids)+1):
    if ii not in ticket_ids:
        print(ii)
