import math
#help = input("PythonCalc V 1.0; Say 'help' for more info, and 'ready' to start the calculator.")
#if help== "help" or "Help":
#  print("Signs: '+', '-', '*', '/', '^2', 'sqrt', '^3', '!', 'power'.")
#else:
print("PythonCalc V 1.0 type help for a list of commands")
sign = input("What sign should I use?")
if sign== "+":
    num1 = int(input("What is the first number?     "))
    num2 = int(input("What is the second number?    "))
    print(num1+num2)
elif sign== "-":
    num1 = int(input("What is the first number?     "))
    num2 = int(input("What is the second number?    "))
    print (num1-num2)
elif sign== "*":
    num1 = int(input("What is the first number?     "))
    num2 = int(input("What is the second number?    "))
    print (num1*num2)
elif sign== "/":
    num1 = int(input("What is the first number?     "))
    num2 = int(input("What is the second number?    "))
    print (num1/num2)
elif sign== "^2":
    num1 = int(input("What is the number you wish to be squared?    "))
    print (num1**2)
elif sign== "^3":
    num1 = int(input("What is the first number?     "))
    num2 = int(input("What is the second number?    "))
    print (num1**3)
elif sign== "power":
    num1 = int(input("What is the first number?     "))
    num2 = int(input("What is the second number?    "))
    print (num1**num2)
elif sign== "sqrt":
    num1 = int(input("What is the number you seek the squae root of?    "))
    print (math.sqrt(num1))
elif sign== "!":
    num1 = int(input("What is the number you seek the factorial of?     "))
    print (factorial(num1))
elif sign== "help":
    print("you can add, subtract, multiply, divide, square, cube, do exponents, find square root, and find factorial.")

else:
    print("I am sorry, but I am unable to process your request.")
