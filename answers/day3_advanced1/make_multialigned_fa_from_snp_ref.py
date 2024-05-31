
import sys
seq = ''
header = ''
file = open("Athaliana_SNPs/TAIR10_chr1.fas")
for line in file:
    if not line[0] == ">":
        seq += line.rstrip()
    else:
        header = line.rstrip()
        #print(line.rstrip())
file.close()
#print(seq[0:3])

seq = list(seq)
#print(seq[0:3])

#file = open("data/Athaliana_SNPs/quality_variant_108_TAIR10_Chr1.txt")
file = open(sys.argv[1])
new_seq = ''
for line in file:
    x = line.rstrip().split()
    #print(x[2], x[4])
    seq[int(x[2])-1] = x[4]
file.close()
#print("".join(seq)[0:10])
print(header)
print("".join(seq))
