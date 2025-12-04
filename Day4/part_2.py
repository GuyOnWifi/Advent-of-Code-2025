grid = []

while True:
    inp = input()
    if inp == "":
        break
    grid.append(list(inp))


def has_roll(grid, x, y):
    if x < 0 or x >= len(grid[0]):
        return False
    if y < 0 or y >= len(grid):
        return False
    return grid[y][x] == "@"


sum = 0
while True:
    changed = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            num_roll = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    if has_roll(grid, j + dx, i + dy):
                        num_roll += 1
            if num_roll < 4 and grid[i][j] == "@":
                grid[i][j] = "."
                changed += 1

    sum += changed
    if changed == 0:
        break

print(sum)

# 2m 43s
