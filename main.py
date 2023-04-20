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

def get_shop_list_by_dishes(dishes, pers_num):
    res = {}
    for dish in dishes:
        if dish in cook_book:
            for ingrid in cook_book[dish]:
                if ingrid['ingrid_name'] in res:
                    res[ingrid['ingrid_name']]['qty'] += int(ingrid['qty']) * pers_num
                else:
                    res[ingrid['ingrid_name']] = {'measure': ingrid['measure'],'qty': (int(ingrid['qty']) * pers_num)}
        else:
            print('\nНекоторых блюд нет в книге рецептов')
    print(f"\nКоличество гостей: {pers_num}\n Необходимо закупить:")
    pprint(res, indent=1, sort_dicts=False, width=88)


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

    # {
    #     'Картофель': {'measure': 'кг', 'quantity': 2},
    #     'Молоко': {'measure': 'мл', 'quantity': 200},
    #     'Помидор': {'measure': 'шт', 'quantity': 4},
    #     'Сыр гауда': {'measure': 'г', 'quantity': 200},
    #     'Яйцо': {'measure': 'шт', 'quantity': 4},
    #     'Чеснок': {'measure': 'зубч', 'quantity': 6}
    # }