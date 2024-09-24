 # module_2_4.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers.remove(1) # удаляем число 1 т.к. оно не является ни простым, ни составным числом
primes = [] # создаем список только простых числ
not_primes = [] # cоздаем список тольконе простых числ
for number in numbers:  # проверка цикла
    if number < 2: # если число меньше 2, оно добавляется в список непростых чисел
        not_primes.append(number)
        continue
    if number == 2: # если число меньше 2, оно добавляется в список непростых чисел
        primes.append(number)
        continue
    is_prime= True # предпологаем что число простое
    for i in range(2, number // 2 + 1): # проверяем на делимость
        if number % i == 0:
            is_prime = False # если делится то число не простое
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)
print("Primes:", primes)
print("Not Primes:", not_primes)