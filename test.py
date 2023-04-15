def print_square(size, end_char=None):

    if size == 0:
        if end_char is not None:
            print(end_char)
        return

    print('*' * size)
    print_square(size - 1, end_char)

    if end_char is not None:
        print(end_char)
