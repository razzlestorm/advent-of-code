from typing import NamedTuple


class Command(NamedTuple):
    command: str
    num: int

class CPU:
    def __init__(self, filelength):
        self.running = True
        self.pc = 0
        self.accumulator = 0
        self.ram = [None] * filelength
        self.rebooted = False

        # Table to call functions with
        self.branchtable = {
            'nop': self.nop,
            'jmp': self.jmp,
            'acc': self.acc
        }

    def load(self, file):
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
        stack = []
        while self.running:
            IR = self.ram[self.pc]
            if IR not in stack:
                stack.append(IR)
                self.branchtable[IR[1].command](IR[1].num)
            elif IR[0] == len(self.ram)-1:
                print("We've finished! Final accumulator is: ")
                print(self.accumulator)
                self.running = False

            elif self.rebooted is False:
                print(self.accumulator)
                # We get the previous command:
                IR = stack.pop()
                # overwrite command at ram address:
                if IR[1].command == 'nop':
                    self.ram[IR[0]] = (IR[0], Command('jmp', IR[1].num))
                elif IR[1].command == 'jmp':
                    self.ram[IR[0]] = (IR[0], Command('nop', IR[1].num))
                # reset and go again (should only happen once)
                self.pc = 0
                self.accumulator = 0
                stack = []
                self.rebooted = True

            else:
                breakpoint()
                print('bug')




with open('input.txt') as f:
    command_list = [line for line in f.read().split('\n')]

cpu = CPU(len(command_list))
cpu.load(command_list)
cpu.run()
