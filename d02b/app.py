import sys

reports = []
with open(sys.argv[1]) as report:
    for line in report.readlines():
        reports.append([int(x) for x in line.strip().split()])


def test_report(report, skip=None):
    if skip is not None:
        report = report[:skip] + report[skip + 1 :]  # wasteful!

    print("\t", report)

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

    print("Valid")
    return True


count = 0

for report in reports:
    if test_report(report):
        count += 1
    else:
        for i in range(len(report)):
            print(i)
            if test_report(report, i):
                count += 1
                break

print(count)
