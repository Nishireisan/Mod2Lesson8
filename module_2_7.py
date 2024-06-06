def get_multiplied_digits(number):
    str_number = f'{number}'
    if len(str_number) < 1:
        return 'Тут пусто :((('
    first = int(str_number[0])
    if first == 0:
        return get_multiplied_digits(int(str_number[1:]))
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits('00123')
print(result)
