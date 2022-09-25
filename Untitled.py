def get_sum(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    delimiter = str('&')
    return str(one + delimiter + two)

summ = get_sum('Learn', 'python').upper()
print(summ)