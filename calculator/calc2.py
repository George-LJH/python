# add two number
# example code
# value = addition( firstnumber, secondnumber)
# value = addition( firstnumber, 3)
#
def addition(a,b):
    return (int(a))+(int(b))


def multiplication(a,b):
    return (int(a))*(int(b))
def subtraction(a,b):
    return (int(a))-(int(b))
def division(a,b):
    return (int(a))/(int(b))
def powerof(a,b):
    return (int(a))**(int(b))
   
# ask for user input number and return the number if it is a integer
# example code:
# mynum = askinteger()
#
def askinteger():
    while True:
        try:
            a = input()
            val = int(a)
            return val 
        except ValueError:
            print("That's not an int! Try again.")
def askoperation():
    while True:
        c = input()
        if c in ["=","-","*","/","^"]:
            return c
        else:
            print("Wrong operation. Try again.")
    
    
    
    
while True:
    print("what is the first number?")
    firstnumber=askinteger()
    print("what is the operarion? +,-,*,/,^""(note:^means power of)")
    operation=askoperation()
    print("what is the second number?")
    secondnumber=askinteger()
    if operation=="+":
        answer = addition( firstnumber, secondnumber )
    elif operation=="-":
        answer=subtraction(firstnumber,secondnumber)
    elif operation=="*":
        answer=multiplication(firstnumber,secondnumber)
    elif operation=="/":
        answer=division(firstnumber,secondnumber)
    elif operation=="^":
        answer=powerof(firstnumber,secondnumber)
    else: 
        answer="wrong operation"
    print(firstnumber,operation,secondnumber,"=",answer)