import pandas as pd
import csv
import numpy as np

HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode("utf-8", "ignore")
    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])
        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3
        results.append(f'{i:04x}  {hexa:<{hexwidth}}  {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results

buffer = b"\x10 \x00\x04MQTT\x04\xc2\x00<\x00\x00\x00\x08username\x00\x08password0\xf0\x9d\x85\xa0\x0e\x0b\xc0\x80\x08dev/testMQTT0\x0e\x00\x08dev/testMQTT\x8e\xca\xb7\xb6MQTT0\x0e\x00\x08dev/testMQTT0\x0e\x00\x08dev/testMQTT-1\x0e\x00\x08dev/testMQTT0\x0e\x00\x08dev/testMQTT0\x0e\x00\x08dev/t\xe2\x81\xa9estMQTT0\x0e\x00\x08dev/testMQTT0\x0e\x00\x08d\xe2\x80\xabev/testMQTT0\x0e\x00\x08dev/testMQTT65535\x0e\x08dev/testMQTT0\x0e\x00\x08dev/testMQTT8\x0e\x00\x08dev/testMQTT\xe0\x000"

print(buffer)
hexdump(buffer)