import random

lst = list(random.randint(0, 99) for _ in range(8))
print(lst)
C = 15
k = 3
lst.append(65)
print(lst)

for i in range(1, len(lst)):
    if (len(lst) - i) == k:
        break
    lst[len(lst) - i] = lst[len(lst) - i - 1]

lst[3] = C
print(lst)