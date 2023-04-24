from random import choice, sample, shuffle

def pass_gen(pass_length, pass_chars):
    shuffle(pass_chars)
    password = ''
    for i in range(pass_length):
        password += choice(pass_chars)[i]
    return password


digits = '1234567890'
letters = 'abcdefghijklmnopqrstuvwxyz'
punctuations = '!@#$%^&*()+-=_'

chars = []

length = int(input('Введите количество символов: '))
is_digits = input('Пароль должен содержать цифры? (да/нет) ') == 'да'
is_upper_letters = input('Пароль должен содержать прописные буквы? (да/нет) ') == 'да'
is_lower_letters = input('Пароль должен содержать строчные буквы? (да/нет) ') == 'да'
is_punctuations = input('Пароль должен содержать знаки пунктуации? (да/нет) ') == 'да'
is_ambigious = input('Пароль должен содержать неоднозначные символы (i l 1 L, o 0 O)? (да/нет) ') == 'да'

if is_digits:
    chars.append(sample(digits, length))
if is_upper_letters:
    chars.append(sample(letters.upper(), length))
if is_lower_letters:
    chars.append(sample(letters, length))
if is_punctuations:
    chars.append(sample(punctuations, length))
if not is_ambigious:
    ambigious_symbols = ['i', 'l', '1', 'L', 'o', '0', 'O']
    for symbol in ambigious_symbols:
        if symbol in chars:
            chars.pop(symbol)

print(pass_gen(length, chars))
