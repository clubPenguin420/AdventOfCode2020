import re


def parse_line(line):
    R = r"(.*) \(contains (.*)\)"
    match = re.match(R, line)
    if match is None:
        return None

    ingredients, allergens = match[1], match[2]

    ingredients = ingredients.split()
    allergens = allergens.split(", ")

    return ingredients, allergens


def read():
    data = []

    with open("Inputs.dat", "r") as f:
        for line in f:
            line = line.strip()
            line = parse_line(line)
            if line is None:
                break
            data.append(line)

    return data


def part1():
    data = read()

    all_ingredients = set()
    all_allergens = set()
    for ingredients, allergens in data:
        all_ingredients.update(set(ingredients))
        all_allergens.update(set(allergens))

    allergens_dict = {allergen: all_ingredients.copy() for allergen in all_allergens}

    for ingredients, allergens in data:
        for allergen in allergens:
            allergens_dict[allergen].intersection_update(set(ingredients))

    all_non_allergenics = all_ingredients.copy()
    for ingredients in allergens_dict.values():
        all_non_allergenics.difference_update(ingredients)

    total = 0
    for ingredients, _ in data:
        for ingredient in ingredients:
            if ingredient in all_non_allergenics:
                total += 1
    print(total)

    return allergens_dict


def is_solved(allergens_dict):
    for ingredients in allergens_dict.values():
        if len(ingredients) == 0:
            raise Exception("unsolvable")
        elif len(ingredients) > 1:
            return False
    return True

print(part1())