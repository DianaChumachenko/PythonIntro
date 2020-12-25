from random import randint

lst = list(randint(0, 99) for _ in range(10))
print(lst)

k = int(input('PLease enter index: '))

for i in range(k, len(lst)-1):
    lst[i] = lst[i+1]

lst.pop(len(lst)-1)
print(lst)