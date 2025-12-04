batteries = []

while True:
    inp = input()
    if inp == "":
        break

    batteries.append(inp)


sum = 0
for b in batteries:
    start_from = 0
    highest = -1
    for i in range(len(b) - 1):
        if int(b[i]) > highest:
            start_from = i
            highest = int(b[i])

    second_highest = -1
    for i in range(start_from + 1, len(b)):
        second_highest = max(second_highest, int(b[i]))

    sum += highest * 10 + second_highest

print(sum)

# 3m 31s
