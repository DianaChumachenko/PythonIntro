s = str(input('Please enter a string: '))

a = s[: s.find('h')+1]
b = s[s.find('h')+1: s.rfind('h')]
c = s[s.rfind('h'):]

s1 = a + b.replace('h', 'H') + c
print(s1)
