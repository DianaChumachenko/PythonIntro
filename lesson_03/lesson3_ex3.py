num = int(input('Please enter a three-digit number: '))

print('Your number:', num)

dig1 = num % 10
dig2 = num // 10 % 10
dig3 = num // 100

num1 = dig1 * 100 + dig2 * 10 + dig3
print('Result:', num1)