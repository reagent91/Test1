numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

is_prime = True
primes = []
not_primes = []

for i in numbers:
    if i == 1:
        numbers.remove(1)
        break
for i in numbers:
    for j in range(2, i):
        if  i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)

print('Простые числа', primes)
print('Сложные числа', not_primes)
