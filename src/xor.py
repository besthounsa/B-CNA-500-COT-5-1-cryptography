#!/usr/bin/env python3

import sys

def xor_block(key):
    my_input = input()
    if(len(my_input)%2 != 0):
        print("Error: Bad Input len", flush=sys.stderr)
        exit(84)
    if(len(key)%2 != 0):
        print("Error: Bad Input len", flush=sys.stderr)
        exit(84)
    if(len(my_input) != len(key) or len(key) == 0):
        print("Error: MESSAGE and BLOCK should be same size", flush=sys.stderr)
        exit(84)
    for i in range(0, len(my_input), 2):
        a = int(key[i: i+2], 16)
        b = int(my_input[i: i+2], 16)
        res = a ^ b
        print("%02x" % res, end="")
    print()
    exit(0)

def xor_stream(key):
    my_input = input()
    if(len(my_input)%2 != 0):
        print("Error: Bad Input len", flush=sys.stderr)
        exit(84)
    if(len(key)%2 != 0):
        print("Error: Bad Input len", flush=sys.stderr)
        exit(84)
    if(len(my_input) == 0 or len(key) == 0):
        print("Error: MESSAGE and BLOCK should be same size", flush=sys.stderr)
        exit(84)
    len_key = len(key)
    for i in range(0, len(my_input), 2):
        a = int(key[(i) % len_key: (i) % len_key + 2], 16)
        b = int(my_input[i: i+2], 16)
        res = a ^ b
        print("%02x" % res, end="")
    print()
    exit(0)