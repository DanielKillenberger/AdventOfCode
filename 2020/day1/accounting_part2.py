with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")

input = list(map(int, input))

input.sort()

comparisons = 0
for i in range(len(input)):
    for j in range(i + 1, len(input)):
        comparisons += 1

        higher = input[j]
        lower = input[i]
        value_3 = 2020 - higher - lower
        if value_3 <= 0:
            print("No 3 numbers add up to 2020")
            exit(0)
        if value_3 in input and value_3 != higher and value_3 != lower:
            print(higher)
            print(lower)
            print(value_3)
            print(higher*lower*value_3)
            print(comparisons)
            exit(0)








