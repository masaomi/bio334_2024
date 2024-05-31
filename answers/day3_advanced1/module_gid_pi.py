
import os
import sys
import math

def load_fasta(fasta):
    sequences = []

    f = open(fasta)
    for line in f:
        if not line[0] == ">":
            sequences.append(line.rstrip())
    f.close()
    return sequences

def count_diff(seq1, seq2):
    diff = 0
    for i in range(0, len(seq1)):
        if not seq1[i] == seq2[i]:
            diff += 1
    return diff

def count_total_diff(sequences):
    total_diff = 0
    for i in range(0, len(sequences)):
        for j in range(i+1, len(sequences)):
            total_diff += count_diff(sequences[i], sequences[j])
    return total_diff



def count_seg_sites(sequences):
    total_seg_sites = 0
    for i in range(0, len(sequences[0])):
        alleles = []
        for seq in sequences:
            alleles.append(seq[i])
        if len(set(alleles)) > 1:
            total_seg_sites += 1
    return total_seg_sites

def nucleotide_diversity(sequences):
    num_sequences = len(sequences)
    len_sequence = len(sequences[0])
    combination = num_sequences*(num_sequences-1)/2.0
    total_diff = count_total_diff(sequences) 
    pi = total_diff/combination/len_sequence
    return pi

def gid_pi(fasta_file_path):
    sequences = load_fasta(fasta_file_path)
    nd = nucleotide_diversity(sequences) 
    gene_id = os.path.basename(fasta_file_path).replace('.fa', '')
    return "\t".join([gene_id, str(nd)])







