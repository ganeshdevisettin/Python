#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 11:32:18 2021

@author: ganeshdevisetti
"""

import random

#hash table with ten spots assumed
#displays hash values of dates

HASH_TABLE_LENGTH = 11

def get_hash(key):
    h = 0
    for ch in key:
        h += ord(ch)
    return h % HASH_TABLE_LENGTH

hash_dict = {}

#reads dates from file
with open("dates.txt", "r") as f:
    #creates dictionary
    for line in f:
        date = line.split(',')
        if len(date) > 1:
            date = date[0:]
            try:
                date = date[0].lower()
                date_hash = get_hash(date)
                #in dict, key = date_hash and value = date
                if date_hash in hash_dict:
                    hash_dict[date_hash].append(date)
                else:
                    hash_dict[date_hash] = [date]
            except:
                continue

hash_arr = [[]]*HASH_TABLE_LENGTH
#transfers values from dictionary to array
#so that hash values can be ordered
for key in hash_dict:
    hash_arr[key] = hash_dict[key]

#displays hash_arr for quality assurance
print("Your dates hash table looks like this: " + '\n')
print(hash_arr)    

#displays hash values with all associated dates
def display_all_date_hashes():
    for x in range(len(hash_arr)):
        print(str(x) + ":", end=' ')
        print(hash_arr[x])
        
#displays a key-value list with each key hashing to
#different area in hash table
def display_random_date_val_list():
    for x in hash_arr:
        if x != []:
            #creates random index
            num = int(random.random()*len(x))
            #uses num to grab random date
            print(x[num] + ',' + str(int(random.random()*500)))
        else:
            print('(no value)')
            
def display_random_random_date_val_list():
    date_table = []
    for x in range(HASH_TABLE_LENGTH):
        y = int(random.random()*HASH_TABLE_LENGTH)
        if hash_arr[y] != []:
            #creates random index
            num = int(random.random()*len(hash_arr[y]))
            #changes indexes if arr[y][num] already in list
            while hash_arr[y][num] in date_table:
                y = int(random.random()*HASH_TABLE_LENGTH)
                num = int(random.random()*len(hash_arr[y]))
            date_table.append(hash_arr[y][num])
            #uses num to grab random date
            print(hash_arr[y][num] + ',' + str(int(random.random()*500)))
        else:
            print('(no value)')

def display_random_random_date_val_list_with_index():
    date_table = []
    for x in range(HASH_TABLE_LENGTH):
        y = int(random.random()*HASH_TABLE_LENGTH)
        if hash_arr[y] != []:
            #creates random index
            num = int(random.random()*len(hash_arr[y]))
            #changes indexes if arr[y][num] already in list
            while hash_arr[y][num] in date_table:
                y = int(random.random()*HASH_TABLE_LENGTH)
                num = int(random.random()*len(hash_arr[y]))
            date_table.append(hash_arr[y][num])
            #uses num to grab random date
            print(hash_arr[y][num] + ',' + str(int(random.random()*500)) + 
                  ',' + str(y))
        else:
            print('(no value)')
