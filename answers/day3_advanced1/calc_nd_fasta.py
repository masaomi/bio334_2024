

import sys

def load_fasta(fasta):  
    sequences = []      

    f = open(fasta)     
    for line in f:      
        if not line[0] == ">":  
            sequences.append(line.rstrip()) 
    f.close()           
    return sequences    


def nucleotide_diversity1(sequences):       
    total_diff = 0  
    for i in range(0, len(sequences)):                      
        for j in range(i+1, len(sequences)):                
            for k in range(0, len(sequences[i])):           
                if not sequences[i][k] == sequences[j][k]:  
                    total_diff += 1                         
    
    num_sequences = len(sequences)                          
    len_sequence = len(sequences[0])                        
    print("len_sequence: %d" % len_sequence)
    combination = num_sequences*(num_sequences-1)/2.0
    PI = total_diff/combination                             
    pi = total_diff/combination/len_sequence                
    return pi



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
            diff = count_diff(sequences[i], sequences[j])
            print("compare: %d, %d diff=%d" % (i, j, diff))
            total_diff += count_diff(sequences[i], sequences[j])
    return total_diff

def nucleotide_diversity2(sequences):
    num_sequences = len(sequences)
    len_sequence = len(sequences[0])
    combination = num_sequences*(num_sequences-1)/2.0
    total_diff = count_total_diff(sequences) 
    pi = total_diff/combination/len_sequence
    return pi

sequences = load_fasta(sys.argv[1])
print("Nucleotide diverisity pi =", nucleotide_diversity1(sequences))
print("Nucleotide diverisity pi =", nucleotide_diversity2(sequences))




