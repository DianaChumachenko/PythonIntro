text = input('Please enter text: ')

d = {}
for word in text.split():
    d[word] = d.get(word, 0) + 1


max_values = max(d.values())
for key in sorted(d.keys()):
    if d[key] == max_values:
        print(key)
        break