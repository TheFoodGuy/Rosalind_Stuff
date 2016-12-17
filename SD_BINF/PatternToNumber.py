#Honestly, I had no idea what they meant even with the limited explanation
#From my understanding, you line everything in alphabetically ordered for the four bases 
# base_index * 4 (the amount of bases to selected) ^ (length of the pattern) + ...
def main():
   print PatternToNumber('ATGCAA')
def PatternToNumber(Pattern):
    total = 0 
    nucleotide_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
    for i in range(len(Pattern)):
        total = total * 4 + nucleotide_to_number[Pattern[i]]
    return total
if __name__ == "__main__":
    main()

#Ex. ATGCAA 
# 0*4^5 + 3*4^4 + 2*4^3 + 1*4^2 + 0*4^1 + 0*4^0 = 912 