def personal_sum(numbers):
    correct_data = 0
    incorrect_data = 0
    result = 0

    for item in numbers:

        try:
            result += item
            correct_data += 1

        except TypeError:
            incorrect_data += 1

            print(f'{incorrect_data} Некорректный тип данных для подсчёта суммы ->> {item}')
    print(f'(некорректный тип данных: {incorrect_data}, правильный тип данных: {correct_data})')
    print(f'сумма найденных чисел: {result}')

    return result, incorrect_data, correct_data


def calculate_average(numbers):
    incorrect_data = 0
    try:
        result2 = personal_sum(numbers)
        avg = result2[0] / result2[2]
        return f'среднее арифметическое {avg}'

    except TypeError:
        incorrect_data += 1
        print(f'{incorrect_data} В numbers записан некорректный тип данных ->> {numbers}')
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print('-------------------------')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print('-------------------------')
print(f'Результат 3: {calculate_average(567)}')
print('-------------------------')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')

# Вывод на консоль:
# Некорректный тип данных для подсчёта суммы - 1
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 2
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 3
# Результат 1: 0
# Некорректный тип данных для подсчёта суммы - Строка
# Некорректный тип данных для подсчёта суммы - Ещё Строка
# Результат 2: 2.0
# В numbers записан некорректный тип данных
# Результат 3: None
# Результат 4: 26.5
