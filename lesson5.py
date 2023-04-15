#
def uni_elements(*args):
    uni_set = set(args)
    return list(uni_set)


def kwargs_func(**kwargs):
    args_count = len(kwargs)
    user_type = kwargs.get("user_type", "Student")
    print("Number of arguments passed:", args_count)
    print("User type:", user_type)


def example_func(arg1, arg2, arg3=None, arg4=None, arg5="value", arg6="value2"):
    pass

def out_func(num):
    def in_func(x):
        return num * x
    return in_func

res_func = out_func(1)
res = res_func(2)

print(res)