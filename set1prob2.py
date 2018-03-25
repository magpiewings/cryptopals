#!/usr/bin/python


def fixed_xor(a, b):
    result = ''
    xor = ''
    if len(a) != len(b):
        return 'false'
    for pair in zip(a, b):
        xor = ord(pair[0]) ^ ord(pair[1])
        result += chr(xor)
        return result
