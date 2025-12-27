# Methods of dictionary 

marks={
    "mohit" :  90,
    "rohit" : 70,
    "sohit":  75,
    "shivi" : 80
}
# print(marks.items()) # print all of item of dictionary

# print(marks.key()) # print the key of dic.

# print(marks.values()) # print the value of dic.

# marks.update({"mohit": 85, "unknown":90 })  # thupdate method is still change and update the original list (key and value)  


# print(marks.get("Rohit"))  # same but it is show none the output 

# print(marks("Rohit"))  # but  it is show the error 

# print(marks.pop("rohit")) #Remove key and return the correspongind value.if the key is not found "default" is returned if provide otherwise 'KeyError is raised 

item = marks.popitem()  #  popitems is used to (((((((last-in-first-out)))))))
print(item)           