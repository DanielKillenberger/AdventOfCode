from functools import reduce

with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")

width = len(input[0])

x_steps = [1, 3, 5, 7]
xs = [0] * 4
amount_trees = [0] * 5
for y in range(len(input)):
    for i in range(4):
        if input[y][xs[i]] == "#":
            amount_trees[i] += 1
        xs[i] = (xs[i] + x_steps[i]) % width

x = 0
for y in range(0, len(input), 2):
    if input[y][x] == "#":
        amount_trees[4] += 1
    x = (x + 1) % width

print(amount_trees)
print(reduce(lambda x, y: x * y, amount_trees))
