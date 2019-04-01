import pytest
import he_encryption
import random
from math import pow


def test_gen_key():
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
    he_encryption.gen_key()

# Driver code
# def main():
#     msg = 'encryption'
#     print("Original Message :", msg)
#
#     q = random.randint(pow(10, 20), pow(10, 50))
#     g = random.randint(2, q)
#
#     key = gen_key(q)  # Private key for receiver
#     h = power(g, key, q)
#     print("g used : ", g)
#     print("g^a used : ", h)
#
#     en_msg, p = encrypt(msg, q, h, g)
#     dr_msg = decrypt(en_msg, p, key, q)
#     dmsg = ''.join(dr_msg)
#     print("Decrypted Message :", dmsg)
