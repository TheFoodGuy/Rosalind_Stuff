#start this by the monday or so gotta finish up to week 4 by the time school starts 
from Week2 import neighbors, HammingDistance
#motif enumeration using brute force through the import of neighbor 
def motif_enumeration(Dna, k, d):
    pattern = set() 
    for i in range(0, len(Dna) - k + 1): 
        for kmer in neighbors(Dna[i:i+k], d):
            if HammingDistance(i,kmer) <= d:
            #if pattern' appears in each string from Dna with at most d mismatches  
                pattern.add(kmer)
    return pattern

    
# 3 1
# ATTTGGC
# TGCCTTA
# CGGTATC
# GAAAATT

# ATA ATT GTT TTT