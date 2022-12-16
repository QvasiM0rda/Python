import mysql.connector
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from get_data_from_xls import get_data_from_xls


class FillTable:

    def __init__(self, config: dict, table_name: str) -> None:
        self.configurations = config
        self.table = table_name
        self.fields = self.set_fields()
        self.values = get_data_from_xls(self.table)
        self.is_foreign_keys = False

    def set_fields(self) -> list:
        with UseDatabase(self.configurations) as cursor:
            _SQL = f'''SELECT COLUMN_NAME
                       FROM information_schema.columns
                       WHERE TABLE_SCHEMA = 'phonebook' AND TABLE_NAME = "{self.table}"'''
            cursor.execute(_SQL)
            result = cursor.fetchall()
            return ', '.join([field[0] for field in result])
    

    def fill_table(self) -> None:
        with UseDatabase(self.configurations) as cursor:
            for value in self.values:
                try:
                    _SQL = f'''INSERT INTO {self.table} ({self.fields})
                               VALUES ({value})'''
                    cursor.execute(_SQL)
                except mysql.connector.errors.IntegrityError as error:
                    print(error)
