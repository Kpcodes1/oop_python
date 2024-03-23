def main():
    smile = str(input(""))
    convert(smile)
    
    

def convert(x):
    if x == ":)":
        return "🙂" 
    elif x == ":(":
        return ("🙁") 
    else:
        return("😐") 
    


        

main()