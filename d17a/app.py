import sys
import math

with open(sys.argv[1]) as f:
    data = f.readlines()
    reg_a = int(data[0].split()[-1])
    reg_b = int(data[1].split()[-1])
    reg_c = int(data[2].split()[-1])

    prog = [int(x) for x in data[4].split()[1].split(",")]

print("Start", reg_a, reg_b, reg_c)
print(prog)
print()


def get_operand(x):
    match x:
        case 0 | 1 | 2 | 3:
            return x
        case 4:
            return reg_a
        case 5:
            return reg_b
        case 6:
            return reg_c
        case 7:
            return None
    raise ValueError(f"unmatched operand {x}")


out = []

ptr = 0

while ptr < len(prog) - 1:
    opcode = prog[ptr]
    literal_operand = prog[ptr + 1]
    combo_operand = get_operand(literal_operand)
    # print(">", reg_a, reg_b, reg_c)
    # print(opcode, literal_operand, combo_operand)
    match opcode:
        case 0:  # division
            reg_a = math.trunc(reg_a / pow(2, combo_operand))
        case 1:  # bitwise XOR of B
            reg_b = reg_b ^ literal_operand
        case 2:  # modulo 8
            reg_b = combo_operand % 8
        case 3:  # nothing or jump
            if reg_a:
                ptr = literal_operand
                continue
        case 4:  # bitwise XOR B C
            reg_b = reg_b ^ reg_c
        case 5:  # modulo 8
            out.append(combo_operand % 8)
        case 6:  # division
            reg_b = math.trunc(reg_a / pow(2, combo_operand))
        case 7:  # division
            reg_c = math.trunc(reg_a / pow(2, combo_operand))
    ptr += 2

print("E", reg_a, reg_b, reg_c)
print(",".join([str(x) for x in out]))
