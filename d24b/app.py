import sys

wires = {}


class Wire:
    name: str
    value: bool

    def __init__(self, name):
        self.name = name
        self.value = None
        self.into = []
        self.outof = []
        wires[name] = self

    def hook_into(self, gate):
        self.into.append(gate)

    def hook_outof(self, gate):
        self.outof.append(gate)

    def set(self, value):
        self.value = value
        for g in self.into:
            g.handle()


class Gate:
    op: str

    def hookup(self, input1: Wire, op: str, input2: Wire, output: Wire):
        self.input1 = input1
        self.op = op
        self.input2 = input2
        self.output = output

    def handle(self):
        if self.input1.value is None or self.input2.value is None:
            return

        match self.op:
            case "AND":
                self.output.set(self.input1.value and self.input2.value)
            case "OR":
                self.output.set(self.input1.value or self.input2.value)
            case "XOR":
                self.output.set(self.input1.value != self.input2.value)


def to_binary(int) -> list[bool]:
    return [bool(int & (1 << i)) for i in range(24)]


def from_binary(bits: list[bool]) -> int:
    return sum(1 << i for i, b in enumerate(bits) if b)


def get_wire(name):
    if name not in wires:
        wires[name] = Wire(name)
    return wires[name]


with open(sys.argv[1]) as f:
    gate_strings = f.read().strip().split("\n\n")[1].split("\n")


def clear_wires():
    for w in wires.values():
        w.value = None


def set_init(a, initval):
    for j, val in enumerate(to_binary(initval)):
        k = a + str(j).rjust(2, "0")
        if k not in wires:
            wires[k] = Wire(k)

        wires[k].set(val)


def check_wire(a):
    vals = []
    for i in range(24):
        k = a + str(i).rjust(2, "0")
        if k not in wires:
            continue
        vals.append(wires[k].value)
    return from_binary(vals)


gates = []
for s in gate_strings:
    if s.startswith("#"):
        continue
    parts = s.split()
    g = Gate()
    input1 = get_wire(parts[0])
    input1.hook_into(g)
    input2 = get_wire(parts[2])
    input2.hook_into(g)
    output = get_wire(parts[4])
    output.hook_outof(g)
    g.hookup(input1, parts[1], input2, output)
    gates.append(g)


worked = False
for testnum in range(5000):
    clear_wires()
    set_init("x", testnum)
    set_init("y", testnum)
    x = check_wire("x")
    y = check_wire("y")
    z = check_wire("z")
    if z != x + y:
        if worked:
            print("FAIL", x, "+", y, "=", z)
        worked = False
    else:
        if not worked:
            print("P   ", x, "+", y, "=", z)
        worked = True


# NOTE: In the end I just solved this one by hand so this code only tests validity, it doesn't solve the problem.
