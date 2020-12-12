import re

with open("input.txt", "r") as input_file:
    input = input_file.read().split("\n")

rules = []


def parse_rule(rule_string):
    [bag_name, children_string] = rule_string.split("contain")
    bag_name = bag_name.replace(" bags ", "")
    if "no other bags" in children_string:
        children = None
    else:
        children_strings = list(map(lambda child: re.sub(" bag(s)?", "", child).replace(".", "").strip(), children_string.split(",")))
        children = list(map(lambda child_string: {"amount": int(child_string[0]), "name": child_string[2:]}, children_strings))
    return {"name": bag_name, "children": children}


def bag_contains_bag(rule, bag_name):
    if not rule["children"]:
        return False
    children = rule["children"]
    return bool(next((child for child in children if child["name"] == bag_name), None))


def get_direct_parent_bags(rules, bag_name):
    return list(filter(lambda rule: bag_contains_bag(rule, bag_name), rules))


def get_all_parents_bags(rules, bag_name):
    parents = {}
    open_list = get_direct_parent_bags(rules, bag_name)

    while open_list:
        current_bag = open_list.pop()
        open_list += get_direct_parent_bags(rules, current_bag["name"])
        if current_bag["name"] not in parents:
            parents[current_bag["name"]] = current_bag

    return list(parents.values())



bags_with_shiny_bags = []

for rule_string in input:
    rule = parse_rule(rule_string)
    rules.append(rule)

parents = list(map(lambda rule: rule["name"], get_all_parents_bags(rules, "shiny gold")))

print(parents)
print(len(parents))



