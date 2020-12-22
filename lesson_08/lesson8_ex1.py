lst = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

res = list(map(lambda lst: lst[0], lst))

res1 = list(map(lambda lst: round((lst[2]*lst[3]), 2), lst))

for i in range(len(res1)):
    if res1[i] < 100:
        res1[i] += 10


result = list(zip(res, res1))
print(result)
