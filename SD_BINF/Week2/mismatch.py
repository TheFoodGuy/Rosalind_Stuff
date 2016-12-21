#2 find the amount of mismatches in between two given strings 
def main():
    in_file = open('/home/david/Downloads/dataset_9_3.txt','r')
    read_file = in_file.read().split("\n")
    #print read_file[0] 
    #print read_file[1]
    a = mismatch_search(read_file[0], read_file[1])
    f.write(str(a))

def mismatch_search(main_string, mis_string):
    return sum(c1!=c2 for c1,c2 in zip(main_string,mis_string))

if __name__ == "__main__":
    f = open('mismatches.txt','w')
    main()
    f.close() 