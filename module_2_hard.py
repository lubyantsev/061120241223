def generate_password(num):
    result = ""

    # Генерация всех уникальных пар (a, b) где 1 <= a < b <= 20 и a + b не равно num
    pairs = []
    for a in range(1, 21):
        for b in range(a + 1, 21):
            pairs.append((a, b))

    # Проверка кратности
    for a, b in pairs:
        pair_sum = a + b
        if num % pair_sum == 0:  # Если num кратно сумме пары
            result += str(a) + str(b)  # Добавляем пару в результат

    return result


# Пример использования
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Нужный пароль для числа {n}: {password}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")
