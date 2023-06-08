# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    abc = string.ascii_lowercase
    lenght = range(1, 16)
    while True:
        first_word = ''.join(random.choices(abc, k=random.choice(lenght)))
        second_word = ''.join(random.choices(abc, k=random.choice(lenght)))
        yield f'{first_word} {second_word}'


gen = generate_random_name()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
