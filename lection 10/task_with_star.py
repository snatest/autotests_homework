# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.fixture
def get_args(request):
    for mark in request.node.iter_markers("id_check"):
        return print(', '.join(str(obj) for obj in mark.args))


@pytest.mark.id_check(1, 2, 3)
def test(get_args):
    return



