#Please note that this is not my work but someone else work that i used to check myself 
#for some reasons my code would not remove duplicates and it was slightly making me mad
#i might come back later on and create my own code, but it's from joeslind guy 
from Week2 import neighbors
def motif_enumeration(k, d, dna_list):
    '''Returns all (k, d)-motifs that are shared by all sequences in dna_list.'''

    # Generate sets of (k,d)-motifs for each dna sequence in the list.
    motif_sets = [{kmer for i in xrange(len(dna)-k+1) for kmer in neighbors(dna[i:i+k], d)} for dna in dna_list]

    # Intersect all sets to get the common elements.  The answers are displayed as sorted, so we'll sort too.
    return sorted(list(reduce(lambda a,b: a & b, motif_sets)))


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('/home/david/Downloads/dataset_156_7.txt') as input_data:
        k, d = map(int, input_data.readline().split())
        dna_list = [line.strip() for line in input_data.readlines()]

    # Get the motifs.
    motifs = motif_enumeration(k, d, dna_list)

    # Print and save the answer.
    print ' '. join(motifs)
    with open('Textbook_03A.txt', 'w') as output_data:
        output_data.write(' '.join(motifs))

if __name__ == '__main__':
    main()