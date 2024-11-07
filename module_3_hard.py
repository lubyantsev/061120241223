def calculate_structure_sum(data):
    total = 0

    if isinstance(data, (list, tuple)):
        for item in data:
            total += calculate_structure_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            total += calculate_structure_sum(key)  # Суммируем длину ключей
            total += calculate_structure_sum(value)  # Суммируем значения
    elif isinstance(data, str):
        total += len(data)  # Суммируем длину строки
    elif isinstance(data, (int, float)):
        total += data  # Суммируем числа
    elif isinstance(data, set):
        for item in data:
            total += calculate_structure_sum(item)  # Суммируем элементы множества

    return total


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99
