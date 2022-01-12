import binascii
import random
import hashlib

word_list = []

try:
    with open("wordlist.txt") as file:
        raw = file.read().strip()
        word_list = raw.split("\n")
except FileNotFoundError:
    print("[ERROR] Word list file not found!")
except IOError:
    print("[ERROR] Word list format invalid!")

bits = 256
print("Bits =", bits)

rand_bin = binascii.unhexlify(''.join(random.choice("0123456789abcdef") for _ in range(bits // 4)))
rand_hex = binascii.hexlify(rand_bin)

print("Entropy: " + str(rand_hex))

sha256_hash = hashlib.sha256(rand_bin).hexdigest()
print("SHA256 Hash: " + str(sha256_hash))

raw_binary = bin(int(rand_hex, 16))[2:].zfill(bits)
checksum = bin(int(sha256_hash, 16))[2:].zfill(bits)[:bits // 32]

print("Raw Binary: " + raw_binary)
print("Checksum: " + checksum)

bin_result = str(raw_binary + checksum)

# Index word list with binary hash + checksum digits
# 11 digits are used in succession for unsigned 0-2047 indices
mnemonic = ' '.join(word_list[int(bin_result[i * 11:i * 11 + 11], 2)] for i in range(len(bin_result) // 11))

print("Mnemonic Length:", len(bin_result) // 11)
print("Mnemonic: " + mnemonic)


