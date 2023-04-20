from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingrid_count = int(file.readline().strip())
        ingrids = []
        for _ in range(ingrid_count):
            ingrid_name, qty, measure = file.readline().strip().split(' | ')
            ingrids.append({
                'ingrid_name': ingrid_name,
                'qty': qty,
                'measure': measure
            })
        file.readline()
        cook_book[dish_name] = ingrids

    pprint(cook_book, indent=2, sort_dicts=False, width=144, compact=False)