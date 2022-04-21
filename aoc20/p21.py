import collections
from functools import reduce
import operator
import re
from dataclasses import dataclass

from aoc20 import utils


@dataclass
class Product:
    ingredients: set[str]
    allergens: set[str]


def possible_allergic_ingredients(products: list[Product]) -> dict[str, set[str]]:
    d = collections.defaultdict(list)
    for product in products:
        for allergen in product.allergens:
            d[allergen].append(product.ingredients)
    return {k: reduce(operator.and_, v) for k, v in d.items()}


def count_non_allergic_ingredients(products: list[Product]) -> int:
    allergic = possible_allergic_ingredients(products)
    all_allergic = reduce(operator.or_, allergic.values())
    all_ingredients = reduce(operator.or_, (p.ingredients for p in products))
    non_allergic = all_ingredients - all_allergic
    c = collections.Counter(
        i for p in products for i in p.ingredients if i in non_allergic
    )
    return sum(c.values())


def dangerous_ingredients(products: list[Product]) -> str:
    allergic = possible_allergic_ingredients(products)
    result: dict[str, str] = {}
    for _ in range(len(allergic)):
        allergen, ingredient = next(
            (k, list(v)[0]) for k, v in allergic.items() if len(v) == 1
        )
        result[allergen] = ingredient
        for v in allergic.values():
            v.discard(ingredient)
    return ",".join(
        v for k, v in sorted(((k, v) for k, v in result.items()), key=lambda x: x[0])
    )


def parse_input(lines: list[str]) -> list[Product]:
    result = []
    for line in lines:
        if m := re.match(r"(.*) \(contains (.*)\)", line):
            ingredients = set(m.group(1).split(" "))
            allergens = set(m.group(2).split(", "))
            result.append(Product(ingredients, allergens))
    return result


def main() -> None:
    products = parse_input(utils.read_input_lines(__file__))
    print(count_non_allergic_ingredients(products))
    print(dangerous_ingredients(products))


if __name__ == "__main__":
    main()
