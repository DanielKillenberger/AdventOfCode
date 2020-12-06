with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")

input = list(map(int, input))

input.sort()
print(input)


highest_index = len(input) - 1
lowest_index = 0
highest = input[highest_index]
lowest = input[lowest_index]
comparisons = 0
while highest + lowest != 2020:
    comparisons += 1
    if highest_index <= lowest_index:
        print("No numbers add to 2020")
        break
    if highest + lowest > 2020:
        highest_index -= 1
    if highest + lowest < 2020:
        lowest_index += 1
    highest = input[highest_index]
    lowest = input[lowest_index]

print(lowest)
print(highest)
print(lowest*highest)
print(comparisons)




