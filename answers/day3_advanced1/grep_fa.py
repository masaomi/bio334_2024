#!/usr/bin/env python
# Version = '20170517-112706'
# $ python --version
# Python 3.6.0 :: Anaconda 4.3.1 (x86_64)

import sys
import os.path

def load_fasta(fasta):  
    sequences = {}

    f = open(fasta)     
    gid = ""
    for line in f:      
        if line[0] == ">":  
          gid = line.replace(">", "").rstrip()
          sequences[gid] = ""
        else:
          sequences[gid] += line.rstrip()
    f.close()           
    return sequences

if not (__name__ == "__main__" and len(sys.argv) > 2):
  print('usage:')
  print(' python ',__file__, ' [fasta] [gid]')
else:
  sequences = load_fasta(sys.argv[1])
  gid = sys.argv[2]
  file_basename = os.path.basename(sys.argv[1]).replace(".fa", "")
  print(">", file_basename, "_", gid, sep="")
  print(sequences[gid])

