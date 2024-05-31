

import sys
import glob # import glob module to use glob method
import os   # import os module to use system method
from module_gid_pi import gid_pi # import a custom module

print("GeneID\tPI")
for file in sorted(glob.glob(sys.argv[1] + "/*.fa")): # iterate all athal_chr*.fa files
  print(gid_pi(file))
