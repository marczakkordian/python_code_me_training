def uppercase_decorator(function_name):
    def wrapper():
        txt = str(function_name)
        return txt.upper()
    return wrapper()


@uppercase_decorator
def return_string():
    my_string = 'my_string'
    return my_string


print(return_string())
