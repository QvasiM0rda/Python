from zipfile import ZipFile
from datetime import datetime

with ZipFile("workbook.zip") as zip_file:
    files = [file.filename.split('/')[-1] for file in zip_file.infolist()
             if datetime(*file.date_time) > datetime(2021, 11, 30, 14, 22, 00) and not file.is_dir()]
    
    for file in sorted(files):
        print(file)
    