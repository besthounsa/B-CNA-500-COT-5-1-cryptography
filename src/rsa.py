#!/usr/bin/env python3


from utils import big_endian_hex_to_little_endian_hex, little_endian_hex_to_big_endian_hex, int_to_hex
import sys

def generate_key(p, q):
    p = int.from_bytes(bytes.fromhex(p), "little")
    q = int.from_bytes(bytes.fromhex(q), "little")
    n = p*q
    e = 0x10001
    d = 0
    try:
        d = pow(e, -1, (p-1)*(q-1))
    except:
        print("Error: P and Q not inversible", flush=sys.stderr)
        exit(84)
    n_hex = big_endian_hex_to_little_endian_hex(int_to_hex(n))
    e_hex = big_endian_hex_to_little_endian_hex(int_to_hex(e))
    d_hex = big_endian_hex_to_little_endian_hex(int_to_hex(d))
    print(f"public key: {e_hex}-{n_hex}")
    print(f"private key: {d_hex}-{n_hex}")
    exit(0)


def rsa_encrypt(key):
    try:
        e_hex, n_hex = key.split("-")
        e = int.from_bytes(bytes.fromhex(e_hex), "little")
        n = int.from_bytes(bytes.fromhex(n_hex), "little")
        m = int.from_bytes(bytes.fromhex(input()), "little")
        c = pow(m, e, n)
        print(big_endian_hex_to_little_endian_hex(int_to_hex(c)))
    except:
        print("Error: Invalid RSA Key", flush=sys.stderr)
        exit(84)
    exit(0)

def rsa_decrypt(key):
    try:
        d_hex, n_hex = key.split("-")
        d = int.from_bytes(bytes.fromhex(d_hex), "little")
        n = int.from_bytes(bytes.fromhex(n_hex), "little")
        c = int.from_bytes(bytes.fromhex(input()), "little")
        m = pow(c, d, n)
        print(big_endian_hex_to_little_endian_hex(int_to_hex(m)))
    except:
        print("Error: Invalid RSA Key", flush=sys.stderr)
        exit(84)
    exit(0)

def rsa_decrypt_bytes(key, cipher : str):
    try:

        d_hex, n_hex = key.split("-")
        d = int.from_bytes(bytes.fromhex(d_hex), "little")
        n = int.from_bytes(bytes.fromhex(n_hex), "little")
        c = int.from_bytes(bytes.fromhex(cipher), "little")
        m = pow(c, d, n)
        return big_endian_hex_to_little_endian_hex(int_to_hex(m))
    except:
        print("Error: Invalid RSA Key", flush=sys.stderr)
        exit(84)

def rsa_encrypt_bytes(key, message : bytes):
    try:
        e_hex, n_hex = key.split("-")
        e = int.from_bytes(bytes.fromhex(e_hex), "little")
        n = int.from_bytes(bytes.fromhex(n_hex), "little")
        m = int.from_bytes(message, "little")
        c = pow(m, e, n)
        return big_endian_hex_to_little_endian_hex(int_to_hex(c))
    except:
        print("Error: Invalid RSA Key", flush=sys.stderr)
        exit(84)

