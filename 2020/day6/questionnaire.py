with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")


total = 0
group_answers = {}
for line in input:
    if not line:
        total += len(group_answers)
        group_answers = {}
    for char in line:
        group_answers[char] = 1

total += len(group_answers)
print(total)

