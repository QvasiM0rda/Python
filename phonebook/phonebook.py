from fill_table import FillTable
from get_data_from_xls import get_data_from_xls


config = {'host': '127.0.0.1',
          'user': 'brick',
          'password': '',
          'database': 'phonebook', }

positions = FillTable(config, 'positions')
print(positions.fields)
