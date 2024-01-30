from pwn import xor
from Cryptodome.Util.number import *
import secrets
from flag import flag

key = secrets.token_bytes(7)
print(key)

flag = xor(flag, key)

with open("output.txt", "w") as f:
    f.write(hex(bytes_to_long(flag)))
