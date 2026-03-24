import functools


def decorator2(num):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            decorator2
            :param args:
            :param kwargs:
            :return:
            """
            max_retry_num = 3
            retry_num = 1
            print('decorator2 start')
            while retry_num <= max_retry_num:
                func(*args, **kwargs)
                retry_num += 1
            print('decorator2 end')

        return wrapper

    return decorator


def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        decorator1 doc
        :param args:
        :param kwargs:
        :return:
        """
        print('decorator1 start')

        func(*args, **kwargs)
        print('decorator1 end')

    return wrapper


@decorator1
@decorator2(1000)
def get_response(str_list):
    """
    get_response 123
    :param str_list:
    :return:
    """
    print(str_list)


# get_response(['a', 'b'])


print(get_response.__name__)
print(get_response.__doc__)
