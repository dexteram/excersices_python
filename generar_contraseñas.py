import string
import random

# string.ascii_letters
# 'abcdefghijklmnñopqrstuvwxyxABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# string.digits
# '0123456789'
letras = string.ascii_letters + string.digits
password = ''.join(random.choice(letras) for x in range(16))
print(password)