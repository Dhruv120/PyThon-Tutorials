# if else condition

age = int(input("Enter your Age: \n"))

name =input("enter your name : \n")

print(f"your age is {age}")

if age<18  or name !="harry" :
    print("you cannot drive")

elif age==20 :
    print("magical")

elif age==40:
    print("super magical")    

else :                    
    print("you can drive") 

if True :         #  this condition is independent of other
    print("I am Always printed")       