import re
from functools import reduce

with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")

rules = {}


def parse_rule(rule_string):
    [bag_name, children_string] = rule_string.split("contain")
    bag_name = bag_name.replace(" bags ", "")
    if "no other bags" in children_string:
        children = None
    else:
        children_strings = list(map(lambda child: re.sub(" bag(s)?", "", child).replace(".", "").strip(), children_string.split(",")))
        children = list(map(lambda child_string: {"amount": int(child_string[0]), "name": child_string[2:]}, children_strings))
    return {"name": bag_name, "children": children}


def get_direct_children_bags(rules, bag_name):
    return [rules[child["name"]] for child in rules[bag_name]["children"]]


def get_all_children_bags(rules, bag):
    children = {}
    open_list = bag["children"]

    while open_list:
        current_bag = open_list.pop()
        open_list += [child for child in get_direct_children_bags(rules, bag["name"]) if child["name"] not in children]
        if current_bag["name"] not in children:
            children[current_bag["name"]] = current_bag
    return children


for rule_string in input:
    rule = parse_rule(rule_string)
    rules[rule["name"]] = rule


all_children = get_all_children_bags(rules, rules["shiny gold"])

print(len(all_children))




