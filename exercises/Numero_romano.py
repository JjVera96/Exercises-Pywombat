def roman_to_decimal(roman):
    nums = {
        'I': { 'value': 1, 'rest': 'VX'},
        'V': { 'value': 5, 'rest': ''},
        'X': { 'value': 10, 'rest': 'LC'},
        'L': { 'value': 50, 'rest': ''},
        'C': { 'value': 100, 'rest': 'DM'},
        'D': { 'value': 500, 'rest': ''},
        'M': { 'value': 1000, 'rest': ''},
    }

    decimal = 0
    i = 0
    while i < len(roman):
        if i == len(roman)-1: 
            decimal += nums[roman[i]]['value']
            i += 1
        else:
            if roman[i+1] in nums[roman[i]]['rest']:
                decimal += (nums[roman[i+1]]['value'] - nums[roman[i]]['value'])
                i += 2
            else:
                decimal += nums[roman[i]]['value']
                i += 1
    return decimal

if __name__ == '__main__':
    roman = input('')
    print(roman_to_decimal(roman.upper()))