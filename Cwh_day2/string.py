name = "yogit" # double quotes

# name2 = 'yogit' # single quotes
# name3 = '''yogit'''# multi quotes
num = 123456789

nameshort = name[0:3]
print(nameshort)
character =name[-1]
print(character)

print(name[:5]) # is same as print (name[0:5])
print(name[1:]) # it is default value use (name [1:5])

num_str=(str(num)) # it convert str to integer 
print(num_str[1:8:2]) # it take same as normal but it is skip 2 num 

print(len(num_str)) # print lenght of srting
print(name.endswith("yog")) # check the word end with .....

print(name.startswith("git")) # chech the words starts with ....

print(name.capitalize())  # it convert the first alphabet of words

chn = "Hello World" # is use tp change the word os string
rep=chn.replace("World", "python")
print(rep)