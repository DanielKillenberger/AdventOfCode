import re

with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")

rules = {}


def parse_rule(rule_string):
    [bag_name, children_string] = rule_string.split("contain")
    bag_name = bag_name.replace(" bags ", "")
    if "no other bags" in children_string:
        children = None
    else:
        children_strings = list(
            map(lambda child: re.sub(" bag(s)?", "", child).replace(".", "").strip(), children_string.split(",")))
        children = list(
            map(lambda child_string: {"amount": int(child_string[0]), "name": child_string[2:]}, children_strings))
    return {"name": bag_name, "children": children}


for rule_string in input:
    rule = parse_rule(rule_string)
    rules[rule["name"]] = rule


def amount_bags_in_bag(rules, bag_name):
    children = rules[bag_name]["children"]
    amount = 0
    if children:
        for child in children:
            amount += child["amount"] + child["amount"] * amount_bags_in_bag(rules, child["name"])
    return amount


print(amount_bags_in_bag(rules, "shiny gold"))
