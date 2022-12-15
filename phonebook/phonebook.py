from fill_table import FillTable


config = {'host': '127.0.0.1',
          'user': 'rustam',
          'password': '',
          'database': 'phonebook', }

table = FillTable(config, 'positions')
table.fill_table()
