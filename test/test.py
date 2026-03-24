import inspect


# Define a class with a method
class MyClass:
    def my_method(self):
        pass


# Define a standalone function
def my_function():
    pass


# Function to determine the class name or module name
def get_func_info(func):
    if inspect.ismethod(func):
        cls_name = func.__self__.__class__.__name__
    elif inspect.isfunction(func):
        cls_name = func.__module__
    else:
        cls_name = None
    return cls_name


# Test cases
if __name__ == "__main__":
    # Create an instance of MyClass
    my_instance = MyClass()

    # Get the method from the instance
    method = my_instance.my_method

    # Get the function
    function = my_function

    # Test with the method
    method_info = get_func_info(method)
    print(f'Method Class Name: {method_info}')  # Should print: MyClass

    # Test with the function
    function_info = get_func_info(function)
    print(f'Function Module Name: {function_info}')  # Should print: __main__