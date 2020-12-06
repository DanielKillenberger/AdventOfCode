with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")

width = len(input[0])
amount_trees = 0
x = 0
for y in range(len(input)):
    if input[y][x] == "#":
        amount_trees += 1
    x = (x + 3) % width

print(amount_trees)
