import random

print(len(set([random.randint(0, 99) for _ in range(25)]) & set([random.randint(0, 99) for _ in range(25)])))