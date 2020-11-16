num1 = int(input('Please enter a number of pupils in the first class: '))
num2 = int(input('Please enter a number of pupils in the second class: '))
num3 = int(input('Please enter a number of pupils in the third class: '))

num = (num1+num2+num3) // 2 + (num1+num2+num3) % 2

print('Result:', num)
