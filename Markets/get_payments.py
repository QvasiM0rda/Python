from get_kbk import get_kbk

def get_tax_name(kbk: str) -> str:
    kbk_dict = get_kbk()
    for k, v in kbk_dict.items():
        if kbk in list(v):
            return k
    return False


def get_payments(file_name: str) -> dict:
    payment_dict = dict()
    with open(file_name, encoding='utf-8') as file:
        file.readline()
        for line in file:
            line = line.rstrip().split('\t')
            inn = line[0]
            tax_name = get_tax_name(line[1])
            payment = int(line[2])
            if tax_name is not False and payment > 0:
                key = inn + '/' + tax_name
                payment_dict.setdefault(key, 0)
                payment_dict[key] += payment
            
    return payment_dict
