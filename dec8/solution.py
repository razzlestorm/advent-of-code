from typing import NamedTuple, Tuple


class Command(NamedTuple):
    command: str
    num: int

class CPU:
    def __init__(self, filelength):
        self.running = True
        self.pc = 0
        self.accumulator = 0
        self.ram = [None] * filelength
        self.solved = False

        # Table to call functions with
        self.branchtable = {
            'nop': self.nop,
            'jmp': self.jmp,
            'acc': self.acc
        }

    def load(self, file: str) -> Tuple:
        # keeping track of the address of the command
        for address, command in enumerate(file):
            self.ram[address] = (address, self.parse_command(command))

    def parse_command(self, command):
        c, i = command.split(" ")
        i = int(i)
        return Command(c, i)

    def nop(self, num):
        self.pc += 1

    def jmp(self, num):
        self.pc += num

    def acc(self, num):
        self.accumulator += num
        self.pc += 1

    def run(self):
        """Run the CPU."""
        # we make this a list (or queue) so we can pop the previous command
        try:
	        stack = []
	        while self.running:
	            IR = self.ram[self.pc]
	            if IR[0] == len(self.ram)-1:
	                self.solved = True
	                print("We've finished! Final accumulator is: ")
	                print(self.accumulator)
	                self.running = False
	            elif IR not in stack:
	                stack.append(IR)
	                self.branchtable[IR[1].command](IR[1].num)
	            else:
	                print(self.accumulator)
	                self.running = False
        except IndexError:
            breakpoint()


def iter_commands(commands):
    cpu = CPU(len(commands))
    cpu.load(commands)
    for i, (command, num) in cpu.ram:
        temp = cpu.ram[:]
        if command == 'nop':
            temp[i] = (i, Command('jmp', num))
        elif command == 'jmp':
            temp[i] = (i, Command('nop', num))
        else:
            continue
        cpu2 = CPU(len(temp))
        cpu2.ram = temp
        cpu2.run()
        if cpu2.solved:
            print('Solved: ', cpu2.accumulator)
            break

with open('input.txt') as f:
    command_list = [line for line in f.read().split('\n')]

# sol 1
cpu = CPU(len(command_list))
cpu.load(command_list)
cpu.run()

# sol 2
iter_commands(command_list)
