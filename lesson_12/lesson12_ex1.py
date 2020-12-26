file = open('src_14.txt', encoding='utf-8')
res = open('dst.txt', 'wt', encoding='utf-8')

avr_class = 0
cnt = 0
temp = '{:<25}{:5}'

for line in file:
    line = line.split()
    name = line[1] + ' ' + line[0][0] + '.'
    avr = round(sum([int(s) for s in line[2:]]) / len(line[2:]), 2)
    if avr < 5:
        print(temp.format(name, avr))

    res.write(temp.format(name, avr))
    res.write('\n')
    avr_class += avr
    cnt += 1


file.close()
res.close()
print(temp.format('Class average:', round(avr_class/cnt, 2)))
