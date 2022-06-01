from time import perf_counter_ns

def repeat_ten_times(f):
    def f2(*args, **kargs):
        for i in range(10):
            f(*args, **kargs)
    return f2

def time_execution(f):
    def f2(*args, **kargs):
        start = perf_counter_ns()
        f(*args, **kargs)
        stop = perf_counter_ns()
        print(stop-start)
    return f2


class Great:

    def __init__(self, name):
        self._name = name

    def say_hello(self):
        print(f'Hello {self._name}')

    @repeat_ten_times
    @time_execution
    def say_good(self, time_of_day):
        print(f'Good {time_of_day} {self._name}')


def main():
    saluti = Great("Filippo")
    saluti.say_good("morning")
    saluti.say_hello()

main()