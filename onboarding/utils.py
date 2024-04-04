import random
import string

def generate_otp():
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(5))
    return otp