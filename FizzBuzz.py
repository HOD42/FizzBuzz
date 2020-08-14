# Use modulus to check if divisible by 3
def checkMultipleOf3(num):
    if num % 3: 
        return(False)
    else:
        return(True)

# Use modulus to check if divisible by 5
def checkMultipleOf5(num):
    if num % 5: 
        return(False)
    else:
        return(True)

# Use modulus to check if divisible by 7
def checkMultipleOf7(num):
    if num % 7: 
        return(False)
    else:
        return(True)

for num in range(1,101):
    if checkMultipleOf3(num):
        print ("Fizz",end="")
    if checkMultipleOf5(num):
        print ("Buzz",end="")
    if checkMultipleOf7(num):
        print ("Bang",end="")
    if not checkMultipleOf3(num) and not checkMultipleOf5(num) and not checkMultipleOf7(num):
        print ("num=",num," ",end="")
    print ("")