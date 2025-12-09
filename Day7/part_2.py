grid = []

while True:
    inp = input()
    if inp == "":
        break
    grid.append(inp)


visited = {}


def beam_down(x, y):
    split_times = 0
    if x < 0 or x >= len(grid[0]):
        return
    while y < len(grid):
        if (x, y) in visited:
            return visited[(x, y)]
        if grid[y][x] == "^":
            split_times += beam_down(x - 1, y)
            split_times += beam_down(x + 1, y)
            visited[(x, y)] = split_times
            return split_times
        y += 1
    return 1


start_idx = 0
for i in range(len(grid[0])):
    if grid[0][i] == "S":
        start_idx = i
        break

print(start_idx)


print(beam_down(start_idx, 0))

# 7m 11
