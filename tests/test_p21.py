from aoc20.p21 import parse_input, count_non_allergic_ingredients, dangerous_ingredients


def test_example():
    data = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip().splitlines()
    assert count_non_allergic_ingredients(parse_input(data)) == 5


def test_dangerous():
    data = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".strip().splitlines()
    assert dangerous_ingredients(parse_input(data)) == "mxmxvkd,sqjhc,fvjkl"
