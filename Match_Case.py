# x = int(input("rite da nambar: "))
# # x is the variable to match
# match x:
#     #if x is 0
#     case 0:
#         print("x is zero")
#     #case with if-condition
#     case 4:
#         print("case is 4")
#     case _:
#         print("ich heisse salman")


z = int(input("Enter the value: "))
match z:
    case 0:
        print("z is zero")
    case 4:
        print("z is 4")
    case _ if z!=90:
        print(z, "is not 90")
    case _ if z!=80:
        print(z, "is not 80")
    case _:
        print(z)
