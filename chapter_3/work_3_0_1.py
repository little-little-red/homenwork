# 参数补足
def paprmeter_supplementation(to_param, param={}):

    def wrapper(func):

        def inner_wrapper(t):
            return func(**{to_param: t}, **param)

        return inner_wrapper

    return wrapper


# 计时器


def timer(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Time taken to execute the function: {end - start}")
        return result

    return wrapper
