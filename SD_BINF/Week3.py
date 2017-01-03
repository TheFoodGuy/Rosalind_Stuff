#start this by the monday or so gotta finish up to week 4 by the time school starts 
from Week2 import neighbors, HammingDistance
#motif enumeration using brute force through the import of neighbor 
def motif_enumeration(Dna, k, d):
    # pattern = list()
    # for cur_dna in Dna:
    #     for i in range(0, len(cur_dna) - k + 1): 
    #         kmer = cur_dna[i:i+k] #this is the pattern on the string 
    #         for n_kmer in neighbors(kmer, d): #this creates the mismatch patterns 
    #             if HammingDistance(kmer, n_kmer) <= d:
    #                 pattern.append(kmer)
    pattern = []
    for cur_dna in Dna: 
        for i in range(len(cur_dna) - k + 1): 
            kmer = cur_dna[i:i+k] 
            for j in neighbors(cur_dna[i:i+k], d):
                pattern.append(j)
    a = [] 
    for i in pattern: 
        if i not in a: 
            a.append(i)
    print a 

            


    
# 3 1
# ATTTGGC
# TGCCTTA
# CGGTATC
# GAAAATT

# ATA ATT GTT TTT
