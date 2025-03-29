#Calculator

'''
1. define a function calculator
2. take 3 inputs - type of operation, number 1, number 2
3. add a match statement with type of operation
4. define the case statements
5. take type of operation from user (user input)
6. take two numbers as user inputs
7. call the function with 5 & 6 as parameters
'''

def calculator(operation):
    if(operation > 0 and operation <=6):
        num1 = int(input("Enter number 1:"))
        num2 = int(input("Enter number 2:"))

    match operation:
        case 1:
            print(f"Addition of two numbers is : ",num1+num2)
        case 2:
            print(f"Subtraction of two numbers is : ", num1-num2)
        case 3:
            print(f"Product of two numbers is: ", num1*num2)
        case 4:
            print(f"After dividing num1/num2 :",num1/num2)
        case 5:   
            print(f"{num1}^{num2} :",num1**num2)
        case 6:
            print(f"Remainder :",num1%num2)
        case _:
            print(f"Enter Correct Option")        


operation = int(input("ENTER an operation 1-Addition , 2-Subtraction ,3- Multiplication ,4-Division , 5-Exponent , 6- Remainder : "))

calculator(operation)
                

