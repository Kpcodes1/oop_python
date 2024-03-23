def main():
    num1 = input("Expression: ").split()
    x = int(num1[0])
    y = num1[1]
    z = int(num1[2])
    
    if y == "+":
        print(x+z)
    elif y == "-":
        print(x-z)
    elif y == "/":
        print(x/z)
    elif y == "*":
        print(x*z)
    else:
        print("Enter a number +,-,/,* Another number")



main()