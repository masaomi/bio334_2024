

import sys

def load_fasta(fasta):  
    sequences = []      

    f = open(fasta)     
    for line in f:      
        if not line[0] == ">":  
            sequences.append(line.rstrip()) 
    f.close()           
    return sequences    


def calc_pi(sequences):       
    total_diff = 0  
    for i in range(0, len(sequences)):                      
        for j in range(i+1, len(sequences)):                
            for k in range(0, len(sequences[i])):           
                if not sequences[i][k] == sequences[j][k]:  
                    total_diff += 1                         
    
    num_sequences = len(sequences)                          
    len_sequence = len(sequences[0])                        
    combination = num_sequences*(num_sequences-1)/2.0
    PI = total_diff/combination                             
    pi = total_diff/combination/len_sequence                
    return pi


sequences = load_fasta(sys.argv[1])
print("pi =", calc_pi(sequences))

def calc_heterozygosity(sequences):
    num_sequences = len(sequences)
    len_sequence = len(sequences[0])
    het_count = 0

    for i in range(len_sequence):
        bases = [seq[i] for seq in sequences]
        base_set = set(bases)
        if len(base_set) > 1:  # Polymorphic site
            het_count += 1

    H = het_count / len_sequence
    return H

print("Heterozygosity (H) =", calc_heterozygosity(sequences))

def calc_theta(sequences):
    num_sequences = len(sequences)
    len_sequence = len(sequences[0])
    S = 0

    for i in range(len_sequence):
        bases = [seq[i] for seq in sequences]
        base_set = set(bases)
        if len(base_set) > 1:  # Polymorphic site
            S += 1

    a1 = sum(1.0 / i for i in range(1, num_sequences))
    theta = S / a1 / len_sequence
    return theta

print("Theta (θ) =", calc_theta(sequences))

