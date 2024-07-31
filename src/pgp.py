#!/usr/bin/env python3
import sys
import random

from rsa import rsa_encrypt_bytes, rsa_decrypt_bytes

from aes import aes_encrypt_bytes, aes_decrypt_bytes


def pgp_encrypt(key):
    print("-----BEGIN MY_PGP MESSAGE-----")
    my_input = sys.stdin.read().encode()
    secret_aes_key = bytes([random.randint(0, 255) for _ in range(16)])
    print("Cipher_Key=", rsa_encrypt_bytes(key, secret_aes_key))
    print("Ciphertext=", aes_encrypt_bytes(secret_aes_key, my_input))
    print("-----END MY_PGP MESSAGE-----")
    exit(0)


def pgp_decrypt(key):
    my_inputs = sys.stdin.readlines()
    if len(my_inputs) != 4:
        print("Error: Invalid MY_PGP File", flush=sys.stderr)
        exit(84)
    if my_inputs[0] != "-----BEGIN MY_PGP MESSAGE-----\n" or  my_inputs[-1] != "-----END MY_PGP MESSAGE-----\n":
        print("Error: Invalid MY_PGP File", flush=sys.stderr)
        exit(84)
    ckey = my_inputs[1].split()
    cmes = my_inputs[2].split()
    if len(ckey) != 2 or ckey[0] != "Cipher_Key=":
        print("Error: Invalid MY_PGP File", flush=sys.stderr)
        exit(84)
    if len(cmes) != 2 or cmes[0] != "Ciphertext=":
        print("Error: Invalid MY_PGP File", flush=sys.stderr)
        exit(84)
    ckey = ckey[1]
    cmes = cmes[1]
    secret_aes_key = rsa_decrypt_bytes(key, ckey)
    print(aes_decrypt_bytes(secret_aes_key, cmes).decode())


    

