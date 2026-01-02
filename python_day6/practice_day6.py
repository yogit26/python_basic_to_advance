# 1.) write a program to ptint multiplications table of a number using for loop.

# n =int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n * i}")


# =================================================================

# 2.) solve  a question 1 for while loop

# n =int(input("Enter a number: "))

# i = 1
# while(i<11):
#     print(f"{n} X {i} = {i*n}")
#     i+=1


# ===========================================================================

# 3.) write a program to greet the person names store ina list 'l' and which starats with s

# for ex. l = ["Harry","soham","sachin","rahul"]

# l = ["Harry","soham","sachin","rahul"]

# for name in l:
#     if(name.startswith("s")):
#         print(f"Hello {name}")

# ==============================================================


# 4.) Write a program to fing=d the sum of first n natural numbers is prime or not

# n = int(input("Enter a number: "))

# for i in range(2,n):
#     if(n%i) == 0:
#         print("number is not prime")
#         break
# else:
#     print("number is prime")


# ================================================================


# wirte a program to find the sum of first n   natural number using while loop

# n = int(input("Eneter the number"))
# i = 1
# sum = 0
# while(i<=n):
#     sum += i
#     i+=1

# print(sum)



# ======================================================================



# write a program to calculate the factorial of a given number using for loop.
# for ex. = 5 = 1x2x3x4x5

n = int(input("Enter the number: "))

product =1

for i in range(1, n+1):
    product = product*i

print(f"The factorial of {n} is {product}")
