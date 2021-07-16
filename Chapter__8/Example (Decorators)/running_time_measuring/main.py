class my_timer(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        import time
        t1 = time.time()
        result = self.original_function(*args, **kwargs)
        t2 = time.time()
        print(f"{self.original_function.__name__}() function ran in: {t2 - t1} sec")
        return result

@my_timer
def my_loop():
    sum = 0
    for i in range(10000000):
        sum += i*i
    print(sum)

my_loop()
