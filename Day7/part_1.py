grid = []

while True:
    inp = input()
    if inp == "":
        break
    grid.append(inp)

split_times = 0

visited = {}


def beam_down(x, y):
    global split_times
    if x < 0 or x >= len(grid[0]):
        return
    while y < len(grid):
        if (x, y) in visited:
            return
        visited[(x, y)] = True
        if grid[y][x] == "^":
            print(x, y)
            split_times += 1
            beam_down(x - 1, y)
            beam_down(x + 1, y)
            return
        y += 1


start_idx = 0
for i in range(len(grid[0])):
    if grid[0][i] == "S":
        start_idx = i
        break

print(start_idx)


beam_down(start_idx, 0)
print(split_times)

# 11m 09
