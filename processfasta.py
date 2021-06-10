#!/user/bin/python
"""
processfasta.py builds a dictionary with all sequences from a FASTA file.
"""

import sys
import getopt

filename=sys.argv[1]

try:
    f = open(filename)
except IOError:
    print(f'the file {filename} does not exist')

def usage():
  print("""
  processfasta.py : reads a FASTA file and builds a dictionary with all sequences bigger than a given length
  
  processfasta.py [-h] [-l <length>] <filename>
  
    -h            print this message
    -l <length>   filter all sequences with a length smaller than <length>
                  (default <length>=0)
    <filename>    the file has to be in FASTA format
    
    """)

o, a = getopt.getopt(sys.argv[1:], 'l:h')
opts = {}
seqlen = 0

for k,v in o:
  opts[k] = v

if '-h' in opts.key():
  # You can put two lines of code on one line with a ';'
  usage(); sys.exit()

if len(a) <1:
  usage(); sys.exit("input fasta file is missing")

if '-l' in opts.key():
  if int(opts['1'])<0:
    print("Length of sequence should be positive!"); sys.exit(0)
  seqlen = opts['-l']



