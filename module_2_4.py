# Исходный список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем каждый элемент в списке numbers
for number in numbers:
    # Пропускаем число 1, так как оно не является простым
    if number == 1:
        continue

    # Предполагаем, что число простое
    is_prime = True

    # Проверяем делимость числа на все числа от 2 до number (не включая)
    for divisor in range(2, number):
        if number % divisor == 0:  # Если число делится на divisor
            is_prime = False  # Устанавливаем флаг is_prime в False
            break  # Выходим из цикла, так как нашли делитель

    # В зависимости от значения is_prime добавляем число в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Выводим результаты на экран
print("Primes:", primes)
print("Not Primes:", not_primes)
