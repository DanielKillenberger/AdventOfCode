with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")


passwords = list(map(lambda line: [list(map(int, line.split(" ")[0].split("-"))), line.split(" ")[1][0], line.split(" ")[2]], input))

valid = 0
for password in passwords:
    indexes = list(map(lambda x: x - 1, password[0]))
    password_string = password[2]
    char = password[1]
    if password_string[indexes[0]] != password_string[indexes[1]]:
        if char == password_string[indexes[0]] or char == password_string[indexes[1]]:
            valid += 1

print(valid)
