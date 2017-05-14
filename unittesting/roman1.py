import re

roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))
def to_roman(n):
    '''Convert integer to Roman numeral'''
    if not isinstance(n, int):
        raise NotIntegerError('non-integers cannot be converted')
    if not (0 < n < 4000):
        raise OutOfRangeError('number out of range (must be positive and less than 4000)')

    result = ''
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    return result

def from_roman(roman_numeral):
    if not isinstance(roman_numeral, str):
        raise InvalidNumeralError('Input must be a string')
    if not roman_numeral:
        raise InvalidNumeralError('cannot convert an empty string')
    valid_pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    if not re.search(valid_pattern, roman_numeral):
        raise InvalidNumeralError('not a valid Roman numeral')
    result, index = 0, 0
    for numeral, integer in roman_numeral_map:
        while roman_numeral[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result


class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidNumeralError(ValueError): pass
