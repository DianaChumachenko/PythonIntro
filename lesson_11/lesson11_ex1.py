from pprint import pprint

d = dict(zip([x for x in range(32, 128)], [chr(x) for x in range(32, 128)]))
pprint(d)