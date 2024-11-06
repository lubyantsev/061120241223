def calculate_structure_product(data):
    product = 1
    has_numbers = False  # Флаг для отслеживания наличия чисел

    if isinstance(data, dict):
        items = data.items()
    elif isinstance(data, (list, tuple)):
        items = data
    else:
        items = [data]  # Обрабатываем один элемент, если это не коллекция

    for item in items:
        if isinstance(item, (dict, list, tuple)):
            result = calculate_structure_product(item)  # Рекурсивный вызов
        elif isinstance(item, str):
            result = len(item)  # Длина строки
        elif isinstance(item, (int, float)):
            result = item  # Число
        else:
            continue  # Игнорируем неподдерживаемые типы

        if result == 0:
            return 0  # Если одно из произведений равно 0

        product *= result
        has_numbers = True

    return product if has_numbers else 0  # Возвращаем 0, если не было чисел


def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    if len(str_number) == 1:
        return int(str_number)  # Если осталась одна цифра, просто возвращаем её
    return int(str_number[0]) * get_multiplied_digits(
        int(str_number[1:]))  # Умножаем первую цифру на результат рекурсии


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
