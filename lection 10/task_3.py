# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('x, y, res',
                         [
                             pytest.param(5, 2, 2.5, marks=pytest.mark.smoke),
                             pytest.param(1, 1, 1, marks=pytest.mark.skip('skipped by task ..'))
                         ])
def test_31(x, y, res):
    assert all_division(x, y) == res


