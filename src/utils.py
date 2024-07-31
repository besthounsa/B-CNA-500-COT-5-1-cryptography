#!/usr/bin/env python3

import struct

def big_endian_hex_to_little_endian_hex(big):
    hex_bytes = bytes.fromhex(big)
    hex_bytes = hex_bytes[::-1]
    return hex_bytes.hex()

def little_endian_hex_to_big_endian_hex(big):
    hex_bytes = bytes.fromhex(big)
    hex_bytes = hex_bytes[::-1]
    return hex_bytes.hex()

def int_to_hex(a):
    out = hex(a)[2:]
    if len(out)%2 == 1:
        out = "0"+out
    return out