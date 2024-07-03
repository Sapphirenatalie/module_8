def add_everything_up(a, b):
    try:
        return round((a + b), 3)
    except TypeError:
        return f'{str(a)} {str(b)}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# Вывод в консоль:
# 123.456строка
# яблоко4215
# 130.456
