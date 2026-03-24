import functools


class Logger:
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('{level}: the function {func} () is running...'.format(level=self.level, func=func.__name__))
            func(*args, **kwargs)

        return wrapper


@Logger(level='WARNNING')
def say(something):
    print('say {}!'.format(something))


if __name__ == '__main__':
    print(say.__name__)
    say('hello')
