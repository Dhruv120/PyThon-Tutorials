#   for else in python

brands = ["ABC","DEF","GHI","JKL","MNO"]

for item in brands :
    print(f"the name of brand is {item}")
    if item == "GHI" :
        break
else :
    print("this is else after for")        
