import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id

encoded = b'gAAAAABqtpPWe6cqe_sUnxDfK063cXYWqAGY1h83ah0-O4dHhuHHhWnC078jRPJmp933nUwJHWJQqEQdFUBWVNliFLdJ_U8VbzuhOiEk4lbPvIYLV5tZQFtnEPPg7EEp07hG4pgEzX6lQNmWlYJlZyoW03UFDP92fTjpptAIK3dKsdJvVwVhT3hF0ydfbGp-vkcYft7QwpRyLO8hCgt7lj8fqSgZdNIadyp9VkcfnxvpgfWVlliXzdcoCGo8bKunjP_t46DACPPUbDbm4rxxzGsWNNjwBE0sd-gNI-G-uev6StBR2H2SGFKrBmZ7JN5H5AfGuBDsx7uCJTfplZnShbvZxF8FO1nTGPNe3uOHTwvsTAylZDUAgFrHPUaJr_o8Cgd63yxxMORXIimOVrBdLQGmnCQNI2gLW2V7NZ6HvH-GLgbBB2kjnv1iIxUqaGRNrqwyHvMaIIp7KkCj_nf65hWH7b81ro_LKWhZ9YPSXuYnvchlTks-cS6Frjh-8-471BKU7bXJBNjv'

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
