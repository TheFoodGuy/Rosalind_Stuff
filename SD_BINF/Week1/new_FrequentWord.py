#improving FrequentWord.py performance 

def main():
    f = open('ans.txt', 'w')
    j = FrequentWords('AACTCGCCAGGCCCGAGAAGGCGAAAGAATGCCCGAAAACAAACAGATATTATAGGGGCCGTTAAAAGGCTCAGCCGTCGACTGATCGCCCCAACAGATGTTGACTGATCCAAACAACCTGTGGAGGTAACACTGATGGAACGCTCTGAGATTCTGAGGCACTATTTGCACCGCTATTCGTGCGTCGATAGTGGGGGGCCTCCGCGATTGGAGATAGGCCCCGAACACTGAGTTGCATACGGGCCAACCCAACTTGCGTATTGCATCAAGCGGAATGCCTCCTCTCTTCCAACCACTCGCCCGAACGAGAACGAACGTTCATCTCTGCGTCCAGACAATTACTACTCTCCATGTCAAAAGCTAGTGGTGCAGCTGCACAGTCTGTCAGAAAATCATCTGAAGATATTCCACGAGTGGGATGGATGAGCAGGCACCGAGACCGTCAACCGTGGCGATACGTCGGAACCGCACACCTGCAGAATTCAATTTGAATGGGTTCTGGGACTTGTTACCGTCCAAAGGAAGTTCGGAGGGTAGTACATAGTAGACTTAAAAAATGTGGCCTCGCCATGCATAGACGCAACGTGACGTTCTGACCATCCGAACTTGGAACCCTAGACCGGCGTGACAGCATACCCTGGCAGCTAGATCGTATTCGGCGAGAATAAAGTATAAACCCAGGGCAGCTTTGATTGGAAGTGTTGCTACTCCTATGGGTGTCTAATG', 7) 
    f.write(str(j))
    f.close()

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

def FrequentWords(Text, k):
    FrequencyArray = [0 for i in range((4**k))] 

    for i in range(0, len(Text)-k+1):
        pattern = Text[i:k+i]
        j = PatternToNumber(pattern)
        #print pattern #confirmation that everything was being taken into account 
        FrequencyArray[j] = FrequencyArray[j] + 1
        
    return FrequencyArray


if __name__ == "__main__":
    main()

    