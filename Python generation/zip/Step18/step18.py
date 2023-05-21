from zipfile import ZipFile
from datetime import datetime

with ZipFile("workbook.zip") as zip_file:
    files = [f for f in zip_file.infolist() if not f.is_dir()]
    
    for file in sorted(files, key=lambda f: f.filename.split('/')[-1]):
        
        print(f"""{file.filename.split('/')[-1]}
  Дата модификации файла: {datetime(*file.date_time)}
  Объем исходного файла: {file.file_size} байт(а)
  Объем сжатого файла: {file.compress_size} байт(а)
""")
