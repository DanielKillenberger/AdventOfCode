with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")

def parse_line(line):
    dict = {}
    key_value_pairs = line.split(" ")
    for key_value_pair in key_value_pairs:
        [key, value] = key_value_pair.split(":")
        dict[key] = value
    return dict


obligotary_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def passport_is_valid(passport):
    return all(key in passport for key in obligotary_keys)


amount_valid = 0
passport = {}
for line in input:
    if not line:
        if passport_is_valid(passport):
            amount_valid += 1
        passport = {}
        continue
    passport = {**passport, **parse_line(line)}

if passport_is_valid(passport):
    amount_valid += 1


print(amount_valid)



