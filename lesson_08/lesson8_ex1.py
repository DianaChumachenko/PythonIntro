ledger = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
def func(lst):
    return round(lst[2]*lst[3], 2)


lst = []
for i in ledger:
    lst.append(func(ledger))