# Присваиваем каждой переменной своё значение,
# предварительно преобразовав его к целому числу.
bread = int(input())
milk = int(input())
eggs = int(input())

# Считаем среднее и выводим результат.
avg_price = int((bread + milk + eggs) / 3)
print(avg_price)