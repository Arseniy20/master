a = int(input('Введите год: '))
if (a % 4 == 0 and a % 100 != 0) or (a % 4 == 0 and a % 400 == 0):
    print('Год ' + str(a) + ' високосный')
else:
    print('Год ' + str(a) + ' невисокосный')