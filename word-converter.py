import sys
import math

units = {
    0: None,
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

leading_digits = {
    1: 'thousand',
    2: 'million',
    3: 'billion',
    4: 'trillion',
    5: 'quadrillion',
    6: 'quintillion',
    7: 'sextillion',
    8: 'septillion',
    9: 'octillion',
    10: 'nonillion',
    11: 'decillion'
}

 
def number_in_words(number):
    if number == 0:
        return 'zero'
    return number_at_index(number)

     
def number_at_index(number):
    # units
    if number < 20:  # units
        return units[number]

    # tenths
    if number < 100:
        return merge(
            tens[number // 10], units[number % 10],
            use_dash=units[number % 10] != None
        )

    # hundred
    if number < 1000:
        return divide_and_modulo(
            dividend=number, divisor=100,
            magnitude='hundred'
        )

    # thousands
    for significant_digit, name in leading_digits.items():
        if number < math.pow(1_000, significant_digit + 1):
            break

    return divide_and_modulo(
        dividend=number,
        divisor=math.pow(1000, significant_digit),
        magnitude=name
    )

def divide_and_modulo(dividend, divisor, magnitude):
    comma = ',' if dividend % divisor > 100 else ''
    return merge(
        number_at_index(dividend // divisor),
        magnitude + comma,
        number_at_index(dividend % divisor)
    )

def merge(*args, use_dash=False):
    if len(args) == 3 and args[-1] != None: # and 'hundred' in args:
        return ' '.join(args[:-1]) + ' and ' + args[-1]
    if use_dash:
        merge_str = '-'
    else:
        merge_str = ' '
    return merge_str.join(filter(bool, args))

def get_user_input(user_input):
    for word in user_input.split(' '):
        if word.isdigit():
            print(number_in_words(int(word)))
            return
    print('number invalid')

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        with open(sys.argv[1]) as buff:
            for input_ in buff.readlines():
                get_user_input(input_)
    else:
        print('no user input file')
