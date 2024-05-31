import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dat = pd.read_table("Athaliana_chr1_genes_pi.dat")
dat = dat.set_index('GeneID')
plt.plot(dat['PI'])
plt.xticks([])
plt.ylabel("PI")
plt.xlabel("Genes")
plt.savefig("Athaliana_chr1_genes_pi.png")
plt.show()

