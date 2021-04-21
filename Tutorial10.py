  #                TUPLES
# uncangable

mycar = ("audi" , "mercedes" , "alto")
print(type(mycar))

mycarstemp = list(mycar)  # to convert tuple into list
print(mycarstemp)

mycarstemp[0]="harry"
mycar = tuple(mycarstemp)   # to convert list into tuple
print(mycar)