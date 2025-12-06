grid = []
while True:
    inp = input()
    if inp == "":
        break
    grid.append(inp)

tmp = 1
split_mask = []
while tmp < len(grid[-1]):
    num_spaces = 0
    for i in range(tmp, len(grid[-1])):
        tmp += 1
        if grid[-1][i] == " ":
            num_spaces += 1
        else:
            break
    split_mask.append(num_spaces)

split_mask[-1] += 1
print(split_mask)

idx = 0
total = 0
for i in split_mask:
    nums = []
    op = grid[-1][idx]
    print(op)
    for j in range(i):
        num = 0
        for k in range(len(grid) - 1):
            if grid[k][idx] == " ":
                continue
            num = 10 * num + int(grid[k][idx])
        idx += 1
        print(num)
        nums.append(num)

    if op == "+":
        sum = 0
        for n in nums:
            sum += n
        print(sum)
        total += sum

    if op == "*":
        sum = 1
        for n in nums:
            sum *= n
        print(sum)
        total += sum
    idx += 1  # advance space

print(total)


# rougly 25 mins (9:12 ended)
