#IF STATEMENT:
#if → Executes a block of code only if the condition is true.

#EX:
num = 10
if num > 0:
    print("Number is positive")

#IF ELSE STATEMENT:
#if...else → Executes one block if condition is true, otherwise another block.

#EX:
num = -5
if num >= 0:
    print("Number is positive")
else:
    print("Number is negative")

#ELIF STATEMENT:
    #if...elif...else → Checks multiple conditions in order, 
    #executes the block of the first true condition, else runs the final block.

#EX:
num = 0
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#NESTED IF:
#A nested if means placing one if statement inside another. It is useful when decisions depend on multiple conditions.

#Example:
age = 19
citizen = True
if age >= 18:
    if citizen:
        print("You are eligible to vote in this country.")
    else:
        print("You must be a citizen to vote.")
else:
    print("You are not old enough to vote.")    