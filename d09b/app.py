import sys
import collections

with open(sys.argv[1]) as input:
    filemap = input.readline().strip()


def get_pairs(s):
    while True:
        try:
            x = s[0]
            y = s[1]
            s = s[2:]
        except IndexError:
            yield int(s[0]), int("0")
            return
        yield [int(x), int(y)]


class File:
    left = None
    right = None
    id = 0
    size = 0
    free = 0

    def __init__(self, id, size, free):
        self.id = id
        self.size = size
        self.free = free

    def __str__(self) -> str:
        return f"File #{self.id} (S:{self.size}, F:{self.free}) L:{self.left and self.left.id} R:{self.right and self.right.id}"


class Result:
    pos = 0
    sum = 0
    final = ""

    def add(self, id):
        if id == ".":
            self.final += "."
        else:
            self.final += str(id)
            self.sum += self.pos * id
        self.pos += 1


cur_id = 0
files = []
pairs = list(get_pairs(filemap))
for i, pair in enumerate(pairs):
    files.append(File(cur_id, pair[0], pair[1]))
    cur_id += 1

start = files[0]
end = files[-2]
for i, file in enumerate(files):
    if i > 0:
        file.left = files[i - 1]

    if i < len(files) - 1:
        file.right = files[i + 1]

for f in files:
    print(f)

for i, rf in enumerate(reversed(files)):
    j = len(files) - i - 1
    print(f"FITTING {rf} after {j} files")
    f = start
    while f:
        if rf.size <= f.free:
            print("\tFITS AFTER", f)
            pl, pr = rf.left, rf.right
            if pl:
                pl.free += rf.free + rf.size

            rf.free = f.free - rf.size
            f.free = 0

            # delete from current position
            if rf.left:
                rf.left.right = rf.right
            if rf.right:
                rf.right.left = rf.left

            # insert after f
            rf.left = f
            rf.right = f.right
            if f.right:
                f.right.left = rf
            f.right = rf

            break
        if f.right.id == rf.id:
            break
        f = f.right
    if rf.id == 2:
        break

for f in files:
    print(f)


print("RESULT")
r = Result()
cur = start
while cur:
    print(cur)
    for i in range(cur.size):
        r.add(cur.id)
    for i in range(cur.free):
        r.add(".")

    cur = cur.right


print(r.final)
print(r.sum)


# cur = end
# s = ""
# while cur:
#     for i in range(cur.free):
#         s += "."
#     for i in range(cur.size):
#         s += str(cur.id)

#     cur = cur.left

# # reverse order of s
# print("G", r.final)

# s = s[::-1]
# print("R", s)
