from pwn import xor
from Crypto.Util.number import *
import secrets

a = 0x7112f78c5d4f524f35edb74957785d2fd690484a535428dca879404b4f24edee0704061d6093ee07045a

flag_ct = long_to_bytes(a)
flag = "MSEC{j"
flag = [ord(i) for i in flag]
key = []
for i in range(len(flag)):
    key.append(flag_ct[i] ^ flag[i])

key.append(flag_ct[-1] ^ ord('}'))
print(key)
flag = []
for i in range(len(flag_ct)):
    flag.append(flag_ct[i] ^ key[i % len(key)])
print(bytes(flag))
print(len(flag))