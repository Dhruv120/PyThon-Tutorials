# ITERABLE    - python object which has __iter__() method define
# ITERATORS   - python object which has __next__() method define
#Generators - they are itertaors (we use generator when we want to 
   #             store large data and we do not have memory)

def harry():
    for i in range(5):
        yield i

# a= harry()
# print(a.__next__())         
# print(a.__next__())
# print(a.__next__())

name = "harry"
iterator = name.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())