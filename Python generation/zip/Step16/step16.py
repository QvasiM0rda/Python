from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    files = [file for file in zip_file.infolist() if not file.is_dir()]
    file = min(files, key=lambda f: (f.compress_size / f.file_size) * 100)
    print(file.filename.split('/')[-1])
    