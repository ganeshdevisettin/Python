#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:45:10 2021

@author: ganeshdevisetti
"""

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        return sum([ord(ch) for ch in key]) % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        count = 1
        removed = -1
        found = False
        while count < self.MAX+1 and self.arr[h] != None:
            if removed == -1 and self.arr[h] == ():
                removed = h
            elif self.arr[h] != () and self.arr[h][0] == key:
                found = True
                break
            h = (h+1) % self.MAX
            count += 1
        if found: 
            self.arr[h] = (key, val)
        elif removed != -1:
            self.arr[removed] = (key, val)
        elif self.arr[h] == None:
            self.arr[h] = (key, val)
        else:
            print("\nException: Hashtable full\ncannot insert" \
                            + str((key, val)) + '\n')
        
    def __getitem__(self, key):
        return self.probe_handler(key, False)
    
    def __delitem__(self, key):
        self.probe_handler(key, True)
    
    def probe_handler(self, key, isDel):
        h = self.get_hash(key)
        idx = self.probe(h, key)
        if idx != None:
            if isDel:
                self.arr[idx] = ()
            else:
                return self.arr[idx][1]
        
    def probe(self, h, key):
        count = 1
        while self.arr[h] == None or self.arr[h] == () or \
                self.arr[h][0] != key:
            if count == self.MAX:
                break
            h = (h+1) % self.MAX
            count += 1
        if count != self.MAX:
            return h

# creates hashtable which reads in input from file
t = HashTable()
# file must be formatted as dates2.txt in order for input
# reading to work
# dates2.txt format:
# key,val
# key,val
# etc..
with open("dates2.txt", "r") as f:
    for line in f:
        try:
            toAdd = line.split(',')
            toAdd[1] = int(toAdd[1].strip())
            t[toAdd[0]] = toAdd[1]
        except:
            print("Invalid line")

# test code

# print(t.arr)
# del t['march 7']
# print(t.arr)
# t['march 17'] = 45
# print(t.arr)
# t['march 26'] = 234
# print(t.arr)
# print(t['march 18'])
# del t['march 26']
# print(t.arr)
# del t['march 26']
# print(t.arr)
# t['march 24'] = 404
# print(t.arr) 

# for x in t.arr:
#     if x != None and x != () and x[0] != 'march 24':
#         del t[x[0]]
# print(t.arr)
# del t['march 24']
# print(t.arr)
# t['march 24'] = 489
# print(t.arr)
       
        
        
        
        
        