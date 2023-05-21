import csv

with open("prices.csv", encoding="utf-8") as file:
    data = csv.reader(file, delimiter=";")
    products = next(data)
    stores = []
    min_price = 0
    for prices in data:
        store_min_price = min(prices[1:], key=lambda price: int(price))
        min_price = min(min_price, store_min_price) if min_price != 0 else store_min_price
        stores.append([prices[0], products[prices.index(store_min_price)], store_min_price])

cheapest_product = min(list(filter(lambda store: store[2] == min_price, stores)),
                       key=lambda product: product[1])
print(f'{cheapest_product[1]}: {cheapest_product[0]}')
