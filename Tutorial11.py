  # DICTIONERY IN PYTHON
# DICTIONERY IS COLLECTION OF KEY VALUES

dict1 = {
    "name":"dhruv" ,
    "salary" : 1000 ,
    "profession" : "engineer" ,
    "l" : [1,2,3,4,5]
}

print(dict1)
print(type(dict1))

print(type(dict1["l"]))

# dictionery function
print(dict1.get("name"))
a=dict1.keys()
a=dict1.values()
a=dict1.items()
print(a)
