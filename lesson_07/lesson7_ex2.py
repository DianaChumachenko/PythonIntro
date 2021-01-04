text = input('Please enter text: ')

d = {}
for word in text.split():
    d[word] = d.get(word, 0) + 1


max_value = 0
result = ''
for i in d:
    if d[i] >= max_value:
        max_value = d[i]
        result = i

print(result)
