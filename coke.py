accumulator = 0
due_amount = 0

while accumulator < 50:
    coin = int(input("Amount Due: "))
     

    if coin == 25 or coin == 10 or coin == 5:
        accumulator += coin
    
        if accumulator > 50:
            change = accumulator - 50
            print(f"Change owed {change}") 
        else:
            print(f"Amount due: {50 - accumulator}")
    else:
        print("Not valid number! ")
            

