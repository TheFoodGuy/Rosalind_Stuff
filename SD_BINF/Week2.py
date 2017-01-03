#another compliation on week2 to make it easer to import 
from Week1 import NumberToPattern, PatternToNumber, reverse_complement_problem
#App_PatternCount.py 
def approximate_pattern_count(text, kmer, d):
    count = 0 
    l = len(text)
    k = len(kmer)
    for i in range(l-k+1):
        pattern = text[i:i+k]
        if mismatch_search(kmer, pattern ) <= d:
            count = count + 1 
    return count

#App_PatternMatching.py 
def App_patternMatching(kmer,genome,mis_appear):
    holder = []
    k = len(kmer)
    l = len(genome)
    for i in range(l-k):
        if mismatch_count(kmer, genome[i:i+k], mis_appear):
            holder = holder + [i]
    return holder 

#shew_diagram.py 
def shewSearch(genome):
    k = 0
    hold_num = {} 
    for i,v in enumerate(genome): #enumerate adds a counter to each index of the letter
        #print i,v 
        hold_num[i] = k
        if v == 'G':
            k = k + 1  
        elif v == 'C':
            k = k - 1
    #check to see if 11 and 24 have the lowest count
    #print hold_num
    min_count = min(hold_num.values())  
    new_hold = set()
    for i in hold_num:
        if hold_num[i] == min_count:
            print i
            new_hold.add(i)
    return new_hold

def HammingDistance(main_string, mis_string):
    count = 0 
    for i in range(len(main_string)):
        if main_string[i] != mis_string[i]:
            count += 1
    return count 

#mismatch_search / the old style 
def mismatch_search(main_string, mis_string):
    return sum(c1!=c2 for c1,c2 in zip(main_string,mis_string))

#mismatch_count 
def mismatch_count(kmer, genome, mis_appear):
    count = 0
    count = sum(c1!=c2 for c1,c2 in zip(kmer, genome))
    if count > mis_appear:
        return False
    return True
    # for k,v in zip(kmer, genome):
    #     if k != v : 
    #         count = count + 1 
    #     if count > mis_appear: 
    #         return False 
    # return True

#frequent mismatches search 
def frequent_mistmatches(Text, k, d):
    freq_pat = set()
    close = [0 for i in range(4**k)] 
    for i in range(0, len(Text)-k):
        neighborhood = neighbors(Text[i:k+i], d)
        for pattern in neighborhood:
            index = PatternToNumber(pattern)
            print index 
            print len(close)
            close[index] = close[index] + 1  
    maxCount = max(close)
    for i in range(0, 4**k -1):
        if close[i] == maxCount:
            pattern = NumberToPattern(i,k)
            freq_pat.add(pattern)
    return freq_pat

#frequent mismatches search including reverse complement
def frequent_mistmatches_rev(Text, k, d):
    freq_pat = set()
    close = [0 for i in range(4**k)] 
    for i in range(0, len(Text)-k):
        neighborhood = neighbors(Text[i:k+i], d) #reverse complement here seems to work here as well 
        for pattern in neighborhood:
            index = PatternToNumber(pattern)
            print index 
            print len(close)
            close[index] = close[index] + 1  
    maxCount = max(close)
    for i in range(0, 4**k -1):
        if close[i] == maxCount:
            pattern = NumberToPattern(i,k)
            freq_pat.add(pattern)
    return freq_pat

#ImmediateNeighbors -> usually used for iteratively finding neighbors 
def close_neighbors(Pattern):
    neighborhood = set() 
    for i in range(1, len(Pattern)):
        symbol = Pattern[i]
        for j in other_nucleotide(symbol):
            neighbor = Pattern[:i] + j + Pattern[i:]
            neighborhood.add(neighbor)
    return neighborhood

#neighbors but with a recursive pattern 
def neighbors(Pattern, d):
    if d == 0 : 
        return Pattern 
    if len(Pattern) == 1 : 
        return {'A', 'C', 'G', 'T'}
    neighborhood = set() 
    suffix_neighbhors = neighbors(suffix(Pattern), d)
    for Text in suffix_neighbhors:
        if HammingDistance(suffix(Pattern), Text) < d:
            for j in "ACGT":
                neighborhood.add(j + Text)
        else:
            neighborhood.add(first_symbol(Pattern) + Text)
    return neighborhood


def first_symbol(Pattern):
    return Pattern[0] 

def suffix(Pattern):
    return Pattern[1:len(Pattern)]
        
def other_nucleotide(symbol):
    cur_pick = "ACGT" 
    cur_nuc = '' 
    for i in cur_pick: 
        if i == symbol : continue
        cur_nuc += i 
    return cur_nuc
