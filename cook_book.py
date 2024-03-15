import pprint


with open('recipes.txt', 'r', encoding='utf-8') as f:
    cook_dict = {}
    name_dish = ""
    ingredients_for_dish = []
    ingredient_dict = {}
    list_keys=['ingredient_name', 'quantity', 'measure']
    while True:
        name_dish = (f.readline().strip())
        if name_dish:
            k = int(f.readline().strip())
            for i in range(k):
                list_values = (f.readline().strip()).split(' | ')
                list_values[1] = int(list_values[1])
                ingredient_dict = dict(zip(list_keys,list_values))
                ingredients_for_dish.append(ingredient_dict)
                ingredient_dict = {}
            cook_dict[name_dish] = ingredients_for_dish
            ingredients_for_dish = []
            f.readline()
        else:
            break


def get_shop_list_by_dishes(list_dishes, count_pers):
    dict_result = {}
    for el in list_dishes:
        for el_list in cook_dict[el]:
            cur_dict={}
            key_name = el_list['ingredient_name']
            cur_dict['measure'] = el_list['measure']
            cur_dict['quantity'] = el_list['quantity'] * count_pers
            if dict_result.get(key_name,0)==0:
                dict_result[key_name] = cur_dict
            else:
                dict_result[key_name]['quantity'] += cur_dict['quantity']
    return dict_result

pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Вареный картофель', 'Компот'], 3))

        

