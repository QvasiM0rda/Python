from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from get_data_from_xls import get_data_from_xls


class FillTable:

    def __init__(self, config: dict, table_name: str) -> None:
        self.configurations = config
        self.table = table_name
        self.fields = self.set_fields()
        self.values = get_data_from_xls(self.table)

    def set_fields(self) -> list:
        with UseDatabase(self.configurations) as cursor:
            _SQL = f'''SELECT COLUMN_NAME
                       FROM information_schema.columns
                       WHERE TABLE_NAME = "{self.table}"'''
            cursor.execute(_SQL)
            fields = ', '.join([field[0] for field in cursor.fetchall()])
            return fields

    def fill_table(self) -> None:
        with UseDatabase(self.configurations) as cursor:
            for value in self.values:
                _SQL = f'''INSERT INTO {self.table} ({self.fields})
                           VALUES ({value})'''
                cursor.execute(_SQL)
