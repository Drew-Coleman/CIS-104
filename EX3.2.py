hours = input("Enter hours worked: ") 
try:
    hours = int(hours)
    
    rate = input("Enter how much you earn per hour: ") 
    
    try:
        rate = float(rate)
        if hours > 40:
            pay = (1.5 * rate * (hours -40) + (40 * rate))
            print(pay)
        else:
            pay = rate * hours
            print(pay)
    except:
        print("Error, please enter a numerica value")
except:
    print("Error, please enter a numerica value")