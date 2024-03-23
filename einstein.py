def main():
    mass = int(input("Whats the mass? "))
    convert(mass)
  
def convert(x):
    energy = x * (300000000.0) ** 2
    print("E:", energy)
    
main()