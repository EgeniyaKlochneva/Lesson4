from functools import reduce
a = [el for el in range(100, 1001) if el % 2 == 0]

def my_func(prev_el, el):
    return prev_el * el
print(a)

print(reduce(my_func, a))