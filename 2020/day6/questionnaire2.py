with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")


total = 0
group_answers = {}
group_size = 0
for line in input:
    if not line:
        total += len(list(filter(lambda x: x == group_size, list(group_answers.values()))))
        group_answers = {}
        group_size = 0
        continue
    for char in line:
        group_answers[char] = 1 if char not in group_answers else group_answers[char] + 1
    group_size += 1

total += len(list(filter(lambda x: x == group_size, list(group_answers.values()))))


print(total)

