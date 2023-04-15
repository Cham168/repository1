def out_func(num):
    def in_func(x):
        return num * x
    return in_func

res_func = out_func(1)
res = res_func(2)

print(res)