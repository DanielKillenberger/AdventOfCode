with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")


def parse_line(line):
    dict = {}
    key_value_pairs = line.split(" ")
    for key_value_pair in key_value_pairs:
        [key, value] = key_value_pair.split(":")
        dict[key] = value
    return dict


def is_int(v):
    try:
        int(v)
        return True
    except ValueError:
        return False


def is_hex(v):
    try:
        int(v, 16)
        return True
    except ValueError:
        return False


def byr(value):
    return 1920 <= int(value) <= 2002


def iyr(value):
    return 2010 <= int(value) <= 2020


def eyr(value):
    return 2020 <= int(value) <= 2030


def hgt(value):
    if value.endswith("cm"):
        return 150 <= int(value.replace("cm", "")) <= 193
    if value.endswith("in"):
        return 59 <= int(value.replace("in", "")) <= 76
    return False


def hcl(value):
    if value.startswith("#"):
        return is_hex(value.replace("#", ""))
    return False


def ecl(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid(value):
    return is_int(value) and len(value) == 9


validations = {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}


def passport_is_valid(passport):
    return all(key in passport and validations[key](passport[key]) for key in validations.keys())


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
