# Глобальная переменная для отслеживания количества вызовов
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    # Приводим все к нижнему регистру для сравнения
    string_lower = string.lower()
    return any(item.lower() == string_lower for item in list_to_search)


# Примеры вызовов функций
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

# Выводим количество вызовов
print(calls)
