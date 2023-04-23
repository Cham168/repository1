import random
import string
import time

PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))

def sum_int_list(lst):
    result = 0
    for item in lst:
        if isinstance(item, int):
            result += item
        elif isinstance(item, list):
            result += sum_int_list(item)
    return result


def cycle_words(words_list, num):
    if num <= 0:
        return []
    cycle_list = []
    for i in range(num):
        cycle_list.append(words_list[i % len(words_list)])
    return cycle_list


def word_checker(password):
    if len(password) != len(PASSWORD):
        return False

    for i in range(len(password)):
        if password[i] != PASSWORD[i]:
            return False
        time.sleep(0.1)

def password_checker(password):
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return


        time.sleep(0.1)