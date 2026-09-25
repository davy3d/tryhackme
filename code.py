import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id

encoded = b'gAAAAABqtpslxWbh3tptFgTO7LEfIa-UrYOoAZsOkfzXACvnRRrL9M6T5fmKSGqQ8uw8F0ZTxb1bgxQxT1Qbjjg4ZfQbmXOQTeJHafrkqzdDxZ9qyWwN0p7FdHwKiVcVCWayxnkT_cL53SVp8KyCpZhwUTa9TwZf5WBmH2LPvba36IRkk_wjA6aY6jH3AEbsaUTQCmnudfT7HOlD6TiVPs5eFHSqfGYqqYHBGAzIv-OHRXVctqBfG4gliTjE9iP2KPcjO0NSRCb2QCQdXHS3bEy2BbGFitmWjnJzr0LsDvbyuPE6r4kZ6FC82xqaMnncmNIiQQPXPBZlXLrisrMGnOgL0Whs3TAG_Br9Vlk6fOrZqWYnMCj8imsKPQSJ9o7gk6Q5la9N5ApEtGW709aG5TkJ0KsFYLWowpBT4JHU-5xjlQ6pRV16HtvTZ-2UucaVSHAXvFjaX9u3sXW0ipjlnweLgsqdYwE7_mRuDXMpNtqysjbvEXR9yyIJFzyqrBLtPG00PHzTXLXkqyPMecdK0GZXnubVGHXfM7PKcmRjaG_TEnlOn-jOVS-goF7q9F3gNBwPXUIMOglP'

print('Hi! Try your luck!')
print('# = number, enter all letters in lowercase. no spaces\n')
a = input('# of people in 8th grade class (ours): ')
b = input('The type of math you took last year (8th grade): ')
c = input("The # of letters in the olderst person in our class's first name: ")
d = input('Your username converted to #: ')
e = input("Priestly Boy's sweater name: ")
f = input('Your middle name: ')
g = input('The webcomic I like: ')

password = '{}{}{}{}{}{}{}'.format(a, b, b, d, e, f, g).encode()
kdf = Argon2id(
    salt=b'\xa8\xfe\xf9\x9b\x8f\xa8i\xa5\xed\x03N\xe6`\x9c:\xcb',
    length=32,
    iterations=1,
    lanes=4,
    memory_cost=2**21
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)

token = f.decrypt(encoded).decode()

print('\n\n')
print(token)
