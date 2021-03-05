import time


def calculate_time(func):
    """Calculates run time of function"""

    def wrapper():
        x = time.time()
        func()
        print(time.time() - x)
    return wrapper


@calculate_time
def random_func():
    time.sleep(2)


if __name__ == '__main__':
    random_func()
