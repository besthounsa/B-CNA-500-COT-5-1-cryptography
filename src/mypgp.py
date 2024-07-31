#!/usr/bin/env python3

import sys
import os

from xor import xor_block, xor_stream

from aes import aes_encrypt, aes_decrypt, aes_encrypt_block, aes_decrypt_block

from rsa import generate_key, rsa_encrypt, rsa_decrypt

from pgp import pgp_encrypt, pgp_decrypt

def afficher_help():
    print("USAGE\n"
    "\t./mypgp [-xor | -aes | -rsa] [-c | -d] [-b] KEY\n"
    "\tthe MESSAGE is read from standard input\n"
    "DESCRIPTION\n"
    "\t-xor\tcomputation using XOR algorithm\n"
    "\t-aes\tcomputation using AES algorithm\n"
    "\t-rsa\tcomputation using RSA algorithm\n"
    "\t-c\tMESSAGE is clear and we want to cipher it\n"
    "\t-d \tMESSAGE is ciphered and we want to decipher it\n"
    "\t-b \tblock mode: for xor and aes, only works on one block\n"
    "\t\tMESSAGE and KEY must be of the same size\n"
    "\t-g P Q for RSA only: generate a public and private key\n"
    "\t\tpair from the prime number P and Q\n"
    )


def afficher_help_erreur():
    print("USAGE\n"
    "\t./mypgp [-xor | -aes | -rsa] [-c | -d] [-b] KEY\n"
    "\tthe MESSAGE is read from standard input\n"
    "DESCRIPTION\n"
    "\t-xor\tcomputation using XOR algorithm\n"
    "\t-aes\tcomputation using AES algorithm\n"
    "\t-rsa\tcomputation using RSA algorithm\n"
    "\t-c\tMESSAGE is clear and we want to cipher it\n"
    "\t-d \tMESSAGE is ciphered and we want to decipher it\n"
    "\t-b \tblock mode: for xor and aes, only works on one block\n"
    "\t\tMESSAGE and KEY must be of the same size\n"
    "\t-g P Q for RSA only: generate a public and private key\n"
    "\t\tpair from the prime number P and Q\n", flush=sys.stderr
    )


def main():
    # Afficher le menu
    if(len(sys.argv) == 2 and sys.argv[1] == "-h"):
        afficher_help()
        exit(0)
    
    # XOR
    if(len(sys.argv) >= 2 and sys.argv[1] == "-xor"):
        # Crypter
        if(len(sys.argv) >= 3 and sys.argv[2] == "-c"):
            # Verifier si en mode block
            if(len(sys.argv) >= 4 and sys.argv[3] == "-b"):
                # Crypter
                if(len(sys.argv) >= 5):
                    xor_block(sys.argv[4])
                    exit(0)
            # Crypter en stream
            if(len(sys.argv) >= 4):
                xor_stream(sys.argv[3])
                exit(0)
            # Mauvais argument
            print("Error: incorrent argument length\n", flush=sys.stderr)
            exit(84)

        # Decrypter
        if(len(sys.argv) >= 3 and sys.argv[2] == "-d"):
            # Verifier si en mode block
            if(len(sys.argv) >= 4 and sys.argv[3] == "-b"):
                # Crypter
                if(len(sys.argv) >= 5):
                    xor_block(sys.argv[4])
                    exit(0)
            # Crypter en stream
            if(len(sys.argv) >= 4):
                xor_stream(sys.argv[3])
                exit(0)
            # Mauvais argument
            print("Error: incorrent argument length\n", flush=sys.stderr)
            exit(84)
        
        # Mauvais argument
        print("Error: third argument must be -c or -d\n", flush=sys.stderr)
        exit(84)

    # AES
    if(len(sys.argv) >= 2 and sys.argv[1] == "-aes"):
        # Crypter
        if(len(sys.argv) >= 3 and sys.argv[2] == "-c"):
            # Verifier si en mode block
            if(len(sys.argv) >= 4 and sys.argv[3] == "-b"):
                # Crypter
                if(len(sys.argv) >= 5):
                    aes_encrypt_block(sys.argv[4])
                    exit(0)
            # Crypter en stream
            if(len(sys.argv) >= 4):
                aes_encrypt(sys.argv[3])
                exit(0)
            # Mauvais argument
            print("Error: incorrent argument length\n", flush=sys.stderr)
            exit(84)
        # Decrypter
        if(len(sys.argv) >= 3 and sys.argv[2] == "-d"):
            # Verifier si en mode block
            if(len(sys.argv) >= 4 and sys.argv[3] == "-b"):
                # Crypter
                if(len(sys.argv) >= 5):
                    aes_decrypt_block(sys.argv[4])
                    exit(0)
            # Crypter en stream
            if(len(sys.argv) >= 4):
                aes_decrypt(sys.argv[3])
                exit(0)
            # Mauvais argument
            print("Error: incorrent argument length\n", flush=sys.stderr)
            exit(84)
        exit(0)

    # RSA
    if(len(sys.argv) >= 2 and sys.argv[1] == "-rsa"):
        # Generate Key
        if(len(sys.argv) >= 3 and sys.argv[2] == "-g"):
            # Verifier P et Q
            if(len(sys.argv) >= 5):
                generate_key(sys.argv[3], sys.argv[4])
                exit(0)
            # Mauvais argument
            print("Error: incorrent argument length\n", flush=sys.stderr)
            exit(84)
        # Crypter
        if(len(sys.argv) >= 3 and sys.argv[2] == "-c"):
            if(len(sys.argv) >= 4):
                rsa_encrypt(sys.argv[3])
                exit(0)
            # Mauvais argument
            print("Error: incorrent argument length\n", flush=sys.stderr)
            exit(84)
        # Decrypter
        if(len(sys.argv) >= 3 and sys.argv[2] == "-d"):
            if(len(sys.argv) >= 4):
                rsa_decrypt(sys.argv[3])
                exit(0)
            # Mauvais argument
            print("Error: incorrent argument length\n", flush=sys.stderr)
            exit(84)


    # PGP
    if(len(sys.argv) >= 2 and sys.argv[1] == "-pgp"):
        # Crypter
        if(len(sys.argv) >= 3 and sys.argv[2] == "-c"):
            if(len(sys.argv) >= 4):
                pgp_encrypt(sys.argv[3])
                exit(0)
            # Mauvais argument
            print("Error: incorrent argument length\n", flush=sys.stderr)
            exit(84)
        # Decrypter
        if(len(sys.argv) >= 3 and sys.argv[2] == "-d"):
            if(len(sys.argv) >= 4):
                pgp_decrypt(sys.argv[3])
                exit(0)
            # Mauvais argument
            print("Error: incorrent argument length\n", flush=sys.stderr)
            exit(84)
    
    # Mauvais argument
    afficher_help_erreur()
    exit(84)
    

if __name__ == "__main__":
    main()