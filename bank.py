def main():
    num = str(input("Greeting: "))
    greet(num)

def greet(x):
    x = x.lower().strip()
    if x == "hello":
        print("$0")
    elif x[0] =="h":
        print("$20")
    else:
        print("$100")

main()