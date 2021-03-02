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
    """Random function wrapped by @calculate_time"""
    time.sleep(2)


if __name__ == '__main__':
    random_func()
