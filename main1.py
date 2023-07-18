# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 

# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from typing import Callable
import random

def main_my(func: Callable):
    NUM_MIN = 1
    NUM_MAX = 100
    COUNT_MIN = 1
    COUNT_MAX = 10

    def wrapper(number1, popitka1, *args, **kwargs):
        if number1 < NUM_MIN or number1 > NUM_MAX:
            number1 = random.randint(NUM_MIN, NUM_MAX)
            print(number1)
        if popitka1 < COUNT_MIN or popitka1 > COUNT_MAX:
            popitka1 = random.randint(COUNT_MIN, COUNT_MAX)
            print(popitka1)

        result = func(number1, popitka1, *args, **kwargs)
        return result
    
    return wrapper


@main_my
def game(number, popitka):
    for _ in range(popitka):
        num = int(input('введите число: '))

        if num == number:
            print('число угадано')
            break
        elif num > number:
            print('ввденное число больше')
        else:
            print('введенное число меньше')
    else:
        print('попытки закончились')


game(50, 3)


# from typing import Callable
# import random

# def main_my(number: int, popitka: int) -> Callable[[], None]:

#     def game():
#         for i in range(popitka):
#             num = int(input('введите число: '))

#             if num == number:
#                 print('число угадано')
#                 break
#             elif num > number:
#                 print('ввденное число больше')
#             else:
#                 print('введенное число меньше')
#         else:
#             print('попытки закончились')
        

#     return game

# if __name__ == '__main__':
#     number = random.randint(1, 100)
#     count_popitka = random.randint(1, 10)

#     result = main_my(number, count_popitka)
#     result()


