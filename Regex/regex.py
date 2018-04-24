import re
file = open('regex_sum_61143.txt', 'r')
total = 0
for line in file:
    numbers_list = re.findall('[0-9]+', line)
    for number in numbers_list:
        total += int(number)
print(total)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

sent = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pattern = re.findall('\S+?@\S+', sent)
print(pattern)
