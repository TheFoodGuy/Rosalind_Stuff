#3
#1.3 here or #3 on the textbook, not too sure really. 
#just finding the starting position of all the pattern 

def main():
    name = 'GACGATATACGACGATA'
    pattern = 'ATA'
    PatternMatching(name, pattern)

def PatternMatching(text, Pattern): 
    #count = []
    for i in range(len(text) - len(Pattern) + 1): #should go up to 2 
        if text[i:len(Pattern)+i] == Pattern:
            print ' ', i, ' ' 
            #count.append(i) 
    #return count



if __name__ == "__main__":
    main()