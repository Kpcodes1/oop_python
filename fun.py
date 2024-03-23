def calc(C):
    return round(C * 0.20, 2)

def tip():
    num1 = int(input("Enter a Number? "))
    tip_amount = calc(num1)
    print("The average tip(20%) is $", tip_amount)

tip()