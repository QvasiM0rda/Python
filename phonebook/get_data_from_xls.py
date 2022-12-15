from openpyxl import load_workbook


def get_data_from_xls(filename: str) -> list:
    workbook = load_workbook(filename + '.xlsx')
    worksheet = workbook.active
    result = []
    for row in worksheet.values:
        string = ''
        for value in row:
            string += "'" + value + "', "
        result.append(string[:-2])
    
    return result
