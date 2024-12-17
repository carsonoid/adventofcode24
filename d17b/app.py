import sys
import math


def run(reg_a, reg_b, reg_c, prog):
    out = []
    ptr = 0
    while ptr < len(prog) - 1:
        opcode = prog[ptr]
        literal_operand = prog[ptr + 1]
        combo_operand = None
        match literal_operand:
            case 0 | 1 | 2 | 3:
                combo_operand = literal_operand
            case 4:
                combo_operand = reg_a
            case 5:
                combo_operand = reg_b
            case 6:
                combo_operand = reg_c

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

    return out


with open(sys.argv[1]) as f:
    data = f.readlines()
    reg_a = int(data[0].split()[-1])
    reg_b = int(data[1].split()[-1])
    reg_c = int(data[2].split()[-1])

    prog = [int(x) for x in data[4].split()[1].split(",")]

print("Start", reg_a, reg_b, reg_c)
print(prog)
print()


# shameless inspiration from https://github.com/categoraal/adventofcode2024/blob/main/day17.py
# but reverse engineering / rewriting it helped me understand the solution. Which is better then giving up!
def solve(n, d):
    min = float("inf")
    if d == -1:
        return n
    for i in range(8):
        nn = n + i * 8**d
        output = run(nn, 0, 0, prog)
        if len(output) != len(prog):
            continue
        if output[d] == prog[d]:
            res = solve(nn, d - 1)
            if res < min:
                min = res
    return min


print("RESULT", solve(0, 15))
