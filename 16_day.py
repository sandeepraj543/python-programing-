# Match case statement in python
# python me break lagane ki need nhi hoti hai , jo v case match hota hai wo print ho jata hai, but c,c++,java me break lagana necessary hota hai
# jaise hi pahli case match ho jati hai ye code bahar ho jata hai

x = int(input("Enter any number: "))

match x:
    case 0:
        print("x is zero(0)")
        print("you have no rupees")
    case 1:
        print("x is one(1)")
        print("you have one rupees")
    case 2:
        print("case is two(2)")
        print("you have two rupees")
    # case _:  # default case ko es trah se likha jata hai
    #     print("value of your number is", x)
    # default case me v condition lga skte ho 
    case _ if x != 10:
        print(x, "x is not 10")
    case _ if x != 20:
        print( x, "x is not 20")
    case _:
        print(x)










