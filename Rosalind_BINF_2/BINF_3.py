seq = 'TTGTGTC'
new_seq = '' 
for i in seq: 
    if i == 'A':
        new_seq = 'T' + new_seq
    elif i == 'C':
        new_seq = 'G' + new_seq
    elif i == 'G': 
        new_seq = 'C' + new_seq
    else:
        new_seq = 'A' + new_seq
print new_seq
