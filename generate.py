def main():
    num = input("Unverse Answers? ")
    fort(num)



def fort(x):
    
    x = x.lower()
    if x == "42":
        print("Yes")
    elif x == "forty two":
        print("Yes")
    elif x == "forty-two":
        print("Yes")
    else:
        print("No")


main()
