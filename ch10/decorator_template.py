from functools import wraps

def decorator_name(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        #  1. Код, который будет исполняться ДО ВЫЗОВА декорируемой функции

        #  2. Вызов декорируемой функции и возврат полученных от неё результатов
        return func(*args, **kwargs)

        #  3. Код, который будет выполняться ВМЕСТО вызова декорируемой функции
    wrapper.__name__ = func.__name__
    return wrapper
