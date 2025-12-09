fresh_list = []

while True:
    inp = input()
    if inp == "":
        break
    fresh_list.append(inp)

ing = []
while True:
    inp = input()
    if inp == "":
        break
    ing.append(inp)

fresh = 0
for i in ing:
    for ing_range in fresh_list:
        left, right = map(int, ing_range.split("-"))
        if left <= int(i) <= right:
            fresh += 1
            break

print(fresh)

# 4m 47s
