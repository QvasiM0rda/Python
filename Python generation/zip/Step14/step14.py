from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    files = len([f for f in zip_file.infolist() if not f.is_dir()])
    print(files)
