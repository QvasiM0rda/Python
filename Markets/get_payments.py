from get_kbk import get_kbk

def get_tax_name(kbk: str) -> str:
    kbk_dict = get_kbk()
    for k, v in kbk_dict.items():
        print(kbk, kbk in list(v))


def get_payments(file_name: str) -> dict:
    with open(file_name, encoding='utf-8') as file:
        file.readline()
        for i in range(1):
            line = file.readline().rstrip().split('\t')
            get_tax_name(line[1])
