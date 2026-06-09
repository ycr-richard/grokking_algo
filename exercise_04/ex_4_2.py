def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


print(count([1, 2, 3, 5, 8, 13, 21]))
