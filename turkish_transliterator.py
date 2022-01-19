#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 08:43:20 2022

@author: ganeshdevisetti
"""

"""Turkish words are often not transliterated correctly in English. 
For example, soft g (ğ) is often transliterated as g, resulting in
catastrophes such as 'Nemrut Dag', which don't reflect how the phrase is
pronounced in Turkish language. This program will transliterate Turkish words to 
the closest corresponding English pronunciation."""

print("Type/paste input into console, press Control-D when finished.")
text = ''
while True:
    try:
        text = input()
    except EOFError:
        break
processed = ''
b = 0
while b < len(text):
    if text[b] == 'ü':
        processed += 'u'
    elif text[b] == 'Ü':
        processed += 'U'
    elif text[b] == 'ö':
        processed += 'o'
    elif text[b] == 'Ö':
        processed += 'O'
    elif text[b] == 'ı':
        processed += 'i'
    elif text[b] == 'ş':
        processed += 'sh'
    elif text[b] == 'Ş':
        processed += 'Sh'
    elif text[b] == 'ç':
        processed += 'ch'
    elif text[b] == 'Ç':
        processed += 'Ch'
    elif text[b] == 'c':
        processed += 'j'
    elif text[b] == 'C':
        processed += 'J'
    elif text[b] == 'İ':
        processed += 'I'
    elif text[b] == 'ğ':
        if b+1 == len(text) or text[b-1] != text[b+1]:
            processed += 'h'
        elif text[b-1].lower() == 'e' or text[b-1].lower() == 'i':
            processed += 'y'
        else:
            processed += 'h'
            b += 1
    else:
        processed += text[b]
    b += 1

print(processed)