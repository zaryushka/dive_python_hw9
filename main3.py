# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable

def count(num: int=1):
    def deco(func: Callable):
        my_dict = {}
        def wrapper(*args, **kwargs):
            for i in range(num):
                result = func(*args, **kwargs)
                my_dict[i] = result
            return my_dict

        return wrapper
    return deco

@count(5)
def add_nums(num1, num2, *args, **kwargs):
    return num1 + num2

if __name__ == '__main__':
    result = add_nums(54, 45)
    print(result)