def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если строка состоит из одной цифры, возвращаем её как целое число
    if len(str_number) <= 1:
        return int(str_number)

    # Отделяем первую цифру
    first = int(str_number[0])

    # Рекурсивно вызываем функцию для оставшихся цифр и умножаем результат на первую цифру
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования функции
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24
