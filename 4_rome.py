
def convert_roman_to_decimal(number):
    roman = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000,
    }
    i = 0
    num = 0
    while i < len(number):
        if i+1 < len(number) and number[i:i+2] in roman:
            num += roman[number[i:i+2]]
            i += 2
        else:
            # print(i)
            num += roman[number[i]]
            i += 1
    return num


def convert_decimal_to_roman(number):
    roman = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    result = ""
    for num in roman:
        div = number // num
        number %= num
        result += roman[num]*div
    return result


string = input()
first_number, second_number = string.split("+")
sum = convert_roman_to_decimal(first_number) + \
    convert_roman_to_decimal(second_number)
print(convert_decimal_to_roman(sum))
