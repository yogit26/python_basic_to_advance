# write a program to find the greatest of four  numbers entered by the User

# a1 = int(input("Enter number 1:"))
# a2 = int(input("Enter number 2:"))
# a3 = int(input("Enter number 3:"))
# a4 = int(input("Enter number 4:"))

# if (a1>a2 and a1>a3 and a1>a4):
#     print("Gretest number is a1: ",a1)
# if (a2>a1 and a2>a3 and a2>a4):
#     print("gretest number is a2 :", a2)
# if (a3>a1 and a3>a2 and a3>a4):
#     print("Gretest number is a3: ", a3)
# if (a4>a1 and a4>a2 and a4>a3):
#     print("Gretest number is a3: ", a4)


# you can also use (elif) 


# ===============================================================================================================


# Write a program to find out whether a student has passed or failed if it requires a tottal of 40% and at least 33% in each subjest to pass. Assume 3 subject and take marks as an input form user



# marks1 = int(input("Enter number 1:"))
# marks2 = int(input("Enter number 2:"))
# marks3 = int(input("Enter number 3:"))
# marks4 = int(input("Enter number 4:"))

# total_percentage = (100*(marks1 + marks2 + marks3 + marks4))/400
# print(total_percentage) 
# if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33 and marks4>=33):
#     print("congratulation your are pass")
# else:
#     print("oh!! your are fail try again next tym")



# ===================================================================================================



'''A spam comment is defined as a text containing following keywords:
make a lot of money , "buy now" , "subcribe this ", "click this" , write a program to delete these spams

'''

# p1= "make a lot of money"
# p2= "buy now"
# p3="subscribe this"
# p4="click the link "

# msg = input("Enter your comment")
# if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
#     print("This comment is a spam")
# else:
#     print("This comment is not a spam ")




# ==========================================================================


# write a program to find  whether a given username contains less than 10 characters or not


# username = input("Enter the username: ")

# if (len(username)<10):
#     print("Your username is contains less than 10 characters ")
# else:
#     print("Your username is contains more than 10 characters ")




# =============================================================================



# write a program  which finds whether a given username is persent in a list or not 



# l =["list", "yogit","shubham", "diya"]
# name = input("Enter your name: ")

# if (name in  l ):
#     print("your name in the list")
# else:
#     print("your name is not persent in the list")


# ==============================================================================



# write  program to calculate the grade of a student from his marks from the synatax (a,b,c,d,e,fail)



# marks = int(input("Enter the your marks "))

# if (marks<=100 and marks>=90):
#     grade = "Ex"
# elif (marks<90 and marks>=80):
#     grade = "A"
# elif (marks<80 and marks>=70):
#     grade = "b"
# elif (marks<70 and marks>=60):
#     grade = "C"
# elif (marks<60 and marks>=50):
#     grade = "D"
# else:
#     (marks<50 )
#     grade = "Fail" 

# print("Your grade is: ", grade )



# ==========================================================================


# write a programming to find out whether a given talking about "input" or not 

# post =input("Enter the post: ")

# if("python".lower() in post.lower()): #change all input lower 
#     print("this post is talking about: ", post)
# else:
#     print("this post is not talking about post ")