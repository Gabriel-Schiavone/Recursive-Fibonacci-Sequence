import time


def func(x, y):
    time.sleep(1)
    print(x)
    x = x + y
    return func(y, x)


func(1, 1)
