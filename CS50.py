# HARVARD CS50 COURSE

s = input("Do you agree? ")

if s == 'Y' or s == 'y':
    print('Agreed.')
elif s == 'N' or s == 'n':
    print('not agreed.')

# OR
    
x = input('Do you agree? ')

if x.lower() in ['y', 'yes']:
    print("Agree.")
elif x.lower() in ['N', 'no']:
    print("Not agree.")
# ---------------------------------

for i in range(3):
    print('meow')
# ---------------------------------

def dog():
    print('bark')

for i in range(3):
    dog()
#----------------------------------
    
def main():
    theory(3)

def theory(n):
    for i in range(n):
        print('theory')

main()