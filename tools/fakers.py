import time

def get_random_email():
    return f"test.{time.time()}@mail.ru"

print(get_random_email())