fresh_list = []

while True:
    inp = input()
    if inp == "":
        break
    fresh_list.append(list(map(int, inp.split("-"))))

ing = []
while True:
    inp = input()
    if inp == "":
        break
    ing.append(inp)

fresh_list.sort()

fresh = 0
idx = 0
range_left = -1
range_right = -1
while idx < len(fresh_list):
    (l, r) = fresh_list[idx]
    if range_left == -1:
        range_left = l
        range_right = r
        continue

    if range_left <= l <= range_right:
        range_right = max(range_right, r)
    else:
        fresh += (range_right - range_left) + 1
        range_left = l
        range_right = r

    idx += 1

fresh += (range_right - range_left) + 1

print(fresh)

# 7m 54s
