#4 this is not like PatternMatch but PatternCount, in the sense that you have to find the number of matching patterns
def main():
    l = 'AGAGCGAAGGAGAAGGCCTATAACCTCTCAGCGAGATGAGGGTCTAGGTAACAATACCGTCTTGCGTTATGACTTCCGTTTCACATTTTCTTACCAGTCTAGGGTTCATGGGAATACCAGCTGCGTAAGTCTCCTATGGGTAAAAGCAACTAGAGTACGCAGTAGGCCTTCACTTGGTGAACGTTTGGGAAGGCGCACAGGACCGTTATGGCTGCAAGGATGCCAAAATCACCGGGTAGCGCAAGTCGTGGATACCAGCTTCTCACCCGCGTCCCGTATCAAAGCATCTTTAAACGTGTGCATGAGAGAAGAAA'
    kl = 'GTACGCA'
    d = 2 
    #f = open('/home/david/Downloads/test.txt','r')
    #read_file = f.read().split('\n')
    print approximate_pattern_count(l, kl, d)

def mismatch_search(main_string, mis_string):
    return sum(c1!=c2 for c1,c2 in zip(main_string,mis_string))

def approximate_pattern_count(text, kmer, d):
    count = 0 
    l = len(text)
    k = len(kmer)
    for i in range(l-k+1):
        pattern = text[i:i+k]
        if mismatch_search(kmer, pattern ) <= d:
            count = count + 1 
    return count

if __name__ == "__main__": 
    main()