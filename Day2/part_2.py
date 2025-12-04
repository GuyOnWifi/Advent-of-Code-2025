raw = input()
data = raw.split(",")


def sum_invalid(l, r):
    start = len(l)
    stop = len(r)

    int_l = int(l)
    int_r = int(r)

    total = 0
    seen = {}
    for digits in range(start, stop + 1):
        for i in range(2, digits + 1):
            if digits % i != 0:
                # not divisible
                continue

            id_len = digits // i
            for j in range(10 ** (id_len - 1), 10**id_len):
                test_id = int(str(j) * i)
                if (test_id >= int_l) and (test_id <= int_r):
                    if test_id not in seen:
                        total += test_id
                        seen[test_id] = 1

                if test_id > int_r:
                    break

    return total


sum = 0
for id_range in data:
    (left, right) = id_range.split("-")
    sum += sum_invalid(left, right)


print(sum)
