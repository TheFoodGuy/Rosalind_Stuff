# even_line = [] 
# with open('even_read.txt') as f: 
#     count = 0
#     for line in f: 
#         count +=1
#         if count % 2 == 0: 
#             even_line.append(line)
# a = 0
# for line in even_line: 
#     print even_line[a]
#     a+=1
f = open('even_read.txt', 'r')
g = open('even_output.txt', 'w')
for x in f.readlines()[1::2]: #ohhh that's pretty cool '
    g.write(x)
g.close() #don't need this for python 3 '