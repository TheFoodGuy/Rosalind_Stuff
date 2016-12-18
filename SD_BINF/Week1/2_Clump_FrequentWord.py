#Improving Clump finding algorithm, hopefully this doesn't take more than 10 mins or so 
def main():
    genome_string = 
    pat_length = 12
    wind_length = 525
    appearance= 17
    a = find_clump(genome_string, pat_length, wind_length, appearance)
    #print str(a) checking to see if it's sorted 
    f.write(' '.join(a))


def PatternToNumber(Pattern):
    if Pattern == '':
        return 0 
    nucleotide_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
    last_value = Pattern[-1]
    rem_pat = Pattern[:len(Pattern)-1] #ATGCA | A 
    return 4 * PatternToNumber(rem_pat) + nucleotide_to_number[last_value]

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

def find_clump(genome, k , L , t):
    FrequentPat = set()
    Clump = [0] * (4**k - 1) #seems really wasteful here 
    Text = genome[0:L]
    FrequencyArray = FrequentWords(Text, k)
    for i in range (4**k - 1):
        if FrequencyArray[i] >= t: 
            Clump[i] = 1
    for i in range(1, len(genome)-L):
        first_pattern = genome[i-1:i-1+k] #double check here | genome(i-1, k) 
        index = PatternToNumber(first_pattern)
        print index , len(FrequencyArray)
        print ("im here")
        FrequencyArray[index] = FrequencyArray[index] - 1
        last_pattern = genome[i+L-k: L+i] #genome(i + L - k, k)
        index = PatternToNumber(last_pattern)
        FrequencyArray[index] = FrequencyArray[index] + 1
        if FrequencyArray[index] >= t: 
            Clump[index] = 1 
    for i in range(4**k - 1): 
        if Clump[i] == 1: 
            Pattern = NumberToPattern(i, k)
            FrequentPat.add(Pattern)
    return FrequentPat

# def find_clump(genome, k, L, t):
#     FrequentPat = set()
#     Clump = [0] * (4**k - 1)
#     for i in range(0, len(genome)-L):
#         Text = genome[i:i+L]
#         FrequencyArray = FrequentWords(Text, k)
#         for index in range(0, 4**k - 1):
#             if FrequencyArray[index] >= t:
#                 Clump[index] = 1 
#     for i in range(0, 4**k - 1):
#         if Clump[i] == 1: 
#             Pattern = NumberToPattern(i,k)
#             FrequentPat.add(Pattern)
#     return sorted(FrequentPat)

if __name__ == "__main__":
    f = open('ans.txt', 'w')
    main()
    f.close()