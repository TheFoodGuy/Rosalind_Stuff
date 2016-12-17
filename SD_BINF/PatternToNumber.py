#Honestly, I had no idea what they meant even with the limited explanation
#From my understanding, you line everything in alphabetically ordered for the four bases 
# base_index * 4 (the amount of bases to selected) ^ (length of the pattern) + ...
def main():
   print PatternToNumber('ATGCAA')

def PatternToNumber(Pattern):
    if Pattern == '':
        return 0 
    nucleotide_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
    last_value = Pattern[-1]
    rem_pat = Pattern[:len(Pattern)-1] #ATGCA | A 
    return 4 * PatternToNumber(rem_pat) + nucleotide_to_number[last_value]

if __name__ == "__main__":
    main()

#Ex. ATGCAA 
# 0*4^5 + 3*4^4 + 2*4^3 + 1*4^2 + 0*4^1 + 0*4^0 = 912 