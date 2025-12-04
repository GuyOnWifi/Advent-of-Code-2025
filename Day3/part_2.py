batteries = []

while True:
    inp = input()
    if inp == "":
        break

    batteries.append(inp)


sum = 0
for b in batteries:
    num = 0
    start_from = -1

    for i in range(12):
        highest = -1
        for i in range(start_from + 1, len(b) - (11 - i)):
            if int(b[i]) > highest:
                start_from = i
                highest = int(b[i])
        num = 10 * num + highest
    print(num)
    sum += num


print(sum)

# 3m 18s
