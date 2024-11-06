def calculate_structure_product(data):
    product = 1
    has_numbers = False  # Флаг для отслеживания наличия чисел

    # Проверяем тип данных
    if isinstance(data, dict):
        # Если это словарь, перебираем ключи и значения
        for key, value in data.items():
            result = calculate_structure_product(key)  # Обрабатываем ключи
            if result == 0:
                return 0  # Если одно из произведений равно 0
            product *= result
            result = calculate_structure_product(value)  # Обрабатываем значения
            if result == 0:
                return 0  # Если одно из произведений равно 0
            product *= result
            has_numbers = True
    elif isinstance(data, list) or isinstance(data, tuple):
        # Если это список или кортеж, перебираем элементы
        for item in data:
            result = calculate_structure_product(item)
            if result == 0:
                return 0  # Если одно из произведений равно 0
            product *= result
            has_numbers = True
    elif isinstance(data, str):
        # Если это строка, добавляем её длину
        product *= len(data)
        has_numbers = True
    elif isinstance(data, (int, float)):
        # Если это число, перемножаем его значение
        product *= data
        has_numbers = True

    return product if has_numbers else 0  # Возвращаем 0, если не было чисел


def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    first = int(str_number[0])  # Берем первую цифру

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))  # Умножаем первую цифру на результат рекурсии
    else:
        return first  # Если осталась одна цифра, просто возвращаем её


# Пример использования функции calculate_structure_product
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result_product = calculate_structure_product(data_structure)
print(result_product)  # Ожидание: 240 (1*2*3*4*5*6*7*8*2*35 = 240)

# Пример использования функции get_multiplied_digits
result_digits = get_multiplied_digits(40203)
print(result_digits)  # Ожидаемый вывод: 24
