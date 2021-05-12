import time


def time_passed(func):
    def nested():
        start = time.process_time()
        func()
        stop = time.process_time()
        result = stop - start
        print(result)
    return nested()


@time_passed
def example_function():
    print('Start')
    time.sleep(10)
    print('End')


example_function()
