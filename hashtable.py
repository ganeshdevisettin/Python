#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:45:10 2021

@author: ganeshdevisetti
"""

class HashTable:
    def __init__(self, probe_incr):
        self.MAX = 11
        self.prime = self.closest_prime_number(self.MAX)
        print(self.prime)
        if (probe_incr == 'linear' or probe_incr == 'quadratic'  
            or probe_incr == 'double hash'):
            self.probe_incr = probe_incr
            self.arr = [None for i in range(self.MAX)]
        elif probe_incr == 'sep chaining':
            self.probe_incr = probe_incr
            self.arr = [[] for i in range(self.MAX)]
        else:
            raise Exception("Probe increment/separate chaining\
 must be specified\noptions include 'linear', 'quadratic', 'double hash',\
 'sep chaining'")
    
    def get_hash(self, key):
        return sum([ord(ch) for ch in key]) % self.MAX
    
    def get_hash2(self, key):
        return self.prime - (self.get_hash(key) % self.prime)
        
    def closest_prime_number(self, num):
        while True:
            i = 2
            while i < num//2+1:
                if num % i == 0 or num == self.MAX:
                    num -= 1
                    break
                i += 1
            if i == num//2+1:
                break
        return num
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        i = h
        count = 1
        removed = -1
        found = False
        if self.probe_incr != "sep chaining":
            while count < self.MAX+1 and self.arr[i] != None:
                if removed == -1 and self.arr[i] == ():
                    removed = h
                elif self.arr[i] != () and self.arr[i][0] == key:
                    found = True
                    break
                i = (h + self.probe_increment(key, count)) % self.MAX
                count += 1
            if found: 
                self.arr[i] = (key, val)
            elif removed != -1:
                self.arr[removed] = (key, val)
            elif self.arr[i] == None:
                self.arr[i] = (key, val)
            else:
                print("\nException: Overflow\ncannot insert" \
                                + str((key, val)) + '\n')
            # for error checking
            print(str(t.arr) + '\n')
        else:
            for idx, elem in enumerate(self.arr[h]):
                if elem[0] == key:
                    self.arr[h][idx] = (key, val)
                    found = True
                    break
            if not found:
                self.arr[h].append((key, val))
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.probe_incr != "sep chaining":
            return self.probe_handler(h, key, False)
        else:
            for elem in self.arr[h]:
                if elem[0] == key:
                    return elem[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.probe_incr != "sep chaining":
            self.probe_handler(h, key, True)
        else:
            for idx, elem in enumerate(self.arr[h]):
                if elem[0] == key:
                    del self.arr[h][idx]
    
    def probe_handler(self, h, key, isDel):
        idx = self.probe(h, key)
        if idx != None:
            if isDel:
                self.arr[idx] = ()
            else:
                return self.arr[idx][1]
        
    def probe(self, h, key):
        count = 1
        i = h
        while self.arr[i] == None or self.arr[i] == () or \
                self.arr[i][0] != key:
            if count == self.MAX:
                break
            i = (h + self.probe_increment(key, count)) % self.MAX
            count += 1
        if count != self.MAX:
            return i
    
    def probe_increment(self, key, count):
        if self.probe_incr == "linear":
            return 1
        elif self.probe_incr == "quadratic":
            return count**2
        else:
            h2 = self.get_hash2(key)
            return count*h2

# creates hashtable which reads in input from file
t = HashTable('sep chaining')
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
# print(t['march 24'])
# del t['march 26']
# print(t.arr)
# del t['march 26']
# print(t.arr)
# t['march 24'] = 404
# print(t.arr) 

# for x in t.arr:
#     if t.probe_incr != "sep chaining":
#         if x != None and x != () and x[0] != 'march 24':
#             del t[x[0]]
#     else:
#         if x != []:
#             x_len = len(x)
#             for i in range(x_len):
#                 if x[0][0] != 'march 24':
#                     del t[x[0][0]]
# print(t.arr)
# del t['march 24']
# print(t.arr)
# t['march 24'] = 489
# print(t.arr)
