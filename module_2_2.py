First= int(input('Введите любое целое число '))
Second= int(input('Введите любое целое число '))
Third= int(input('Введите любое целое число '))
if First==Second==Third:
    print(3)
elif First==Second or First==Third or Second==Third:
    print(2)
else:
    print(0)