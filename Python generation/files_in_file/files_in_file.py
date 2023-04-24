def get_size_in_bytes(s, u):
    units = {'B': 1,
             'KB': 1024,
             'MB': 1024 ** 2,
             'GB': 1024 ** 3}
    return s * units[u]


def get_size_in_units(s):
    if s < 1024:
        u = str(s) + ' B'
    elif s < 1024 ** 2:
        u = str(round(s / 1024)) + ' KB'
    elif s < 1024 ** 3:
        u = str(round(s / 1024 ** 2)) + ' MB'
    else:
        u = str(round(s / 1024 ** 3)) + ' GB'
    return u


extensions = dict()
with open("files.txt", encoding="utf-8") as files:
    for file in files:
        name, size, unit = file.split()
        ext = name[name.rfind('.') + 1:]
        size = get_size_in_bytes(int(size), unit)
        extensions.setdefault(ext, [])
        extensions[ext].append([name, size])

for ext, names in sorted(extensions.items()):
    total_size = 0
    for name in sorted(names):
        total_size += name[1]
        print(name[0])
    print(f"""----------
Summary: {get_size_in_units(total_size)}
""")
