# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json

def save_json(func):


    with open('file_json.json', 'r', encoding='utf-8') as f:
        my_dict = json.load(f)

    def wrapper(*args, **kwargs):
        my_dict.update({'args': args, **kwargs})
        result = func(*args, **kwargs)
        my_dict.update({f'{args[0]} + {args[1]} result': result})


        with open('file_json.json', 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)
        return result
    return wrapper



@save_json
def add_nums(num1, num2, *args, **kwargs):
    return num1 + num2

if __name__ == '__main__':
    result = add_nums(54, 45, 7, 1, x = False, www = True, z = 'stroka', y = 145)
    print(result)