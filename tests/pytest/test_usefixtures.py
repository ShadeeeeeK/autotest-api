import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из БД")


@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в БД")


@pytest.mark.usefixtures('clear_books_database', 'fill_books_database')
class TestLibrary:
    def test_read_book_from_library(self):
        print("Я читаю книгу")

    def test_delete_book_from_library(self):
        print("Я удаляю книгу")

@pytest.fixture(scope="session")
def session_fixture():
    print("\n[SETUP] session_fixture")
    yield
    print("\n[TEARDOWN] session_fixture")

@pytest.fixture(scope="module")
def module_fixture():
    print("\n[SETUP] module_fixture")
    yield
    print("\n[TEARDOWN] module_fixture")

@pytest.fixture(scope="function")
def function_fixture():
    print("\n[SETUP] function_fixture")
    yield
    print("\n[TEARDOWN] function_fixture")

def test_one(session_fixture, module_fixture, function_fixture):
    print("Executing test_one")

def test_two(session_fixture, module_fixture, function_fixture):
    print("Executing test_two")

class TestClass:
    def test_three(self, session_fixture, module_fixture, function_fixture):
        print("Executing test_three")

    def test_four(self, session_fixture, module_fixture, function_fixture):
        print("Executing test_four")
