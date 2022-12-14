from openpyxl import load_workbook


def get_data_from_xls(filename: str) -> list:
    workbook = load_workbook(filename + '.xlsx')
    worksheet = workbook.active
    result = list()
    for row in worksheet.values:
        result.append(row)
    return result
