from openpyxl import load_workbook
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from fill_table import fill_table
from get_data_from_xls import get_data_from_xls


config = {'host': '127.0.0.1',
          'user': 'rustam',
          'password': '',
          'database': 'phonebook',}

fields = fill_table(config, 'positions', [])
string = ', '.join(fields)


print(string)
