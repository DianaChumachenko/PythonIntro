import random

lst = list(random.randint(0, 99) for _ in range(25))
print(lst)

x = 0
for i in range(1, len(lst) - 1):
    if lst[i - 1] < lst[i] > lst[i + 1]:
        x += 1
print(x)