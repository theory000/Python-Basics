def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a, b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is great")

def isLesser(a, b):
    pass #We use 'pass' in an empty function to prevent errors and work on it later.

a = 9
b = 10
calculateGmean(a, b)
isGreater(a,b)
# if(a>b):
#     print("first number is greater")
# else:
#     print("second number is great")
# gmean1 = (a*b)/(a+b) 
# print(gmean1)

c = 8
d = 7
calculateGmean(c, d)
isGreater(c,d)
# if(c>d):
#     print("first number is greater")
# else:
#     print("second number is great")
# gmean1 = (c*d)/(c+d) 
# print(gmean1)

