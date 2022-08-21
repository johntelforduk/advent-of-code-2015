# Solution to day 23 of AOC 2015, Opening the Turing Lock
# https://adventofcode.com/2015/day/23


class Computer:

    def __init__(self, filename: str):
        f = open(filename)
        whole_text = f.read()
        f.close()

        self.program = whole_text.split('\n')
        print(self.program)
        self.pc = 0                                 # Program counter.
        self.registers = {'a': 0, 'b': 0}

    def hlf(self, operand):
        """hlf r sets register r to half its current value, then continues with the next instruction."""
        self.registers[operand] = self.registers[operand] // 2
        self.pc += 1

    def tpl(self, operand):
        """tpl r sets register r to triple its current value, then continues with the next instruction."""
        self.registers[operand] = self.registers[operand] * 3
        self.pc += 1

    def inc(self, operand):
        """inc r increments register r, adding 1 to it, then continues with the next instruction."""
        self.registers[operand] = self.registers[operand] + 1
        self.pc += 1

    def jmp(self, operand):
        """jmp offset is a jump; it continues with the instruction offset away relative to itself."""
        self.pc += int(operand)

    def jie(self, operands):
        """jie r, offset is like jmp, but only jumps if register r is even ("jump if even")."""
        register, offset = operands.split(', ')
        if (self.registers[register] % 2) == 0:
            self.jmp(offset)
        else:
            self.pc += 1

    def jio(self, operands):
        """jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd)."""
        register, offset = operands.split(', ')
        if self.registers[register] == 1:
            self.jmp(offset)
        else:
            self.pc += 1

    def evaluate(self):
        """Evaluate instruction at program counter."""
        operators = {'hlf': self.hlf,
                     'tpl': self.tpl,
                     'inc': self.inc,
                     'jmp': self.jmp,
                     'jie': self.jie,
                     'jio': self.jio}

        instruction = self.program[self.pc]
        operator = instruction[0: 3]
        operands = instruction[4:]

        print(f"{self.pc} | {instruction} | a={self.registers['a']} | b={self.registers['b']}")

        command = operators[operator]
        command(operands)

    def run(self):
        while self.pc < len(self.program):
            # print(self.pc)
            self.evaluate()


part2 = Computer('input.txt')
part2.registers['a'] = 1
part2.run()
print(part2.registers)
