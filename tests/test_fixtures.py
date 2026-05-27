import pytest


@pytest.fixture(autouse=True, scope="class")
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки АТ")
    yield 'Bb connection client'
    print('Закрыли соединение')


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")


@pytest.fixture(scope="function")
def users_client(settings): # фикстура может передаваться в другую фикстуру
    print("[FUNCTION] Создаем АПИ клиент на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, users_client):
        ...

    def test_user_can_create_cource(self, settings, user, users_client):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, users_client):
        ...


@pytest.fixture
def user_data(settings):
    print('Получили настройки для входа в БД')
    print("Создаём пользователя до теста (setup)")
    yield {"username": "test_user", "email": "test@example.com"}
    print("Удаляем пользователя после теста (teardown)")


def test_user_email(user_data):
    assert user_data['email'] == "test@example.com"


def test_user_name(user_data):
    assert user_data['username'] == "test_user"
