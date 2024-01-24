# Degault Arguments
def average(a=2, b=4):
    print("the average is" , (a+b)*2)
average()

'''
# Rewriting the default arguments
def average(a=2, b=4):
    print("the average is" , (a+b)*2)
average(1, 4) # the default will be replaced
'''

'''
# What if we give value only one arg
def average(a, b=4):
    print("the average is" , (a+b)*2)
average(1) # 1 will be givin to a
'''

'''
# What if we don't give value to second arg
def average(a=2, b):
    print("the average is" , (a+b)*2)
average(b=1) # 1 will be givin to b
'''