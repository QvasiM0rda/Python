from datetime import date

# Создаем переменную now типа date.
# Переменная today хранит текущую дату.
today = date.today()

print("{:%d.%m.%Y}".format(today))
