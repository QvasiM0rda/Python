# Получаем целое число из стандартного потока ввода.
# Обратите внимание, что через stdin мы всегда передаем и принимаем строки,
# поэтому нам нужно применять функцию int(), чтобы сделать из них числа.
number = int(input())

# Напишите ваш код тут.
int_part = number // 2
remainder = number % 2
print(int_part, remainder)