import time


def calculate_time(func):
    """Calculates run time of function"""

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return wrapper


@calculate_time
def random_func():
    time.sleep(2)

