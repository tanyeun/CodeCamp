import time


def pair_equal_non_order(pair1, pair2):
    if pair1[0] == pair2[0] and pair1[1] == pair2[1]:
        return True
    elif pair1[0] == pair2[1] and pair1[1] == pair2[0]:
        return True
    else:
        return False


def timeit(func):
    """
    Decorator for measuring function's running time.
    """
    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.2f ns."
              % (func.__qualname__, time.time()*pow(10, 9) - start_time*pow(10, 9)))
        return result

    return measure_time
