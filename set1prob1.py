#!/usr/bin/env python3
# convert hex to base64
# hex: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# base64: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
import binascii

# returns Base64 encoding of a hexidecimal string


def hextoBase64(hex):
    return binascii.b2a_base64(binascii.unhexlify(hex))


def hextor(hex):
    r = binascii.unhexlify(hex)
    return r
