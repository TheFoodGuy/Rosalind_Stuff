#The reverse order of PatternToNumber.py 
#a recursion problem
def main():
    #nucleotide_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
    print NumberToPattern(5437,7)


def NumberToPattern(num_position, seq_length):
    nuc_conversion = {0:'A', 1:'C', 2:'G', 3:'T'}
    if seq_length == 0: 
        return None
    elif seq_length == 1: 
        return nuc_conversion[num_position%4]
        #return numToalp(num_position%4)  
    next_value = num_position // 4 #1359 
    remainder = nuc_conversion[num_position%4]
    #remainder = numToalp(num_position % 4) #R 1 -> C 
    return NumberToPattern(next_value, seq_length-1) + remainder

# def numToalp(remainder_num):
#     base = '' 
#     if remainder_num == 0: 
#         base = 'A'
#     elif remainder_num == 1: 
#         base = 'C'
#     elif remainder_num == 2: 
#         base = 'G' 
#     elif remainder_num == 3: 
#         base = 'T'
#     return base

if __name__ == "__main__":
    main()