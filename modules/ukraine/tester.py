#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import colored
asdf = colored('2', 'yellow')
b = colored('b', 'magenta')
print(asdf)
for a in asdf:
    print(hex(ord(a)))

"""
0x1b 0x5b 0x33 0x35 0x6d 0x6d 0x6d 0x1b 0x5b 0x30 0x6d < magenta
0x1b 0x5b 0x33 0x31 0x6d 0x1b 0x5b 0x30 0x6d < red
0x1b 0x5b 0x33 0x33 0x6d 0x1b 0x5b 0x30 0x6d < yellow
  [    3    3    m     [    0    m
текст всавляется между 'm' и 
"""
bytearray(b'\x1b\x5b\x33\x35\x6d\x6d\x6d\x1b\x5b\x30\x6d')[2:4]
