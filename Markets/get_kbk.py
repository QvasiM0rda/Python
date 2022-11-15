def get_kbk() -> dict:
    '''Формирует словарь из текстового файла, содержащего сокращенные наименования налогов и соответствующих им КБК.
Ключ словаря - наименование налога, значение - список КБК.'''
        
    kbk_dict = dict()
    with open('kbk.txt', encoding='utf-8') as kbk_file:
        kbk_file.readline()
        for line in kbk_file:
            line = line.rstrip().split('\t')
            name = line[1]
            kbk = line[:13] + '0' + line[14:]
            kbk_dict.setdefault(name, [])
            kbk_dict[name].append(kbk)
    
    return kbk_dict
