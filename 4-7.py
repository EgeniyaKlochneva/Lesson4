def fact(n):
    temp = 1
    for i in range(1, n + 1):
        temp *= i
        yield temp


n = int(input("Введите число: "))
for el in fact(n):
    print(el)
