#!/usr/bin/env python3
# Based on a script and research by Larsenv from RiiConnect24
from glob import glob
import os.path
import sys

from Crypto.Cipher import AES

# Thanks to Larsenv for figuring these out!
key = b"\xFF\x4C\x1A\xE3\xD4\xFF\xD2\x36\x71\x2E\x25\x8A\x1F\x0B\x91\xE7\x2C\x91\x25\xB0\xDF\x94\xC1\x69\x1B\xCE\xF1\x30\x11\xF1\x6C\x0F"
iv = b"\x86\x2D\x7D\x86\x76\xA6\x30\xA8\x29\x72\xAB\x97\x35\xE1\xA5\xCE"

decrypted_dir = os.path.join("address", "decrypted")

if not os.path.exists("address"):
    print("Please put all your ALAS files in the \"address\" directory!")
    sys.exit(0)

if not os.path.exists(decrypted_dir):
    os.makedirs(decrypted_dir)

for alas_file in glob(os.path.join("address", "*.alas")):
    print("Decrypting " + os.path.basename(alas_file) + "...")
    with open(alas_file, "rb") as infile:
        encrypted_file = infile.read()
        decrypted_file = AES.new(key, AES.MODE_CBC, iv).decrypt(encrypted_file[320:])
    with open(os.path.join(decrypted_dir, os.path.basename(alas_file)), "wb") as outfile:
        outfile.write(decrypted_file[32:])

print("Operation completed.")
