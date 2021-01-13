before_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

after_list = [before_list[i] for i in range(1, len(before_list)) if before_list[i] > before_list[i-1]]
print(after_list)
