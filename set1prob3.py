# !/usr/bin/env python3
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
from binascii import unhexlify, unhexlify


freq = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074,
}


def scorecharacter(s):
    score = 0
    for char in s:
        score += freq[char.lower()]
    return score


def singlebytexor(n, keyvalue):
    result = ''
    for char in n:
        result += bytes([char ^ keyvalue])
    return result


def babysfirstbruteforceattack(t):
    possible = []
    for key in range(256):
        cleartext = singlebytexor(t, key)
        possiblescore = scorecharacter(cleartext)
        likely = {'k': key, 's': possiblescore, 'c': cleartext}
        possible.append(likely)
