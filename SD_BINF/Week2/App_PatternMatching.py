#3 Approximate Pattern Matching Problem - find the number of patterns 
# that closely match to the reference pattern in the sting 
def main():
    #with open('testingFille.txt', 'r') as read_file:
    with open('/home/david/Downloads/dataset_9_4.txt', 'r') as read_file: 
        read_input = read_file.read().split("\n")
    #print read_input[0]
    #print read_input[2] 
    #reading works here, double checking to make sure everything is good to go
    a = App_patternMatching(read_input[0], read_input[1], int(read_input[2]))
    f.write(" ".join(str(e) for e in a))
    read_file.close()

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

def App_patternMatching(kmer,genome,mis_appear):
    holder = []
    k = len(kmer)
    l = len(genome)
    for i in range(l-k):
        if mismatch_count(kmer, genome[i:i+k], mis_appear):
            holder = holder + [i]
    return holder 

if __name__ == "__main__":
    f = open('appPat_ans.txt', 'w')
    main()
    f.close()