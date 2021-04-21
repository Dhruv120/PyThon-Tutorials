# string



name="dhruv"  # string literal

description = '''my
name
is dhruvv '''

print(description)
print(name[0])
print(name[0:4])
print(len(name))


fresh = " Mohan "         # strip is used to remove the space
print(fresh.strip())
print(fresh.lower()) 
print(fresh.upper()) 
print(fresh.replace('M','S'))  


nums = "1,2,3,4,5,6,7,8,9"
print(nums.split(","))