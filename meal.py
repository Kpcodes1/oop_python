def main():
    time_str = input("What time is it? ")
    time_hours = convert(time_str)
    if time_hours >= 7.0 and time_hours <= 8.0:
        print("Its breakfest time! ")
    elif time_hours >= 12.0 and time_hours <= 13.0:
        print("Its Lunch time! ")
    elif time_hours >= 18.0 and time_hours <= 19.0:
        print("Its Dinner time! ")
    else:
        print()

def convert(time):
    time = str(time.strip(":"))
    if ":" in time:
        hours, minutes = map(float, time.split(":"))
    else:
        hours = float(time)
        minutes = 0
    return hours + minutes / 60

if __name__ == "__main__":
    main()