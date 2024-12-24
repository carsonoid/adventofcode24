import sys

wires = {}


class Wire:
    name: str
    value: bool

    def __init__(self, name):
        self.name = name
        self.value = None
        self.into = []
        wires[name] = self

    def hook_into(self, gate):
        self.into.append(gate)

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


def get_wire(name):
    if name not in wires:
        wires[name] = Wire(name)
    return wires[name]


with open(sys.argv[1]) as f:
    wire_strings, gate_strings = [x.strip().split("\n") for x in f.read().split("\n\n")]


gates = []
for s in gate_strings:
    parts = s.split()
    g = Gate()
    input1 = get_wire(parts[0])
    input1.hook_into(g)
    input2 = get_wire(parts[2])
    input2.hook_into(g)
    output = get_wire(parts[4])
    g.hookup(input1, parts[1], input2, output)
    gates.append(g)

for s in wire_strings:
    wire, value_string = s.split(": ")
    value = value_string == "1"
    print("SET", wire, value)
    wires[wire].set(value)


zgates = []
for k, v in wires.items():
    if k.startswith("z"):
        zgates.append(v)

ret = 0
i = 0
for gate in sorted(zgates, key=lambda g: g.name):
    print(gate.name, gate.value)
    if gate.value:
        ret += 1 << i
    i += 1
print(ret)
