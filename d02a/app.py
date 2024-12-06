import sys

reports = []
with open(sys.argv[1]) as report:
    for line in report.readlines():
        reports.append([int(x) for x in line.strip().split()])


def test_report(report):
    dir = None
    last = None

    for x in report:
        if last is None:
            last = x
            continue

        diff = x - last

        if diff == 0:
            return False

        if dir is None:
            if diff < 0:
                dir = "down"
            elif diff > 0:
                dir = "up"

        print(dir, diff, "-", last, x)

        if dir == "up" and 0 <= diff <= 3:
            print(last, x, "in range at", diff)
        elif dir == "down" and -3 <= diff <= 0:
            print(last, x, "in range at", diff)
        else:
            return False

        last = x

    return True


count = 0

for report in reports:
    safe = test_report(report)
    print(report, safe)

    if safe:
        count += 1

print(count)
