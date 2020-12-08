from typing import NamedTuple, List, Tuple, Dict
from collections import defaultdict
import re


class Command(NamedTuple):
    command: str
    num: int


class CPU:
    def __init__(self, filelength):
        self.running = True
        self.pc = 0
        self.accumulator = 0
        self.ram = [None] * filelength

        self.branchtable = {
            'nop': self.nop,
            'jmp': self.jmp,
            'acc': self.acc
        }


    def load(self, file):
        address = 0
        # keeping track of the line of the command
        for ii, command in enumerate(file):
            self.ram[address] = (ii, self.parse_command(command))
            address += 1

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
        visited = set()
        while self.running:
            IR = self.ram[self.pc]
            if IR[0] not in visited:
                visited.add(IR[0])
                self.branchtable[IR[1].command](IR[1].num)
            else:
                print(self.accumulator)
                self.running = False


with open('input.txt') as f:
    command_list = [line for line in f.read().split('\n')]

cpu = CPU(len(command_list))
cpu.load(command_list)
cpu.run()
