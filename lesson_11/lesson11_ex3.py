from pprint import pprint

d = {
    'apple': ['malum', 'pomum', 'popula'],
    'fruit': ['baca', 'bacca', 'popum'],
    'punishment': ['malum', 'multa']
}

d1 = {}
for key, value in d.items():
    for word in value:
        if word not in d1:
            d1[word] = []
        d1[word].append(key)

pprint(d1)