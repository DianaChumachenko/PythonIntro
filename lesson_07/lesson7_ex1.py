from pprint import pprint

text = input('Please enter text: ')

d = {}
for word in text.split():
    d[word] = d.get(word, 0) + 1
pprint(d)