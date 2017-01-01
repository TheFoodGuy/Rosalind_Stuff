#this is to test the function of a line split in python 

target_string = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
#print target_string 
new_string = target_string.rstrip().split(' ')
next_string = new_string[6].split(':')
final_string = next_string[0]
print final_string 