from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(","))

max_len_ingredient = len(max(order, key=len))
max_len_amount = len(str(max(order.values())))
total_sum = 0

for ingredient, amount in sorted(order.items()):
    print(f"{ingredient.ljust(max_len_ingredient)} x {amount}")
    total_sum += (ingredients[ingredient] * amount)
print("-" * max(max_len_ingredient + max_len_amount + 3, 7 + len(str(total_sum))))
print(f"ИТОГ: {total_sum}р")
