#testing area to make sure everything is up to date 
from Week3 import motif_enumeration
def main():
    file_name = raw_input('what is the name of the file\n')
    file_name = '/home/david/Downloads/' + file_name
    with open(file_name) as in_file:
        read_input = in_file.read().split()

    a = frequent_mistmatches(read_input[0], int(read_input[1]), int(read_input[2]))
    a = list(a)
    f.write(' '.join(a)) 

if __name__ == "__main__":
    f = open('ans.txt', 'w')
    main()
    f.close()