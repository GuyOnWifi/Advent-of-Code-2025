grid = []
while True:
    inp = input()
    if inp == "":
        break
    grid.append(inp.split())


print(grid)
sum = 0
for i in range(len(grid[0])):
    res = 0
    if grid[-1][i] == "+":
        for j in range(len(grid) - 2, -1, -1):
            res += int(grid[j][i])

    if grid[-1][i] == "*":
        res = 1
        for j in range(len(grid) - 2, -1, -1):
            res *= int(grid[j][i])
    print(res)
    sum += res

print(sum)

# 6m 09
