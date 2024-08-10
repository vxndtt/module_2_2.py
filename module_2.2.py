first = input('Введите первое число: ')
second = input('Введите первое число: ')
third = input('Введите первое число: ')
if first == second and first == third:
    print(3)
elif first == second and first != third or first == third and first != second or second == third and second != first:
    print(2)
else:
    print(0)