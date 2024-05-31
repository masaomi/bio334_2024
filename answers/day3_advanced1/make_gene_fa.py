#!/usr/bin/env python
# Version = '20170517-111151'
# $ python --version
# Python 3.6.0 :: Anaconda 4.3.1 (x86_64)

import sys

def load_fasta(fasta):  
    sequences = []      

    f = open(fasta)     
    for line in f:      
        if not line[0] == ">":  
            sequences.append(line.rstrip()) 
    f.close()           
    return "".join(sequences)

def load_gff(gff):
    genes = []
    f = open(gff)
    for line in f:
      if not line[0] == "#":
        annotation = line.split()
        anno = annotation[2]
        if anno == "gene":
          chrn = annotation[0]
          sp = int(annotation[3])
          ep = int(annotation[4])
          last_anno = annotation[-1]
          gid_ = last_anno.split(";")[0]
          gid = gid_.split("=")[-1]
          genes.append([sp,ep,gid])
    return genes

def make_genes_fa(seq, genes):
    for sp,ep,gid in genes: 
      print(">", gid, sep="")
      print(seq[sp-1:ep])

if not (__name__ == "__main__" and len(sys.argv) > 2):
  print('usage:')
  print(' python ',__file__, ' [fasta] [gff]')
else:
  sequence = load_fasta(sys.argv[1])
  genes = load_gff(sys.argv[2])
  make_genes_fa(sequence, genes)

