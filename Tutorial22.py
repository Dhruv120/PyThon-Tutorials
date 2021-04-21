# try except exception handlind in python

a=5
b= int(input("enter b \n"))

c=a+b
sd = False

try:
    if(sd):
        d=6
    print(d)

    print("success")

except Exception  as e:
    print(f"It failed because of this error -->{e}")

print("some more lines")        