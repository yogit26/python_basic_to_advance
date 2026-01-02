'''
Sometimes we want to repeat a set of statements in our program for instance: pt
1 to 10000

loops make it easy for a programming to tell the computer which set of instructions to reapeat and how!

# TYPES OF LOOPS IN PYTHON

PRIMARY THERE ARRE TWO TYPES OF LOOPS IN PYTHON.

1.) WHILE LOOPS
2.) FOR LOOPS


print(1)
print(2)
print(3)
print(4)
'''
# The same task can be done like this

# for i in range(1,5):
#     print(i)


# WHILE LOOPS :-) THE BLOCK KEEPS EXECUTING UNTILL THE CONDITION IS TRUE (BODY OF THE LOOP)

# i= 1 
# while(i<=50):
#     print(i)
#     i +=1



l=[1,3,4,5,6,"harry","marry","sharry"]

i=0

while(i<len(l)):
    print(l[i])
    i =i+1