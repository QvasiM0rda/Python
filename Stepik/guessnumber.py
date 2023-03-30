import random


def is_valid(value, border=100):
    return value.isdigit() and 1 <= int(value) <= border


try_again = 'да'
print('Добро пожаловать в числовую угадайку!')

while try_again.lower() in ['да', 'yes']:
    right_border = int(input('Введите правую границу: '))
    random_number = random.randint(1, right_border)
    try_count = 0

    while True:
        user_input = input(f'Введите целое число от 1 до {right_border}: ')
        if not is_valid(user_input):
            print(f'То, что вы ввели, не является числом от 1 до {right_border}')
            continue
        else:
            number = int(user_input)
            try_count += 1
        if number < random_number:
            print('Ваше число меньше загаданного, попробуйте ещё раз.')
        elif number > random_number:
            print('Ваше число больше загаданного, попробуйте ещё раз.')
        else:
            print(f'Вы угадали! Вам потребовалось {try_count} попыток!')
            break
    try_again = input('Сыграем ешё? ')

print('Спасибо за игру, возвращайтесь!')
