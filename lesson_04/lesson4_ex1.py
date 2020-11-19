N = int(input('Please enter a number: '))

i = 1
print(N, end='\t')
while i ** 2 <= N:
    print(i ** 2, end=' ')
    i += 1
