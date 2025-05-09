#pedir datos
print("Hi! ,how old are you?")
age = int(input("tell me your age"))
if age <10:
    print("you are child")
elif age >10 and age <17:
    print("you are teenager")
elif age >18 and age <60:
    print("you are and adult")   
else:
    print("thanks for the information")     
