import sys
import socket
import threading

# Contains ASCII printable characters if one exists, or a . if
# it does not exist. The representation of printable characters
# have a length of 3.
HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)]
)

def hexdump(src, length=16, show=True):
    # Ensure a byte string is passed
    if isinstance(src, bytes):
        src = src.decode()

    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])

        # Get string representation of the characters
        printable = word.translate(HEX_FILTER)

        # Get hexadecimal representation of chatacters
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3

        # Contains the hex value of the index of the first byte in the word
        # (in hex), the hex value of the word, and printable representation.
        results.append(f'{i:04x}    {hexa:<{hexwidth}}  {printable}')

    if show:
        for line in results:
            print(line)
    else:
        return results

hexdump('test string\n foo bar\n')

