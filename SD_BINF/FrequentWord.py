#2 - checking for how frequent a particular pattern appears in a string 
genome_string = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
genome_pattern = 5
#genome_pattern is
def FrequentWords(text, k) : 
    #text - > genome_string 
    #k - > genome_pattern value 
    genome_count = {}
    for i in range(len(text) - k + 1): # < - from the instruction here
        pattern = text[i:k+i] 
        if pattern in genome_count: 
            genome_count[pattern] += 1
        else: 
            genome_count[pattern] = 1 
        max_count = max(genome_count.values())
    
    #target = [] # it prints the sequences with the greatest values, should be an even number of sequences 
    for k in genome_count: 
        if genome_count[k] == max_count: 
            print(k)
            #target.append(k) #there's really no point in doing this tho
            


FrequentWords(genome_string, genome_pattern)