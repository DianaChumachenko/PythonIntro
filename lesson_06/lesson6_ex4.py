import random

lst = list(random.randint(0, 99) for _ in range(8))
print(lst)
C = 15
k = 3
lst.append(65)
print(lst)

x = 0
for i in lst[len(lst):3:-1]:
    lst[i] = lst[i - 1]
    x += 1
print(lst)

lst[3] = 15