import random

def generate_password(chars, len):
    password = ''
    for i in range(len):
        password += random.choice(chars)
    return password

chars = list(
    '0123456789!#$%&*+-=?@^_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
random.shuffle(chars)

len = int(input('Desired password length: '))
print(generate_password(chars, len))
