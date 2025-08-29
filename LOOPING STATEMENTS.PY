#CONDITIONAL STATEMENT:
#Looping statements are used to repeat a block of code multiple times.

#FOR LOOP:
#Definition:
#The for loop is used to iterate (go through) a sequence such as a list, tuple, string, or a range of numbers.

#Example 1 (using range):
for i in range(1, 6):
    print("Number:",i)

#WHILE LOOP:
#Definition:
#The while loop executes a block of code as long as the condition is True.
#It is useful when the number of iterations is not known in advance.

#Example:
count = 1
while count <= 5:
    print("Count is:", count)
    count+= 1

#Nested Loops:
#Definition:
#A nested loop means having one loop inside another loop.

#Example (multiplication table):
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=",i*j)
print("---")