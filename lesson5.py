
#Unicue elements
def uni_elements(*args):
    uni_set = set(args)
    return list(uni_set)


#kwargs
def kwargs_func(**kwargs):
    args_count = len(kwargs)
    user_type = kwargs.get("user_type", "Student")
    print("Number of arguments passed:", args_count)
    print("User type:", user_type)


#More elements
def example_func(arg1, arg2, arg3=None, arg4=None, arg5="value", arg6="value2"):
    pass


#Inner function
def out_func(num):
    def in_func(x):
        return num * x
    return in_func


res_func = out_func(5)
res = res_func(2)

print(res)


# Исправить на квадрат
def print_square(size, end_char=None):

    if size == 0:
        if end_char is not None:
            print(end_char)
        return

    print('*' * size)
    print_square(size - 1, end_char)

    if end_char is not None:
        print(end_char)
