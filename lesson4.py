# p1.a(If 2 args)

def find_max(a, b):
    if a < b:
        return a
    elif a > b:
        return b

# p1.a(If args more than 2)


def find_max2(a, b):
    args = [a, b]
    args.sort()
    max_args = args[-1]
    return max_args


# p1.b


def find_min(a, b, c):
    args = [a, b, c]
    args.sort()
    min_args = args[0]
    return min_args
# p1.c


def my_abs(a):
    if a < 0:
        return a*(-1)
    return a


# p1.d

def find_sum(a, b):
    print(a + b)


# p1.e
def print_sign(a):
    if a == 0:
        print("Error")
    elif a > 0:
        print("Positive number")
    else:
        print("Negative number")
