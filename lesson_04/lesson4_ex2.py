amount = 0
sum = 0
min_value = 0
max_value = 0
even = 0
odd = 0

while True:
    num = int(input('Please enter a number: '))
    if num == 0:
        break

    amount += 1
    sum += num

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

    if amount == 1:
        min_value = num
        max_value = num

    if min_value > num:
        min_value = num

    if max_value < num:
        max_value = num

print('Amount: ', amount)
print('Sum: ', sum)
print('Average: ', round(sum / amount, 2))
print('Max value: ', max_value)
print('Min value: ', min_value)
print('Even: ', even)
print('Odd: ', odd)


