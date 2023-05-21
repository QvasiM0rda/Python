from zipfile import ZipFile

with ZipFile("test.zip") as zip_file:
    info = zip_file.infolist()
    before_compress = sum(file.file_size for file in info)
    after_compress = sum(file.compress_size for file in info)
    print(f"Объем исходных файлов: {before_compress} байт(а)")
    print(f"Объем сжатых файлов: {after_compress} байт(а)")