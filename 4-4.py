before_list = [1, 3, 5, 3, 1, 6, 8, 4, 7, 5, 1, 6, 6, 5, 6, 9, 4, 7, 6]

after_list = [el for el in before_list if before_list.count(el) < 2]

print(after_list)
