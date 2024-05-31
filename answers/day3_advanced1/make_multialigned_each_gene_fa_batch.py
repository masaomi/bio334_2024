#!/usr/bin/env python
# Version = '20210525-120309'

import sys
import os
OUTDIR = "multialigned_gene_fastas"
if not os.path.exists(OUTDIR):
  os.mkdir(OUTDIR)

f = open(sys.argv[1])
gene_list = []
for line in f:
  gid=line.rstrip()
  gene_list.append(gid)
f.close()
#print(len(gene_list))

import glob
files = glob.glob('Ath_*_genes.fa')
#print(files)

print("set -eu")
for gid in gene_list:
  out_fa = OUTDIR + "/" + gid + ".fa"
  for file in files:
    command = "python grep_fa.py " + file + " " + gid + " >> " + out_fa
    print(command)
