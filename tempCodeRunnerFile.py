def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while True:
        if int(s) >= 2 and int(s) <= 6:
            return s
        break        
        
            

        
    
        


main()