from random import randint

def print_matrix(matrix):
    l = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print('{:6}'.format(matrix[i][j]), end='')
            l[j] += matrix[i][j]
        print()
    for i in range(len(l)):
        print('{:6}'.format(l[i]), end='')
    print()


rows = int(input('Please enter rows: '))
cols = int(input('Please enter cols: '))

lst = [[randint(1, 99) for _ in range(cols)] for _ in range(rows)]


print_matrix(lst)