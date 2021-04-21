# Collectio 1 ---- LIST

mygrocery= ["banana","guava","range",10,25]
print(type(mygrocery))


mygrocery[2] = "dhruv"      # change list
print(mygrocery) 
print(len(mygrocery))
print(len(mygrocery[0]))

mygrocery.append("rahul")        #add element
print(mygrocery)

mygrocery.insert(3, "ketan")        # need to indicate index as well
print(mygrocery)

mygrocery.remove("ketan")        
print(mygrocery)

mygrocery.pop()    # remove last element
print(mygrocery)

