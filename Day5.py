lst = list(range(1, 101))
print(lst)

filteredList = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, lst))

print(filteredList)
