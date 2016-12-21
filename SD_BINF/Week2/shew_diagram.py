#1 - find the min
#sample - TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
#ans: 11 24 (no idea why there's two answer at the moment) 
#i guess there's two answer because they are the two smallest

#file is too big to open and crashes gedit 
#just straight up read the file first
def main():
    in_file = open('/home/david/Downloads/dataset_7_6.txt','r')
    gen = in_file.read()
    a = shewSearch(gen)
    a = sorted(a)
    f.write(" ".join(str(e) for e in a))
    #print ' '.join(str(k))

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

if __name__ == "__main__":
    f = open('shew_ans.txt', 'w')
    main()
    f.close()

