# Solution to day 7 of AOC 2015, Some Assembly Required
# https://adventofcode.com/2015/day/7

def is_integer(candidate: str) -> bool:
    """Returns True if parm is a an integer."""
    if candidate[0] == '-':
        return candidate[1:].isnumeric()
    return candidate.isnumeric()


f = open('input.txt')
whole_text = f.read()
f.close()

lines = whole_text.split('\n')
# print('lines:', lines)

circuit = {}
for connection in lines:
    gate, wire = connection.split(' -> ')
    circuit[wire] = gate

# For Part 2.
circuit['b'] = '956'

to_do = -1
while to_do != 0:
    to_do = 0

    for wire in circuit:
        if 'NOT' in circuit[wire]:
            _, op1 = circuit[wire].split('NOT ')
            if op1.isnumeric():
                circuit[wire] = str(~ int(op1))
            elif is_integer(circuit[op1]):
                circuit[wire] = 'NOT ' + circuit[op1]

        elif 'LSHIFT' in circuit[wire]:
            op1, op2 = circuit[wire].split(' LSHIFT ')
            if op1.isnumeric():
                circuit[wire] = str(int(op1) << int(op2))
            elif is_integer(circuit[op1]):
                circuit[wire] = circuit[op1] + ' LSHIFT ' + op2

        elif 'RSHIFT' in circuit[wire]:
            op1, op2 = circuit[wire].split(' RSHIFT ')
            if is_integer(op1):
                circuit[wire] = str(int(op1) >> int(op2))
            elif circuit[op1].isnumeric():
                circuit[wire] = circuit[op1] + ' RSHIFT ' + op2

        elif 'OR' in circuit[wire]:
            op1, op2 = circuit[wire].split(' OR ')
            if is_integer(op1) and is_integer(op2):
                circuit[wire] = str(int(op1) | int(op2))
            elif not op1.isnumeric():
                if is_integer(circuit[op1]):
                    circuit[wire] = circuit[op1] + ' OR ' + op2
            elif not is_integer(op2):
                if is_integer(circuit[op2]):
                    circuit[wire] = op1 + ' OR ' + circuit[op2]

        elif 'AND' in circuit[wire]:
            op1, op2 = circuit[wire].split(' AND ')
            if is_integer(op1) and is_integer(op2):
                circuit[wire] = str(int(op1) & int(op2))
            elif not is_integer(op1):
                if is_integer(circuit[op1]):
                    circuit[wire] = circuit[op1] + ' AND ' + op2
            elif not is_integer(op2):
                if is_integer(circuit[op2]):
                    circuit[wire] = op1 + ' AND ' + circuit[op2]

        elif not is_integer(circuit[wire]):
            if is_integer(circuit[circuit[wire]]):
                circuit[wire] = circuit[circuit[wire]]

        if not is_integer(circuit[wire]):
            to_do += 1
            # print(wire, ':', circuit[wire])

    # print(circuit)
    print('to_do:', to_do)

print(circuit['a'])
