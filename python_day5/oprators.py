#  Relational operators  are used to evalute conditions inside the if statements. some example of relational operators are:
'''
(==) equals.
(>=) grater than equal to 
(>=) lesser than equal to 

'''

# logical operators

# In python logical operators operate on conditonal statements. Example
'''
and -true if both oprerands are true else false
or - true if at least one operand is true or else false
not -invents true to false to true 
'''

# YES WE USE MULTIPLE IF IN A SINGLE CODE BUT PROPER WAY 

a = int(input("Enter your age: "))
# if  statememt number 1 
if(a%2 == 0) :
    print("a is even")


# IF STATEMENT NUMBER 2
if (a>=18):
    print("You are the above the age of concert")
    print("enjoye your day")
elif(a<=0):
    print("You are invalide age")
else:
    print("You are the below the age of concert")