raw = input()
data = raw.split(",")


def is_invalid(l, r):
    start = len(l)
    stop = len(r)

    int_l = int(l)
    int_r = int(r)

    total = 0
    for i in range(start, stop + 1):
        if i % 2 == 1:
            continue
        repeating = 10 ** (i // 2 - 1)
        while True:
            test_id = repeating * (10 ** (i // 2)) + repeating
            if test_id > int_r:
                return total
            if test_id >= int_l and test_id <= int_r:
                print(test_id)
                total += test_id
            repeating += 1
            if len(str(repeating)) > i // 2:
                break

    return total


sum = 0
for id_range in data:
    (left, right) = id_range.split("-")
    sum += is_invalid(left, right)

print(sum)
