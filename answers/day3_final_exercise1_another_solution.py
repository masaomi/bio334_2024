

import glob

seq_length = 4

def load_snps(path):
    snps = {}
    f = open(path)
    for line in f:
        pos = line.split()[2]
        nuc = line.split()[4]
        snps[pos] = nuc
    f.close()
    print(path, ": ", sorted(snps.items()))
    return snps

def all_positions(samples):
    all_positions_ = []
    for sample in samples:
        all_positions_ += sample.keys()
    return sorted(list(set(all_positions_)))

def insert_N(samples):
    for sample in samples:
        for pos in all_positions(samples):
            if not pos in sample:
                sample[pos] = 'N'

def count_nucleotide_difference(snps0, snps1):
    pos1 = set(snps0.keys())
    pos2 = set(snps1.keys())
    comm_pos = pos1 & pos2

    diff = 0
    for pos in comm_pos:
        if not snps0[pos] == snps1[pos]:
            diff += 1
    return diff

def calculate_pi(snps):
    total_diff = 0
    count_compare = 0
    for i in range(0, len(snps)):
        for j in range(i+1, len(snps)):
            diff = count_nucleotide_difference(snps[i], snps[j])
            print("compare: sample%d & sample%d: diff=%d" % (i+1, j+1, diff))
            total_diff += diff
            count_compare += 1

    pi = float(total_diff) / count_compare / seq_length
    return pi


# main
samples = []
for file_name in glob.glob("*.vcf"):
    samples.append(load_snps(file_name))
insert_N(samples)
print("pi = %f" % calculate_pi(samples))

