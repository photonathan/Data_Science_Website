# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:45:36 2021

@author: MDNat
"""

## Reading and opening files
try:
    f = open('test.txt')
except IOError:
    print('the file does nCoot exist')
    
for line in f:
    print(line)

# If you first iterate through a document, you will be at the end.
# If you are at the end, you can't read anything else using .read()
f.read()
# You must use the .seek() method to go to the beginning
f.seek(0)
# Now .read() method works
f.read()
f.seek(0)
# .readline() reads the file line by line
f.readline()
# Open() defaults to 'r' read only
# If we want ot write to the file, specify 'a' to append
f = open('test.txt', 'a')
# .write() method writes the contents of a string to the file
f.write('This is a third line')
f.close()
# To read the file, open it in 'r' read mode
f = open('test.txt', 'r')
f.seek(0)
f.read()
f.close()

## Build a dictionary containing all sequences from a FASTA file
try:
    f = open('file.fa')
except IOError:
    print('the file does not exist')
seqs = {}
for line in f:
    # discard the newline and whitespace at the end of the line (if any)
    line = line.rstrip()
    # distinguish header from sequence
    if line[0] == '>': # can also use line.startswith('>')
        # Split method returns a list of words in a string default sep is white space
        words = line.split()
        # grabs the first word but ignores the first character which is a '>'
        name = words[0][1:]
        # Initialzes a new dictionary sequence
        seqs[name]=''
    else: # it's a sequence, not a header
        seqs[name] = seqs[name] + line
f.close()

## Retrieving Data from Dictionaries
# Retrieve the key and value from our dictionary using items() method
for name, seq in seqs.items():
    print(name,seq)

# Scirpts often need to process command line arguments.
# Suppose a script that parses a FASTA file is called processfasta.py
# and you want to run it on a file whose name we give as an argument in the command line
# >python processfasta.py myfile.fa
# The arguments of the above command are stored in the sys module's argv attribute as a list
import sys
print(sys.argv)