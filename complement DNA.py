# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:31:32 2021

@author: MDNat
"""

dna = 'AGTGTGGGGC'

def complement(dna):
    base_complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A','N':'N', 'a':'t', 'c':'g', 'g':'c', 't':'a', 'n':'n'}
    letters = list(dna)
    letters = [base_complement[base] for base in letters]
    return ''.join(letters)


complement(dna)


sentence = 'enzymes and other proteins come in many shapes'
# Split method returns a list of words in a string
sentence.split()
# Split defaults to split on white spaces but you can define a separator
sentence.split('and')

# Join will return a string which the elements were joined from a list
'-'.join(['enzymes', 'and', 'other', 'proteins', '...'])

