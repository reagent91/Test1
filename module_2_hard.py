table_2 = int(input('Введите число с первой каменной вставки '))
old_result = []
i = table_2
x = int(i//1.5)
for j in range(1, x):
    for k in range(1, i):
        if i % (j + k) == 0 and k!= j and k >=j:
            old_result.extend([j, k])
        else:
            continue
for new_result in old_result:
    print(new_result, end='')




