import math
from functools import reduce

with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")


def find_index(dir_string, range):
    for dir in dir_string:
        if dir == "F":
            range[1] = range[1] - math.ceil((range[1] - range[0]) / 2)
        if dir == "B":
            range[0] = range[0] + math.ceil((range[1] - range[0]) / 2)
        if range[0] == range[1]:
            return range[0]


def find_row(value):
    return find_index(value, [0, 127])


def find_column(value):
    return find_index(value.replace("R", "B").replace("L", "F"), [0, 7])


rows = [x[:] for x in [[0] * 8] * 128]

for boarding_pass in input:
    row_string = boarding_pass[0:7]
    column_string = boarding_pass[7:]
    row = find_row(row_string)
    column = find_column(column_string)
    rows[row][column] = 1


for row_number in range(len(rows)):
    row = rows[row_number]
    if reduce(lambda x, y: x + y, row) == 7:
        column_number = row.index(0)
        print(row_number, column_number)
        print(row_number*8 + column_number)
        exit(0)
