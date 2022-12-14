from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError


def fill_table (config: dict, table_name: str, values: list) -> None:
    with UseDatabase(config) as cursor:
        _SQL = f'''SELECT COLUMN_NAME
                  FROM information_schema.columns
                  WHERE TABLE_NAME = "{table_name}"'''
        cursor.execute(_SQL)
        fields = cursor.fetchall()
    return fields
