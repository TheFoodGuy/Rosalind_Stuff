def find_pattern(p, q, d):
    count = 0
    for x, y in zip(p,q):
        if x != y: 
            count = count + 1
        if count > d:
            return False
    return True
	
def approximate_pattern_matching_problem(pattern, genome, d):
    pos = []
    k = len(pattern)
    l = len(genome)
    for i in range(l-k):
        if find_pattern(pattern, genome[i:i+k], d):
            pos = pos + [i]
    return pos
    
string =  "".join(open("testingFille.txt")).split()
f = open('appPat_ans.txt', 'w')
a = approximate_pattern_matching_problem(string[0], string[1], int(string[2]))
f.write(" ".join(str(e) for e in a))
f.close()
