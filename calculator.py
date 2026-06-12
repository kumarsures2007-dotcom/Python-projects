def additon(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def  divition(x,y):
    if y==0:
       return "Error: Cannot divide by zero"
    return x/y
print("======Simple Calculator======")
while True:
    print("-------Select Option--------")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4:Division")
    print("5: Exit")
    choice=input("Enter a number(1-5):")
    if choice=='5':
        print(" ...!Existing Calculator.....BYE BYE ..")
        break
    if choice in ['1','2','3','4']:
        num1=float(input("Enter The First Number: "))
        num2=float(input("Enter The Second Number: "))
        if choice=='1':
            print("Result: ",addition(num1,num2))
        elif choice=='2':
            print("Result: ",subtract(num1,num2))
        elif choice=='3':
            print("Result: ",multiplication(num1,num2))
        elif choice=='4':
            print("Result: ",divition(num1,num2))
else:
    print("Invalid Choice ..Try again Sorry..!!!")


