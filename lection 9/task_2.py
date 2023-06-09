# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import time

def func_log(file_log='log.txt'):
    def obertka(func):
        def wrapper_func():
            func()
            log_datetime = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
            wrapper_func.__name__ = func.__name__
            wrapper_func.__doc__ = func.__doc__
            with open(file_log, 'a', encoding='utf-8') as flog:
                flog.write(f'{wrapper_func.__name__} вызвана {log_datetime}\n')
        return wrapper_func

    return obertka


#@func_log()
def func2():
    """ тут описание 1"""
    print('зовем без декоратора')
    return


func2()
help(func2)


@func_log('func3.txt')
def func2():
    """ тут описание 2"""
    time.sleep(1)
    return print('зовем с декоратором')


func2()
func2()
func2()
func2()
func2()

help(func2)
