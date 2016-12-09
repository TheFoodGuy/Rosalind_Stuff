
a = input("What is A?") #100
b = input("What is B?") #110
#adds up to 101 103 105 107 109 = 525
c = 0 
if a < b and b < 10000 : 
    for x in xrange(a,b):
        if x%2 == 1:
            c += a
        a += 1
else: 
    print("out of bound man")

print(c);
