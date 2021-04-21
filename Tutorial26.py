# file handling -  working with file programmicly using python

f = open('firstfile.txt')   # create a file pointer
content = f.read()          # read the content of file
# print(content)
f.close()

f = open('firstfile.txt' , 'a')   # create a file pointer
f.write("he is a good boy")
f.close()


# mode of opening a file
# 1. r --- readmode
# 2. w - writemode
# 3. a = append
# 4. x -- create mode -- it cretae file and show error