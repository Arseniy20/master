a = int(input('Введите номер плакцартного места: '))
if a < 37:
    print('Купе')
else:
    print('Боковое')
if a % 2 == 0:
    print('Верхнее')
else:
    print('Нижнее')