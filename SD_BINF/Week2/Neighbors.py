#5 - it is to create a set of all k-mers whose hamming distance from Pattern does not 
# exceed d (or the number of mismatches/appearance)

def main():
    with open ('/home/david/Downloads/dataset_3014_3.txt', 'r') as read_file: 
        read_input = read_file.read().split('\n')
    print read_input[0]
    print 'hi'
    print read_input[1]
    f = open('neighbor_ans.txt', 'w')
    f.write('\n'.join(Neighbor(read_input[0], int(read_input[1])))) #this format works with the answer 
    f.close()

def Neighbor(pattern, d):
    #i don't quite understand the pseudocode here, so im using another person's as reference 
    #http://stackoverflow.com/questions/35106626/implement-neighbors-to-find-the-d-neighborhood-of-a-string-in-python
    chars = "ACGT" 
    assert(d <= len(pattern)) #condition to check if d is less than or equal to the length of pattern

    if d == 0:
        return [pattern] #returns the rest of pattern if d == 0 

    r2 = Neighbor(pattern[1:], d-1) #recursively call the function till d == 0 or if pattern is less than d
    r = [c + r3 for r3 in r2 for c in chars if c != pattern[0]] #does the magic here

    if (d < len(pattern)):
        r2 = Neighbor(pattern[1:], d)
        r += [pattern[0] + r3 for r3 in r2]

    return r
      

if __name__ == "__main__":
    hold = ['A', 'C', 'G', 'T']
    main()