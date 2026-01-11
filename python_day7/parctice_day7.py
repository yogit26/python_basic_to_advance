# 1.) write a program using funcions to find greatest of three numbers.


# a =1
# b =24
# c =3

# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>b and c>a):
#         return c
    

# print(greatest(a,b,c))



# 2.) write a program using function to convert celsius to Fahrenheit.

# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temperature in f: "))
# print(f_to_c(f))


# ====================================================

# How do you prevent a python print () functions to print a new line at the end.



# print("a")
# print("b")
# print("c", end= "")
# print("d", end= "")


# ============================================================================================


# write a recursive function to calculate the sum of first n natural numbers.



# sum(1) = 1
# sum(2) = 1 + 2
# sum(3) = 1 + 2 + 3
# sum(4) = 1 + 2 + 3 + 4
# sum(5) = 1 + 2 + 3 + 4 + 5


# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print(sum(4))



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# write a pyhon funtions to print first n lines of the following pattern.

# ***
# **
# *
# -for n=3



# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(3)

# ==============================================================

#6.) Write  a python program convert inches to cms.

# def covert(inch):
#     return inch *2.54

# n = int(input("Enter the value of inches"))

# print(f" The coressponding value in cms is {covert(n)}")



# ======================================================================


#7.) write a python function to remove a given word from a list and strip it at the same time.


# def rem(l, word):
#     n=[     ]
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# l =["monu","sonu","sona","sana","ua"]

# print(rem(l,"ua"))



# ======================================================================

# write a python function to print multiplication table of a given number.


def multi(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

multi(5)