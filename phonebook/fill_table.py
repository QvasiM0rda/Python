from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError


class FillTable:

    def __init__(self, config: dict, table_name: str) -> None:
        self.configurations = config
        self.table = table_name
        self.fields = self.get_fields()

    def get_fields(self) -> list:
        with UseDatabase(self.configurations) as cursor:
            _SQL = f'''SELECT COLUMN_NAME
                       FROM information_schema.columns
                       WHERE TABLE_NAME = "{self.table}"'''
            cursor.execute(_SQL)
            fields = ', '.join([field[0] for field in cursor.fetchall()])
            return fields

    def fill_table(self, values: dict) -> None:
        with UseDatabase(self.configurations) as cursor:
            _SQL = f'''INSERT INTO {self.table} ({self.fields})
                       VALUES ({values.keys(), values.values()})'''
            cursor.execute(_SQL)
