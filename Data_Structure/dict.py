#python for everybody - dictionary script that reaads and figures about the greatest number of mail messages 

name = raw_input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
hand = open(name)
