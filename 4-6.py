from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)


a = 0
for el in cycle("ABCDE"):
    if a > 10:
        break
    print(el)
    a += 1
