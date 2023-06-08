import pytest
from datetime import datetime


@pytest.fixture()
def test_for_class():
    yield print(f'\nСтарт теста: {datetime.now().time()}')
    print(f'\nЗавершение теста: {datetime.now().time()}')


@pytest.fixture()
def test_for_def():
    start = datetime.now()
    yield print(f'\nНачало: {start}')
    print(f'\nВремя выполнения: {datetime.now() - start}')
