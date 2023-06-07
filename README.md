
# BIP39 Mnemonic Generator

This script is a BIP39 mnemonic generator. BIP39 is a Bitcoin Improvement Proposal which defines the implementation of a mnemonic code or mnemonic sentence -- a group of easy to remember words -- for the generation of deterministic wallets.

## Functionality

1. Imports necessary modules:
   - `binascii`: for binary and ASCII conversions
   - `random`: for generating random numbers
   - `hashlib`: for SHA256 hash computations

2. Reads a word list from a text file named "wordlist.txt". This word list is used to convert binary strings into mnemonic phrases.

3. Defines the number of bits for the entropy.

4. Generates random binary data (entropy) and its SHA256 hash. It also generates a checksum from the hash.

5. Combines the entropy and checksum into a single binary string.

6. Breaks the binary string into segments of 11 bits each, uses each segment as an index into the word list, and joins the words to form the mnemonic phrase.

7. Prints the entropy, hash, raw binary, checksum, and mnemonic phrase.

## Requirements

- Python 3

## Usage

Run the script with Python:

```
python main.py
```

Ensure that the "wordlist.txt" file is in the same directory as the script. This file should contain 2048 words, one per line.

