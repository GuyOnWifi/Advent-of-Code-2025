data = []
while True:
    inp = input()
    if inp == "":
        break

    data.append(inp)


def pos_mod(num, m):
    if num == 0:
        return (0, 1)
    res = (num % m + m) % m

    loop = abs(num) // m
    if num < 0:
        loop += 1

    return (res, loop)


pos = 50
loop = 0
count = 0
for d in data:
    if d.startswith("L"):
        num = int(d[1:])
        if pos == 0:
            count -= 1
        (pos, loop) = pos_mod(pos - num, 100)
    else:
        num = int(d[1:])
        (pos, loop) = pos_mod(pos + num, 100)

    count += loop
    print(pos, loop)

print(count)
