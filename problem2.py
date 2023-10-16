#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

x = input('enter a number')
x = int(x)
if x % 2 == 0:
    print("this number is an interger")
elif x % 2 == 1:
    print("this number is an integer")
else:
    print("this number is not an integer")
