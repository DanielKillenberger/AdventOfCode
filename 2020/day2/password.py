with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")


passwords = list(map(lambda line: [list(map(int, line.split(" ")[0].split("-"))), line.split(" ")[1][0], line.split(" ")[2]], input))

valid = 0
for password in passwords:
    count_letter = password[2].count(password[1])
    if password[0][0] <= count_letter <= password[0][1]:
        valid += 1

print(valid)
