#1.5 from FrequencyArray, apparently I didn't do this

def main():
    genome = 'CCTGGACACATAAGGAGGAGAGATGGGTGTTGGTAACGTTAACACGTCCCGGAGTATACCACGTTGGACACCGCGCTGCTGTGTCTTCGTTGCTGACTATCCTGCTACTCAAAGGTGGAAGCCTACTGGGTTTTTCCAGGATCGCGTCCTTACAAGGTTTAAGGGTTTCGGGCGTCAAGTAGACCTCTCAGGTGCCGTTCGGCGGGCAGTAACGGCTGCCGTAACACTCTGGCCACTTAGATGGCGAGGGAACTCAGTAGTGTCGCGTCCGGCGATAGGCGCTGGTACGACCATAAATCACATCACTCAGAGCCGTCCCTCACGCCCAGCCGATTACTTCCAAGATTTCATCTCCTGATACATAGCCCCGAAGTGACTATGATATACCCTTCTCTAGGTGCATACGCGCCCGCAACTAATCGCAGGCGTACTTTAACCGTTTAGCTATTACTTTCACGCACGAAAGACTTGTCAGGAACCAAACGACCCTATTAGCATCAGTCTTGAATCGCAGTACCAGCACGATAGATTTATCAGCGTAAAAGTCACCGTTGGGGAAGCTTCGCACTACTTCTCCAGTCCTTGAATTCCTATTCGCTGTGGATTACACAGTGTTTAATACAGTAAGGTGGGCACGCGAAATTGCGGAAAGCCCCATGTATTGTCGGAGACGACACAAAGACTTTCTTCACCACGATCTAGTAGTGCGTAATCTGTGGTGGCCAATCGTGCTTGCATTTGCCACAA' 
    k = 8
    a = ComputingFrequencies(genome, k)
    f.write(str(a))

def PatternToNumber(Pattern):
    total = 0 
    nucleotide_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
    for i in range(len(Pattern)):
        total = total * 4 + nucleotide_to_number[Pattern[i]]
    return total

def NumberToPattern(num_position, seq_length):
    nuc_conversion = {0:'A', 1:'C', 2:'G', 3:'T'}
    if seq_length == 0: 
        return None
    elif seq_length == 1: 
        return nuc_conversion[num_position%4]
    next_value = num_position // 4 #1359 
    remainder = nuc_conversion[num_position%4]
    return NumberToPattern(next_value, seq_length-1) + remainder


def ComputingFrequencies(Text, k):
    FrequencyArray = [0] * (4**k)
    for i in range(len(Text)-k+1):
        Pattern = Text[i:k+i]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1 
    return FrequencyArray

if __name__ == "__main__":
    f = open('ans.txt', 'w')
    main()
    f.close()