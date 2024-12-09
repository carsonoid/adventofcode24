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
        yield int(x), int(y)


cur_id = 0
files = []
for pair in get_pairs(filemap):
    files.append((cur_id, *pair))
    cur_id += 1

print(files)


class Result:
    pos = 0
    sum = 0
    final = ""

    def add(self, id):
        self.final += str(id)
        self.sum += self.pos * id
        self.pos += 1


def get_result():
    r = Result()
    files_copy = files.copy()
    last_file = list(files_copy.pop())
    for file in files:
        print(file)
        id, size, free = file
        curid = id

        if id >= last_file[0]:
            print("LAST", last_file)
            id, size, free = last_file
            for x in range(0, size):
                print("\t CHK", r.pos, id)
                r.add(id)
            return r

        for x in range(0, size):
            print("\t CHK", r.pos, id)
            r.add(id)

        for x in range(0, free):
            id = last_file[0]
            print("\tMCHK", r.pos, id, last_file)
            r.add(id)
            last_file[1] = last_file[1] - 1
            if last_file[1] == 0:
                last_file = list(files_copy.pop())
                print("\t\tPOP", last_file, id)
                if last_file[0] <= curid:
                    return r


r = get_result()

print(r.final)
print(r.sum)
