import sys
from functools import cache

# Shameless copy of work from https://topaz.github.io/paste/#XQAAAQD6EQAAAAAAAAA4GEiZzRd1JAgz+whYRQxSFI7XvmlfhtGDinguAj8sFyD4ftJ8OW5ekoqnVIaEYm1TRzRozXdrSWph6uPxJTZjFA79rnO0DuC0UuIh7ERk/Duk3psptqVA73J8Z4I2hW2SL6gJB3Q1/1XR38DhDEO8md9rWyVWBo4CJDydIWxuyMJcWVQ1ufgwX0ZmJoE5ZQfJjzbh+DZJ+rn4Sbosya9WNQ6/9qJVmsYOKTaGQSnTXeXuKSxXcsEM8aOYrwwokHmz1qm/XBD0xY3AAVJTkzrYdTl4OQox1mjh84ro0qEU4/rUv+M6fqUGeLv9d6MjvSvdq9zb3kVlUg0EIXhQNEfOjoUDdnZjwo6W1fT4LIOQRKQDTXkLNCovRuWLphjKGCHFmcJyrSRLcBrpa3UPBz2cIWDABX80asng9GqkqlBPZ00Xwo7HcF2g/+CbHp5krjy5MghjW+IFMXZ6KzO3bqOGmmXmXmAJbcPpaASmOyJuZAIqZPlGWT8cfySbmkncDrAdGAl5s9SaZp+ouygkV74I+YpoBLf0T+bbJ4jHatgdyEeX+hb35+eN08OB0E0S06WUzSAHJfIJV6QqkQAhlu3aJTiam9LsuRQa8l65jvSVum1zympU0thS5R73tSq43ExG3n7ZoPEt54+GoAqWEb8DYTiiSaLSL0E+aDYNsxeBhJNU8aw3+TPNHS5AOzEHuKfY1fAfcvsx8tcpeEB1bSGtPhmjbDOJtnzhdS76jrV68K4hjgzpqJ/YfVeoIhVBPJpnc9AuNMyMECjKIN9gOhKqzooSr6teDDrCi6EFCvwAWoA9BQtKq+m4nH0QPUznsSCp4WVVzzeuuUQU9VKbtJClZlWGdFOp+iaoaZg3jec+rsSrPbW/Egz9Wz6G+BT+ehdYjxUjkSj27qxJK0O+0prbEkq1E4rjNgZIq0l1n76ERO7TPmYhDOzOP/URcnhJJ27nB6eeeABAlr7ovC+1nFP51FNvugYf8NvGQ1T5Tk/X1yGvomNHwHvvJ6PWDQn4FgDPQj1f6AEqnD1aStgkAszG7CSoF1shmf6ODrEcuELJ+UcVUrD2QFMiIqpi5xaez/noF5INiALPoYedsYG9cQ1ogzqBK80652Q2JK7YxdAX9N2ANeYF9tdZ6kY4Gh4t9sIa16T1ujIPde/SFaEFy/uxVkjwMsxUMdLCyIKJJ9YtPI9Ahfmt+3HziHQHM3IQ8sqTlPnyFPp2JLazKBkPlOuaZ1Q+xFRmTf5urms6GyI4GZ6nsjRCoGqJ391vaD8LhgSUlbTVPLgPolti1H4WVKv/DMee2bSRnpmlbff9/BzPP/qbip1F1iw2Za9WZ7ycf4zMn2/zK0VW8OtNAfRTStX3wqWNStrdPSPppYtRSnsHTkGYND3q5lLI0JyEJNu11IOiM2XQMVzF6QgTOuiCx8qKdFG+pUtWL2onkj2iNOvURnsU0jTqWH2rCVdG6T9JeXEjZno7bABLfBmyMNBB+v9ajn+Nv0pW7Ag9cHPgeogkZVvx6zaJTpPQQ/cD2juyVFpEsdBmXEqaIVrKOCIUYnZUwEmEF3zeDqdJZqlYwrQcQzD4xX4SpDxWRXDTR24Rg7zj/vuA/eO1eb4IA/qLxhltMAb7VLqZOU0imaKmDZHOjTP14WoRXD/uy6Y7p9BThBCmg+fX3QXFu5HsCgN82aaAbKJ6laKX2CbA6//SMmnE
# Ref: https://www.reddit.com/r/adventofcode/comments/1hj2odw/comment/m36j01x/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# I think it is probably better to copy somone's system then give up after 3 failed tries
# At least I'll learn something about python by transcoding
ideal_paths = {
    ("A", "0"): "<A",
    ("0", "A"): ">A",
    ("A", "1"): "^<<A",
    ("1", "A"): ">>vA",
    ("A", "2"): "<^A",
    ("2", "A"): "v>A",
    ("A", "3"): "^A",
    ("3", "A"): "vA",
    ("A", "4"): "^^<<A",
    ("4", "A"): ">>vvA",
    ("A", "5"): "<^^A",
    ("5", "A"): "vv>A",
    ("A", "6"): "^^A",
    ("6", "A"): "vvA",
    ("A", "7"): "^^^<<A",
    ("7", "A"): ">>vvvA",
    ("A", "8"): "<^^^A",
    ("8", "A"): "vvv>A",
    ("A", "9"): "^^^A",
    ("9", "A"): "vvvA",
    ("0", "1"): "^<A",
    ("1", "0"): ">vA",
    ("0", "2"): "^A",
    ("2", "0"): "vA",
    ("0", "3"): "^>A",
    ("3", "0"): "<vA",
    ("0", "4"): "^<^A",
    ("4", "0"): ">vvA",
    ("0", "5"): "^^A",
    ("5", "0"): "vvA",
    ("0", "6"): "^^>A",
    ("6", "0"): "<vvA",
    ("0", "7"): "^^^<A",
    ("7", "0"): ">vvvA",
    ("0", "8"): "^^^A",
    ("8", "0"): "vvvA",
    ("0", "9"): "^^^>A",
    ("9", "0"): "<vvvA",
    ("1", "2"): ">A",
    ("2", "1"): "<A",
    ("1", "3"): ">>A",
    ("3", "1"): "<<A",
    ("1", "4"): "^A",
    ("4", "1"): "vA",
    ("1", "5"): "^>A",
    ("5", "1"): "<vA",
    ("1", "6"): "^>>A",
    ("6", "1"): "<<vA",
    ("1", "7"): "^^A",
    ("7", "1"): "vvA",
    ("1", "8"): "^^>A",
    ("8", "1"): "<vvA",
    ("1", "9"): "^^>>A",
    ("9", "1"): "<<vvA",
    ("2", "3"): ">A",
    ("3", "2"): "<A",
    ("2", "4"): "<^A",
    ("4", "2"): "v>A",
    ("2", "5"): "^A",
    ("5", "2"): "vA",
    ("2", "6"): "^>A",
    ("6", "2"): "<vA",
    ("2", "7"): "<^^A",
    ("7", "2"): "vv>A",
    ("2", "8"): "^^A",
    ("8", "2"): "vvA",
    ("2", "9"): "^^>A",
    ("9", "2"): "<vvA",
    ("3", "4"): "<<^A",
    ("4", "3"): "v>>A",
    ("3", "5"): "<^A",
    ("5", "3"): "v>A",
    ("3", "6"): "^A",
    ("6", "3"): "vA",
    ("3", "7"): "<<^^A",
    ("7", "3"): "vv>>A",
    ("3", "8"): "<^^A",
    ("8", "3"): "vv>A",
    ("3", "9"): "^^A",
    ("9", "3"): "vvA",
    ("4", "5"): ">A",
    ("5", "4"): "<A",
    ("4", "6"): ">>A",
    ("6", "4"): "<<A",
    ("4", "7"): "^A",
    ("7", "4"): "vA",
    ("4", "8"): "^>A",
    ("8", "4"): "<vA",
    ("4", "9"): "^>>A",
    ("9", "4"): "<<vA",
    ("5", "6"): ">A",
    ("6", "5"): "<A",
    ("5", "7"): "<^A",
    ("7", "5"): "v>A",
    ("5", "8"): "^A",
    ("8", "5"): "vA",
    ("5", "9"): "^>A",
    ("9", "5"): "<vA",
    ("6", "7"): "<<^A",
    ("7", "6"): "v>>A",
    ("6", "8"): "<^A",
    ("8", "6"): "v>A",
    ("6", "9"): "^A",
    ("9", "6"): "vA",
    ("7", "8"): ">A",
    ("8", "7"): "<A",
    ("7", "9"): ">>A",
    ("9", "7"): "<<A",
    ("8", "9"): ">A",
    ("9", "8"): "<A",
    ("<", "^"): ">^A",
    ("^", "<"): "v<A",
    ("<", "v"): ">A",
    ("v", "<"): "<A",
    ("<", ">"): ">>A",
    (">", "<"): "<<A",
    ("<", "A"): ">>^A",
    ("A", "<"): "v<<A",
    ("^", "v"): "vA",
    ("v", "^"): "^A",
    ("^", ">"): "v>A",
    (">", "^"): "<^A",
    ("^", "A"): ">A",
    ("A", "^"): "<A",
    ("v", ">"): ">A",
    (">", "v"): "<A",
    ("v", "A"): "^>A",
    ("A", "v"): "<vA",
    (">", "A"): "^A",
    ("A", ">"): "vA",
}


with open(sys.argv[1]) as f:
    codes = f.read().strip().split("\n")


@cache
def get_length(seq: str, depth: int):
    length = 0
    if not depth:
        length = len(seq)
    else:
        cur = "A"
        for next in seq:
            move_len = get_move_count(cur, next, depth)
            cur = next
            length += move_len
    return length


def get_move_count(cur, next, depth):
    if cur == next:
        return 1

    return get_length(ideal_paths[(cur, next)], depth - 1)


total = 0
for code in codes:
    total += int(code.rstrip("A")) * get_length(code, 26)

print(total)
