data = []
while True:
    inp = input()
    if inp == "":
        break

    data.append(inp)


def pos_mod(num, m):
    return (num % m + m) % m


pos = 50
count = 0
for d in data:
    if d.startswith("L"):
        num = int(d[1:])
        pos = pos_mod(pos - num, 100)
    else:
        num = int(d[1:])
        pos = pos_mod(pos + num, 100)

    if pos == 0:
        count += 1

print(count)
