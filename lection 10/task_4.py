# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


@pytest.mark.usefixtures("test_for_class")
class TestTrue:

    def test1(self):
        time.sleep(1)
        return

    def test2(self):
        time.sleep(1)
        return


def test3(test_for_def):
    time.sleep(1)
    return
