h = int(input('Please enter height: '))

i = 0
while i < h:
    j = 0
    while j < h * 2:
        if h - 1 - i <= j <= h - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1
print()


i = 0
while i < h:
    j = 0
    while j < h * 2 - 1:
        if i == h - 1 - j or i == h - 1 or j == h - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1
print()


i = 0
while i < h:
    j = 0
    while j < h * 2:
        if h - 1 - i <= j <= h - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1
i = 0
while i < h - 1:
    j = 0
    while j < h * 2:
        if i == j - 1 or j == h - i - 1 + (h - 1) - 1:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1
print()


i = 0
while i < h:
    j = 0
    while j < h * 2:
        if h - 1 - i <= j <= h - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1
i = 0
while i < h - 1:
    j = 0
    while j < h * 2:
        if i == j - 1 or j == h - i - 1 + (h - 1) - 1 or j == h - 1:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1
print()

