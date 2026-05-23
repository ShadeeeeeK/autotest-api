import pytest


@pytest.mark.xfail(reason="В приложении есть баг")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Баг исправлен, но на тесте все ещё висит маркировка xfail")
def test_without_bug():
    ...


@pytest.mark.xfail(reason="Внешний сервис временно недоступен")
def test_external_services_is_unavailable():
    assert 1 == 2
