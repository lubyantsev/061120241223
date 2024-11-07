def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    if len(str_number) == 1:
        return int(str_number) if str_number != '0' else 1  # Если осталась одна цифра, возвращаем её, 0 мы не учитываем
    first = int(str_number[0])  # Первая цифра
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))  # Пропускаем ноль
    # Умножаем первую цифру на результат рекурсии с оставшимися цифрами
    return first * get_multiplied_digits(int(str_number[1:]))

# Примеры использования функции get_multiplied_digits
result1 = get_multiplied_digits(40203)
print(result1)  # Ожидаемый вывод: 24