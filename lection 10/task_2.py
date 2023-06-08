# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_1():
    assert all_division(-1, 1) == -1, 'чет то'


def test_2():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)


@pytest.mark.smoke
def test_3():
    assert all_division(2, 1) == 3, 'Неправильный ОР'


@pytest.mark.skip('Скип по задаче')
def test_31():
    assert all_division(100, 10) == 10, 'ok'


def test_5():
    assert all_division(103.3, 2) == 51.65, 'ok'
