#1 - I could not solve the app_PatternMatching due to a number of random reasons 
#even though i had the correct answers for both the example and dataset
#with regards, here's the reference link : https://github.com/minw2828/Coursera---Bioinformatics-Algorithms/blob/master/chapter1/C1_8/8_3/approximate_pattern_match.py

import sys

def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    return data
    f.close()

def comparison(pattern,text):
    i,count = 0,0    
    while i < len(pattern):
        if pattern[i] != text[i]:
            count += 1
        i += 1
    return count

def approximate(pattern,text,d):
    i, result = 0, []
    while i < len(text)-len(pattern)+1:
        if comparison(pattern,text[i:i+len(pattern)]) <= d:
            result.append(i)
        i += 1
    return result

if __name__ == '__main__':

    pattern, text, d = [item.strip() for item in read_file('/home/david/Downloads/dataset_9_4.txt')]
    d = float(d)
    result = approximate(pattern,text,d)
    
    fw = open('output.'+sys.argv[-1][:-4]+'.txt','w')
    fw.write(' '.join(map(str,result)))
    fw.close()