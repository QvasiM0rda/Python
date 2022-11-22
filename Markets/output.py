def output(payments: dict, file_name: str) -> 'file':
    with open(file_name, 'w', encoding='utf-8') as file:
        for k, v in sorted(payments.items()):
            print(*k.split('/'), v, file=file)
