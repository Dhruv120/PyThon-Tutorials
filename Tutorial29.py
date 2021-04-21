# list comphrension

myfood = ["apple","orange ",25,89,"banana"]

nonint = []

# without using list comphrension
for item in myfood:
    if not str(item).isdigit():
        nonint.append(item)

print(nonint)        

# using list comphrension

nonint2 = [item for item in myfood if not str(item).isdigit()]
print(nonint2)