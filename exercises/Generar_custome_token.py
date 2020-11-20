import string
import random

digits = string.ascii_uppercase + string.digits

def get_promo_code():
    return ''.join(random.choices(digits, k=7))

print(get_promo_code())
print(get_promo_code())
print(get_promo_code())