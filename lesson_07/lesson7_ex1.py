s = str(input('Please enter a string: '))

x = {}

for word in s:
    x[word] = x.get(word, 0) + 1
    print(x[word] - 1, end=' ')