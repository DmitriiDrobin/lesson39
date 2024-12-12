

def apply_all_func(int_list, *functions):
    dictres = {}
    for function in functions:
        result = function(int_list)
        dictres[function.__name__] = result
    return dictres

print(apply_all_func([6, 20, 15, 9], max, min))

print(apply_all_func([6, 20, 15, 9], len, sum, sorted))