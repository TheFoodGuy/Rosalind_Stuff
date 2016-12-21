#3 Approximate Pattern Matching Problem - find the number of patterns 
# that closely match to the reference pattern in the sting 
def main():
    with open('testingFille.txt', 'r') as read_file:
    #with open('/home/david/Downloads/dataset', 'r') as read_file: 
        read_input = read_file.read().split("\n")
    #print read_input[0]
    #print read_input[2]
    App_patternMatching(read_input[0], read_input[1], read_input[2])
    read_file.close()

def App_patternMatching(kmer,genome,mis_appear):
    holder = {}
    for i in range(len(genome)-len(kmer)+1):
        pattern = genome[i:len(kmer)+1]
        if sum(c1!=c2 for c1,c2 in zip(kmer, pattern)) <= mis_appear:  
            holder[i] = pattern
    
        

if __name__ == "__main__":
    f = open('appPat_ans.txt', 'w')
    main()
    f.close()