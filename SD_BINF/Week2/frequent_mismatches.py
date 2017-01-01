#trying again with frequent words with mismatches problems 
from App_PatternCount import mismatch_search, approximate_pattern_count
from Neighbors import Neighbor

def PatternToNumber(Pattern):
    if Pattern == '':
        return 0 
    nucleotide_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
    if len(Pattern) > 0: 
        substr = len(Pattern) - 1 
    else: 
        substr = 0 
    last_value = Pattern[0:substr]
    last_symbol = nucleotide_to_number[Pattern[-1]]
    return 4 * PatternToNumber(last_value) + last_symbol


def NumberToPattern(num_position, seq_length):
    nuc_conversion = {0:'A', 1:'C', 2:'G', 3:'T'}
    if seq_length == 0: 
        return None
    elif seq_length == 1: 
        return nuc_conversion[num_position%4]
    next_value = num_position // 4 #1359 
    remainder = nuc_conversion[num_position%4]
    return NumberToPattern(next_value, seq_length-1) + remainder


def frequent_mismatches(text, k , d):
    freq_pattern = set()
    close = [0] * (4**k-1)
    for i in range(len(text) - k):
        Neighborhood = Neighbor(text[i:k+i],d)
        for i in Neighborhood:
            index = PatternToNumber(i)
            close[index] = close[index] + 1 
    maxCount = max(close)
    for i in range(4**k-1):
        if close[i] == maxCount:
            pattern = NumberToPattern(i,k)
            freq_pattern.add(pattern)
    return freq_pattern

def main():
    # with open('testingFille.txt', 'r') as in_file: 
    #     read_input = in_file.read().split('\n')
    # #print read_input[0], read_input[1], read_input[2]
    # print frequent_mismatches(read_input[0], int(read_input[1]), int(read_input[2]))
    #f.write(frequent blah)
    k_1 = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k_2 = 4
    k_3 = 1
    print frequent_mismatches(k_1, k_2, k_3)
    
if __name__ == "__main__":
    f = open('frequent_ans.txt', 'w')
    main()
    f.close()